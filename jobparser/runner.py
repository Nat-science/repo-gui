from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from jobparser import settings
#from jobparser import settings2
from jobparser.spiders.hhru import HhruSpider
from jobparser.spiders.superjobru import SuperjobruSpider

if __name__ == '__main__':
    vacancy = 'Python'

    # crawler_settings2 = Settings()
    # crawler_settings2.setmodule(settings2)
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(SuperjobruSpider, vacancy=vacancy)
    process.crawl(HhruSpider, vacancy=vacancy)

    process.start()