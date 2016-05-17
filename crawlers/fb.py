from .base import BaseCrawler
from api.fb import FbApi


class ProfileCrawler(BaseCrawler):

    def __init__(self, settings):
        super().__init__(settings)
        self.api = FbApi(host=settings.HOST, token=settings.TOKEN)

    def callback(self, item, conn):
        print(item)

    def process(self):
        for i in range(10):
            self.queue.put(i)
        self.queue.join()
