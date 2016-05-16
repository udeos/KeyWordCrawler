from urllib import request


class BaseApi:
    def request(self, uri, params, method='GET', conn=None):
        pass
