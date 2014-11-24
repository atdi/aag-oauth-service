__author__ = 'aurel'

import tornado.ioloop
import tornado.web


class OauthHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([(r"/authorize", OauthHandler)])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()