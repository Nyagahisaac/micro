import os















class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'dsk221541461'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2//username:pssword@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USER_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings

    '''
    pass



class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config:The parent configuration class
    '''
    DEBUG = True
    
config_options = {
    'development': DevConfig,
    'production': ProdConfig
    
}
