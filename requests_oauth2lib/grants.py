# -*- coding: utf-8 -*-


class ClientCredentialsGrant(object):

    def __init__(self, client_id, client_secret, token_endpoint):
        self._client_id = client_id
        self._client_secret = client_secret
        self._token_endpoint = token_endpoint

    def request_access_token(self):
        return 'access_token'
