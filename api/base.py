from http import client


class BaseApi:

    def __init__(self, host, token):
        self.host = host
        self.token = token

    def request(self, uri, body=None, headers={}, method='GET', conn=None):
        if conn:
            conn = client.HTTPSConnection(self.host)
        conn.request(method, uri, body, headers)
        response = conn.getresponse()
        return response.status, response.read()
