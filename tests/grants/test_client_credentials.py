# -*- coding: utf-8 -*-


from unittest import TestCase

from requests_oauth2lib.grants import ClientCredentialsGrant


class TestClientCredentials(TestCase):

    def test_should_request_access_token(self):
        client_id = 'client_id'
        client_secret = 'client_secret'
        token_endpoint = 'http://example.org/token'
        grant = ClientCredentialsGrant(client_id, client_secret, token_endpoint)
        access_token = grant.request_access_token()
        self.assertEqual(access_token, 'access_token')
