from flask import Flask
from config.settings import config
from app.extensions import db, migrate, bcrypt, jwt, cors
from app.database.db_session import init_db
from app.middleware.error_handler import init_error_handler

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    cors.init_app(app, origins=app.config['CORS_ORIGINS'])
    
    # Initialize database
    init_db(app)
    
    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.user import user_bp
    from app.routes.course import course_bp
    from app.routes.enrollment import enrollment_bp
    from app.routes.interaction import interaction_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(course_bp, url_prefix='/api/courses')
    app.register_blueprint(enrollment_bp, url_prefix='/api/enrollments')
    app.register_blueprint(interaction_bp, url_prefix='/api/interactions')
    
    # Initialize error handling
    init_error_handler(app)
    
    return app