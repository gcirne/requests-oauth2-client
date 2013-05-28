# -*- coding: utf-8 -*-


from mock import Mock
from unittest import TestCase

from requests_oauth2lib.auth import BearerTokenAuth


class TestBearerTokenAuth(TestCase):

    def test_should_add_authorization_header(self):
        auth = BearerTokenAuth('access_token')
        request = Mock()
        request.headers = {}

        auth(request)

        self.assertEqual(request.headers, {'Authorization': 'Bearer access_token'})
