__author__ = 'lyb'
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from douban.items import DoubanItem
class doubanspider(CrawlSpider):
    name='douban'
    download_delay=0.5
    allowed_domains=['movie.douban.com']
    start_urls=['http://movie.douban.com/top250']
    rules = [
         Rule(SgmlLinkExtractor(allow=(r'http://movie.douban.com/top250\?start=\d+.*'))),
         Rule(SgmlLinkExtractor(allow=(r'http://movie.douban.com/subject/\d+'),
                               ),
             callback='parse_item',
             follow=True)
    ]

    def parse_item(self,response):
        item=DoubanItem()
        sel=Selector(response)
        item['rank']=sel.xpath('//div[@class="top250"]/span/text()').extract()
        item['title']=sel.xpath('//div[@id="content"]/h1/span[1]/text()').extract()
        item['director']=sel.xpath('//div[@id="info"]/span[1]/span[2]/a/text()').extract()
        item['classification']=sel.xpath('//div[@id="info"]/span[5]/text()').extract()
        item['score']=sel.xpath('//div[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract()

        yield item