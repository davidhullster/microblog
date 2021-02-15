import os
import uuid
basedir = os.path.abspath(os.path.dirname(__file__))
random_uuid = str(uuid.uuid4())

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or random_uuid
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['davidhullster@gmail.com']
    POSTS_PER_PAGE = 3