from .base import BaseCrawler
from ..api.fb import FbApi


class ProfileCrawler(BaseCrawler):
    def __init__(self, settings):
        super().__init__(settings)
        self.api = FbApi(token=settings.TOKEN, host=settings.HOST)

    def callback(self, item, conn):
        pass
