# -*- coding: utf-8 -*-


import requests


class ClientCredentialsGrant(object):

    def __init__(self, client_id, client_secret, token_endpoint):
        self._client_id = client_id
        self._client_secret = client_secret
        self._token_endpoint = token_endpoint

    def request_access_token(self):
        response = requests.post(self._token_endpoint,
                                 data={'grant_type': 'client_credentials'},
                                 auth=(self._client_id, self._client_secret))
        return response.json()
