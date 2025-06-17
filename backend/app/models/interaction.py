from app.extensions import db
from datetime import datetime
import shortuuid


class Enrollment(db.Model):
    __tablename__ = "enrollments"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))
    enrollment_id = db.Column(db.String(20), default=shortuuid.uuid, unique=True)
    enrolled_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime)

    user = db.relationship("User", backref="enrollments")
    course = db.relationship("Course", backref="enrollments")


class Progress(db.Model):
    __tablename__ = "progress"
    id = db.Column(db.Integer, primary_key=True)
    enrollment_id = db.Column(db.Integer, db.ForeignKey("enrollments.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("variant_items.id"))
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)

    enrollment = db.relationship("Enrollment", backref="progress")
    item = db.relationship("VariantItem", backref="progress")


class Wishlist(db.Model):
    __tablename__ = "wishlists"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))
    added_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", backref="wishlist")
    course = db.relationship("Course", backref="wishlisted_by")


class Notification(db.Model):
    __tablename__ = "notifications"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    type = db.Column(db.String(50))  # enrollment, progress, message, review, etc.
    message = db.Column(db.String(255))
    read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    link = db.Column(db.String(255))

    user = db.relationship("User", backref="notifications")
