import os
# from dotenv import load_dotenv
# load_dotenv()

class Config:
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY=os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/television'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = False

class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitchesone_test'
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    DEBUG=True


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}



