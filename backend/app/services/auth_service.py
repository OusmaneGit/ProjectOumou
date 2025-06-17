from app.models.user import User
from app.extensions import db, bcrypt
from app.utils.exceptions import AuthenticationError, ValidationError


def register_user(data):
    # Validate input
    if not data.get("email") or not data.get("password"):
        raise ValidationError("Email and password are required")

    if User.query.filter_by(email=data["email"]).first():
        raise ValidationError("Email already registered")

    # Create user
    user = User(
        email=data["email"],
        username=data.get("username", data["email"].split("@")[0]),
        is_teacher=data.get("is_teacher", False),
    )
    user.set_password(data["password"])

    # Create profile
    from app.models.user import Profile

    profile = Profile(
        user=user, full_name=data.get("full_name", ""), country=data.get("country", "")
    )

    db.session.add(user)
    db.session.add(profile)
    db.session.commit()

    return user


def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        raise AuthenticationError("Invalid credentials")

    if not user.is_active:
        raise AuthenticationError("Account is inactive")

    return user


def refresh_token(identity):
    from flask_jwt_extended import create_access_token

    return create_access_token(identity=identity)
