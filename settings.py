import os

DEBUG = True

# App directory
BASE_DIR = os.path.abspath( os.path.dirname(__file__) )

# Define the database connection
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join( BASE_DIR, 'app.db' )
DATABASE_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Thread options
THREAD_PER_PAGE = 1

# Enable CSRF
CSRF_ENABLED = True

# Use a secret key for signing the data
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"



