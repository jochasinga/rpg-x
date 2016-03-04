from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'mysecret'

# Set configurations
app.config.from_object('settings.DevelopmentConfig')
db = SQLAlchemy(app)

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app import views, models
