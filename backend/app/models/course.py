from app.extensions import db
from datetime import datetime
import shortuuid


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255), default="category.jpg")
    active = db.Column(db.Boolean, default=True)
    slug = db.Column(db.String(100), unique=True)

    def generate_slug(self):
        from slugify import slugify

        self.slug = slugify(self.title)
        return self.slug


class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"))
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, default=0.00)
    language = db.Column(db.String(20), default="English")
    level = db.Column(db.String(20), default="Beginner")
    platform_status = db.Column(
        db.String(20), default="pending"
    )  # pending, published, rejected
    featured = db.Column(db.Boolean, default=False)
    course_id = db.Column(db.String(20), default=shortuuid.uuid, unique=True)
    slug = db.Column(db.String(200), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    category = db.relationship("Category", backref="courses")
    teacher = db.relationship("Teacher", backref="courses")

    def generate_slug(self):
        from slugify import slugify

        self.slug = f"{slugify(self.title)}-{shortuuid.uuid()[:6]}"
        return self.slug


class Variant(db.Model):
    __tablename__ = "variants"
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))
    title = db.Column(db.String(1000), nullable=False)
    variant_id = db.Column(db.String(20), default=shortuuid.uuid, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    order = db.Column(db.Integer, default=0)

    course = db.relationship("Course", backref="variants")


class VariantItem(db.Model):
    __tablename__ = "variant_items"
    id = db.Column(db.Integer, primary_key=True)
    variant_id = db.Column(db.Integer, db.ForeignKey("variants.id"))
    title = db.Column(db.String(1000), nullable=False)
    description = db.Column(db.Text)
    file_path = db.Column(db.String(255))
    duration = db.Column(db.String(20))
    preview = db.Column(db.Boolean, default=False)
    item_id = db.Column(db.String(20), default=shortuuid.uuid, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    order = db.Column(db.Integer, default=0)

    variant = db.relationship("Variant", backref="items")
