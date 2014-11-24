__author__ = 'aurel'

from tornado.web import RequestHandler
from oauth2.web import Request, SiteAdapter
import oauth2


class OAuth2Handler(RequestHandler):
    """
    Dispatches requests to an authorization controller
    """
    def initialize(self, controller):
        self.controller = controller

    def get(self):
        response = self._dispatch_request()
        self._map_response(response)

    def post(self):
        response = self._dispatch_request()
        self._map_response(response)

    def _dispatch_request(self):
        request = Request(request_handler=self)

        return self.controller.dispatch(request, environ={})

    def _map_response(self, response):
        for name, value in list(response.headers.items()):
            self.set_header(name, value)

        self.set_status(response.status_code)
        self.write(response.body)


class WebSiteAdapter(SiteAdapter):
    def authenticate(self, request, environ, scopes):
        return {}


def main():
    pass

if __name__ == "__main__":
    main()