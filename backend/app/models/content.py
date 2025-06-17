from app.extensions import db
from datetime import datetime
import shortuuid


class QuestionAnswer(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String(1000))
    question_id = db.Column(db.String(20), default=shortuuid.uuid, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    resolved = db.Column(db.Boolean, default=False)

    course = db.relationship("Course", backref="questions")
    user = db.relationship("User", backref="questions")


class Answer(db.Model):
    __tablename__ = "answers"
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    content = db.Column(db.Text)
    answer_id = db.Column(db.String(20), default=shortuuid.uuid, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_teacher = db.Column(db.Boolean, default=False)

    question = db.relationship("QuestionAnswer", backref="answers")
    user = db.relationship("User", backref="answers")


class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("variant_items.id"))
    content = db.Column(db.Text)
    note_id = db.Column(db.String(20), default=shortuuid.uuid, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", backref="notes")
    course = db.relationship("Course", backref="notes")
    item = db.relationship("VariantItem", backref="notes")


class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))
    rating = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text)
    review_id = db.Column(db.String(20), default=shortuuid.uuid, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    approved = db.Column(db.Boolean, default=False)

    user = db.relationship("User", backref="reviews")
    course = db.relationship("Course", backref="reviews")
