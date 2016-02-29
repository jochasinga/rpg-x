from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from redis import Redis

app = Flask(__name__)

# Set configurations
app.config.from_object('settings')

# Define database object
db = SQLAlchemy(app)

redis = Redis(host='redis', port=6379)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app import views
