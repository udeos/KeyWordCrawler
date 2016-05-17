from crawlers.fb import ProfileCrawler

import settings


crawler = ProfileCrawler(settings)
crawler.process()
