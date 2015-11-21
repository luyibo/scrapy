__author__ = 'lyb'
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from zhihu.items import ZhihuItem
class zhihu_spider(CrawlSpider):
    name='zhihu'
    download_delay=0.5
    allowed_domains=['www.zhihu.com']
    start_urls=['http://www.zhihu.com/topic/19642818/top-answers?page=1']
    rules = [
        Rule(SgmlLinkExtractor(allow=(r'http://www.zhihu.com/topic/19642818/top-answers\?page=\d+'),
                               ),
        callback='parse_item',
             follow=True)
    ]

    def parse_item(self,response):
        sel=Selector(response)
        item=ZhihuItem()


        item['question']=sel.xpath('//div[@class="content"]/h2/a/text()').extract()
        #for question in questions:
            #item['question']=question
        #item['answer']=sel.xpath('//textarea/text()').extract()
        item['vote']=sel.xpath('//div/div/div[1]/div[@class="zm-item-vote"]/a/text()').extract()
        item['writer']=sel.xpath('//div/div[1]/div[3]/div[1]/a/text()').extract()



        yield item
