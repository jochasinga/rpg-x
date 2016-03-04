from __future__ import print_function

import tornado
from tornado import autoreload
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.log import enable_pretty_logging
from app import app, db, admin
from app.models import User, Stage, Candidate, Question, Choice

enable_pretty_logging()

from flask_admin import Admin

PORT = 8000

def init():
    db.drop_all()
    db.create_all()

if __name__ == '__main__':

    init()
    
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(PORT)
    ioloop = tornado.ioloop.IOLoop().instance()
    print("Server listening at 127.0.0.1:{}".format(PORT))

    ioloop.start()
    
