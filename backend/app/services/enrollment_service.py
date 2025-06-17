from datetime import datetime
from app.models.interaction import Enrollment, Progress
from app.models.course import Course
from app.extensions import db
from app.utils.exceptions import NotFoundError

def enroll_user(user_id, course_id):
    # Check if already enrolled
    if Enrollment.query.filter_by(user_id=user_id, course_id=course_id).first():
        return False, 'Already enrolled in this course'
    
    course = Course.query.get(course_id)
    if not course:
        raise NotFoundError('Course not found')
    
    enrollment = Enrollment(user_id=user_id, course_id=course_id)
    db.session.add(enrollment)
    
    # Add to notifications
    from app.models.interaction import Notification
    notification = Notification(
        user_id=user_id,
        type='enrollment',
        message=f"You've enrolled in {course.title}",
        link=f"/courses/{course.id}"
    )
    db.session.add(notification)
    
    db.session.commit()
    return enrollment

def mark_progress(enrollment_id, item_id):
    enrollment = Enrollment.query.get(enrollment_id)
    if not enrollment:
        raise NotFoundError('Enrollment not found')
    
    # Check if already completed
    if Progress.query.filter_by(enrollment_id=enrollment_id, item_id=item_id).first():
        return False
    
    progress = Progress(enrollment_id=enrollment_id, item_id=item_id)
    db.session.add(progress)
    
    # Check if course completed
    total_items = len(enrollment.course.variants)  # Simplified
    completed_items = len(enrollment.progress)
    
    if completed_items >= total_items:
        enrollment.completed = True
        enrollment.completed_at = datetime.utcnow()
        
        # Add completion notification
        from app.models.interaction import Notification
        notification = Notification(
            user_id=enrollment.user_id,
            type='completion',
            message=f"You've completed {enrollment.course.title}",
            link=f"/courses/{enrollment.course_id}/certificate"
        )
        db.session.add(notification)
    
    db.session.commit()
    return progress