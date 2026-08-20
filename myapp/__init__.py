from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager   
from .views import views
from .auth import auth
from .admin import admin as admin_bp

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    from .views import views
    from .auth import auth
    from .admin import admin as admin_bp

    app.register_blueprint(views)
    app.register_blueprint(auth)
    app.register_blueprint(admin_bp)


    from .models import Customer, Order 

    @login_manager.user_loader
    def load_user(user_id):
        return Customer.query.get(int(user_id))


    with app.app_context():
        db.create_all()
    # ---------------------------------------------------

    return app
