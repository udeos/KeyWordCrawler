from .base import BaseApi


class FbApi(BaseApi):

    def __init__(self, token, host):
        self.token = token
        self.host = host

    def get_user(self, uid, fields, conn=None):
        uri = '/{uid}/'.format(uid=uid)
        params = {'fields': fields}
        response = self.request(uri, params, conn=conn)
