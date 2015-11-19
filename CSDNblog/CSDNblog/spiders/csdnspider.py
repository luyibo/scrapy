__author__ = 'lyb'
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from CSDNblog.items import CsdnblogItem
class CSDNspider(CrawlSpider):
    name='CSDNspider'
    download_delay=2
    allow_domains=['blog.csdn.net']
    start_urls=['http://blog.csdn.net/u012150179/article/details/11749017']
    rules = [
        Rule(SgmlLinkExtractor(allow=('/u012150179/article/details'),
                               restrict_xpaths=('//li[@class="next_article"]')),
             callback='parse_item',
             follow=True)
    ]

    def parse_item(self,response):
        item=CsdnblogItem()
        sel=Selector(response)
        blog_url=str(response.url)
        blog_name=sel.xpath('//div[@id="article_details"]/div/h1/span/a/text()').extract()
        item['article_name']=[n.encode('utf-8') for n in blog_name]
        item['article_url']=blog_url.encode('utf-8')

        yield item