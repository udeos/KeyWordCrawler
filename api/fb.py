from .base import BaseApi


class FbApi(BaseApi):

    def get_user(self, uid, fields=None, conn=None):
        uri = '/{uid}/'.format(uid=uid)
        params = {}
        if fields:
            params['fields'] = fields
        return self.get(uri, params, conn=conn)

    def get_user_friends(self, uid):
        friends = []
        return friends
