import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ["SECRET_KEY"]


class LocalConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
