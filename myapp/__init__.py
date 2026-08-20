from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # points to auth blueprint

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from .views import views
    from .auth import auth
    from .admin import admin as admin_bp

    app.register_blueprint(views)
    app.register_blueprint(auth)
    app.register_blueprint(admin_bp)

    # User loader
    from .models import Customer, Order  # Import Order too so tables exist

    @login_manager.user_loader
    def load_user(user_id):
        return Customer.query.get(int(user_id))

    # -------------------- ADD THIS --------------------
    # Create all tables if they don't exist yet
    with app.app_context():
        db.create_all()
    # ---------------------------------------------------

    return app
