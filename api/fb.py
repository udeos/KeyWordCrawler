from .base import BaseApi

from urllib import parse


class FbApi(BaseApi):

    def get_user(self, uid, fields, conn=None):
        uri = '/{uid}/'.format(uid=uid)
        params = {'fields': fields}
        params = parse.urlencode(params)
        status, response = self.request(uri, params, conn=conn)
        return response
