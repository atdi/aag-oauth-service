__author__ = 'aurel'

import unittest
from unittest.mock import MagicMock
from aag.oauth.server import OAuth2Handler


class OAuth2HandlerTest(unittest.TestCase):
    def setUp(self):
        #request_handler =
        handler = OAuth2Handler()
