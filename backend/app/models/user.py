from app.extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_teacher = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    
    profile = db.relationship('Profile', backref='user', uselist=False, cascade='all, delete-orphan')
    teacher = db.relationship('Teacher', backref='user', uselist=False, cascade='all, delete-orphan')
    
    def set_password(self, password):
        from app.extensions import bcrypt
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password):
        from app.extensions import bcrypt
        return bcrypt.check_password_hash(self.password, password)

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    full_name = db.Column(db.String(100))
    bio = db.Column(db.Text)
    image = db.Column(db.String(255), default="default.jpg")
    country = db.Column(db.String(100))

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    image = db.Column(db.String(255), default="default.jpg")
    full_name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.String(100))
    facebook = db.Column(db.String(255))
    twitter = db.Column(db.String(255))
    linkedin = db.Column(db.String(255))
    about = db.Column(db.Text)
    country = db.Column(db.String(100))
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected