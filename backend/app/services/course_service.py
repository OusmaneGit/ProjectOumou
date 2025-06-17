from app.models.course import Course, Variant, VariantItem
from app.models.user import Teacher
from app.extensions import db
from app.utils.exceptions import NotFoundError, PermissionDenied

def create_course(teacher_id, data):
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        raise NotFoundError('Teacher not found')
    
    course = Course(
        teacher=teacher,
        title=data['title'],
        description=data.get('description', ''),
        price=data.get('price', 0),
        language=data.get('language', 'English'),
        level=data.get('level', 'Beginner'),
        category_id=data.get('category_id')
    )
    course.generate_slug()
    
    db.session.add(course)
    db.session.commit()
    return course

def get_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        raise NotFoundError('Course not found')
    return course

def update_course(course_id, teacher_id, data):
    course = Course.query.get(course_id)
    if not course:
        raise NotFoundError('Course not found')
    
    if course.teacher_id != teacher_id:
        raise PermissionDenied('You can only update your own courses')
    
    # Update fields
    for field in ['title', 'description', 'price', 'language', 'level', 'category_id']:
        if field in data:
            setattr(course, field, data[field])
    
    course.generate_slug()
    db.session.commit()
    return course

def add_variant(course_id, data):
    course = get_course(course_id)
    variant = Variant(
        course=course,
        title=data['title'],
        order=data.get('order', 0)
    )
    db.session.add(variant)
    db.session.commit()
    return variant

def add_variant_item(variant_id, data, file=None):
    variant = Variant.query.get(variant_id)
    if not variant:
        raise NotFoundError('Variant not found')
    
    item = VariantItem(
        variant=variant,
        title=data['title'],
        description=data.get('description', ''),
        preview=data.get('preview', False),
        order=data.get('order', 0)
    )
    
    if file:
        from app.services.file_service import save_course_file
        item.file_path = save_course_file(file, variant.course_id)
        
        # Calculate duration for videos
        if file.filename.split('.')[-1] in ['mp4', 'mov']:
            from app.utils.helpers import get_video_duration
            duration = get_video_duration(item.file_path)
            if duration:
                minutes = int(duration // 60)
                seconds = int(duration % 60)
                item.duration = f"{minutes}m {seconds}s"
    
    db.session.add(item)
    db.session.commit()
    return item