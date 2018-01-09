# coding=utf-8

from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from ..output import output
from ..content_parser import ModifyContent


class BiQuGeSpider(CrawlSpider):
    name = "biquge"
    start_urls = [
        'http://www.biqudu.com/0_398/'
    ]

    rules = (
        Rule(LinkExtractor(allow=(r'http://www.biqudu.com/0_\d+/\d+.html',)),
             callback='parse_content',
             follow=False, ),
    )

    def parse_content(self, response):
        mc = ModifyContent(response.text)
        mc.del_tag("script")
        title = mc.get_title().encode("utf-8")
        content = mc.get_content().encode("utf-8")
        index = response.url[-12: -5]
        output.output(index+title, content)
        print ("url: %s, status: %s" % (response.url, response.status))
