from .crawlers.fb import FbCrawler

from . import settings


crawler = FbCrawler(settings)
crawler.queue