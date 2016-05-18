import json

from http import client
from urllib import parse

from .exceptions import BadRequestError


class BaseApi:

    def __init__(self, host, token):
        self.host = host
        self.token = token

    def get(self, uri, params=None, headers=None, conn=None):
        params = params or {}
        params['access_token'] = self.token
        status_code, response = self._request(
            method='GET',
            uri='?'.join([uri, parse.urlencode(params)]),
            headers=headers,
            conn=conn
        )
        if status_code == 200:
            return response
        if status_code == 400:
            error = response['error']
            raise BadRequestError(
                code=error['code'],
                message=error['message'],
                type=error['type']
            )

    def _request(self, method, uri, body=None, headers=None, conn=None):
        if conn:
            conn = client.HTTPSConnection(self.host)
        conn.request(method, uri, body, headers or {})
        response = conn.getresponse()
        body = response.read().decode()
        return response.status, json.loads(body)
