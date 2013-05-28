# -*- coding: utf-8 -*-


from requests.auth import AuthBase


class BearerTokenAuth(AuthBase):

    def __init__(self, access_token):
        self._access_token = access_token

    def __call__(self, request):
        request.headers['Authorization'] = 'Bearer %s' % self._access_token
        return request
