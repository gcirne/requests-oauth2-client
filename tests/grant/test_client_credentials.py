# -*- coding: utf-8 -*-


from mock import patch
from unittest import TestCase

from requests_oauth2lib.grant import ClientCredentialsGrant


class TestClientCredentials(TestCase):

    @patch('requests.post')
    def test_should_request_access_token(self, post):
        client_id = 'client_id'
        client_secret = 'client_secret'
        token_endpoint = 'http://example.org/token'
        grant = ClientCredentialsGrant(client_id, client_secret, token_endpoint)

        post.return_value.json.return_value = {'access_token': 'accesstoken'}
        access_token = grant.request_access_token()

        post.assert_called_with(token_endpoint, data={'grant_type': 'client_credentials'})
        self.assertEqual(access_token, {'access_token': 'accesstoken'})
