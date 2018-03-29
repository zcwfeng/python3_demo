# scrapy 1.4
import re
import json


from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor  as sle
import codecs
from itzhaopin.items import TencentItem

from scrapy.utils.log import logger as logging


class TencentSpider(CrawlSpider):
    name = "tencent"
    allowed_domains = ["tencent.com"]
    start_urls = [
        "http://hr.tencent.com/position.php"
    ]
    rules = [
        Rule(sle(allow=("/position.php\?&start=\d{,4}#a")), follow=True, callback='parse_item')
    ]

    def parse_item(self, response):
        items = []
        sel = Selector(response)
        base_url = get_base_url(response)
        logging.info("url------baseurl:" + base_url)
        sites_even = sel.css('table.tablelist tr.even')
        for site in sites_even:
            item = TencentItem()
            logging.info("url---even---baseurl:" + base_url)
            item['name'] = site.css('.l.square a').xpath('text()').extract()[0]
            relative_url = site.css('.l.square a').xpath('@href').extract()[0]
            item['detailLink'] = codecs.decode(urljoin_rfc(base_url, relative_url),"utf-8")
            item['catalog'] = site.css('tr > td:nth-child(2)::text').extract()[0]
            item['workLocation'] = site.css('tr > td:nth-child(4)::text').extract()[0]
            item['recruitNumber'] = site.css('tr > td:nth-child(3)::text').extract()[0]
            item['publishTime'] = site.css('tr > td:nth-child(5)::text').extract()[0]
            items.append(item)
            #print repr(item).decode("unicode-escape") + '\n'

        sites_odd = sel.css('table.tablelist tr.odd')
        for site in sites_odd:
            item = TencentItem()
            logging.info("url---odd---baseurl:" + base_url)
            item['name'] = site.css('.l.square a').xpath('text()').extract()[0]
            relative_url = site.css('.l.square a').xpath('@href').extract()[0]
            item['detailLink'] = codecs.decode(urljoin_rfc(base_url, relative_url),"utf-8")
            item['catalog'] = site.css('tr > td:nth-child(2)::text').extract()[0]
            item['workLocation'] = site.css('tr > td:nth-child(4)::text').extract()[0]
            item['recruitNumber'] = site.css('tr > td:nth-child(3)::text').extract()[0]
            item['publishTime'] = site.css('tr > td:nth-child(5)::text').extract()[0]
            items.append(item)
            #print repr(item).decode("unicode-escape") + '\n'

        logging.info('parsed ' + str(response))
        return items


    def _process_request(self, request):
        logging.info('process ' + str(request))
        return request

