from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from config import config_options 
from flask_mail import Mail
from flask_uploads import UploadSet,configure_uploads,IMAGES





login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
photos = UploadSet('photos',IMAGES)

def create_app(config_name):
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"]  = "sqlite:////test11.db"
    
    app.config.from_object(config_options [config_name])
    
    bootstrap.init_app(app)
    db.init_app(app)
    # db.create_all()
    # db.session.commit()
    login_manager.init_app(app)
    mail.init_app(app)
     
    configure_uploads(app,photos)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    
    from flask_simplemde import SimpleMDE
    simple = SimpleMDE()
    
    simple.init_app(app)
    
    return app
