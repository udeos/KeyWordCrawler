from .base import BaseCrawler
from api.fb import FbApi
from api.exceptions import BadRequestError


class ProfileCrawler(BaseCrawler):

    def __init__(self, settings):
        super().__init__(settings)
        self.api = FbApi(host=settings.HOST, token=settings.TOKEN)

    def callback(self, uid, conn):
        try:
            response = self.api.get_user(uid, conn=conn)
            print(response)
        except BadRequestError as e:
            print(e)

    def process(self):
        for i in ['1016651418404325'] * 10:
            self.queue.put(i)
        self.queue.join()
