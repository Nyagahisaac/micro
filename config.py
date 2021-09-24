import os



class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'dsk221541461'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://isaac:2face@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USER_TLS = True
    MAIL_USERNAME = os.environ.get('nyagahisaac21@gmail.com')
    MAIL_PASSWORD = os.environ.get('2face')
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
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://isaac:2face@localhost/pitch'
    
    DEBUG = True
    
config_options = {
    'development': DevConfig,
    'production': ProdConfig
    
}
