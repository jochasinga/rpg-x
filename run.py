from __future__ import print_function

import tornado
from tornado import autoreload
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.log import enable_pretty_logging
from app import app, db
from app.models import User

enable_pretty_logging()

PORT = 8000

if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(PORT)
    ioloop = tornado.ioloop.IOLoop().instance()

    if User.query.all():
        db.drop_all()
        
    db.create_all()

    print("Server listening at 127.0.0.1:{}".format(PORT))
    ioloop.start()
