import os

# Project directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Base class for config environment"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    APP_NAME = 'RPG-X'
    DATABASE_OPTIONS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    THREAD_PER_PAGE = 1
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "extremesecret0987"
    SECRET_KEY = "supersecret01234"

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
    TESTING = True
