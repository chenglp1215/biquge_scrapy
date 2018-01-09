# coding=utf-8
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings

runner = CrawlerRunner(get_project_settings())

d = runner.crawl('biquge')
d.addBoth(lambda _: reactor.stop())
reactor.run()