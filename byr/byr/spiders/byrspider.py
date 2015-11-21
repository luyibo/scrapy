__author__ = 'lyb'
#coding=utf-8
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from byr.items import ByrItem
from scrapy.http import FormRequest,Request
class byrspider(CrawlSpider):
     name='byr'
     allowed_domains=['bbs.byr.cn']
     start_urls=['http://bbs.byr.cn/#!board/Friends']
     rules = (
         Rule(SgmlLinkExtractor(allow=(r'/#!board/Friends\?p=\d'))),
         Rule(SgmlLinkExtractor(allow=(r'/#!board/Friends/\d+')),callback='parse_item')
     )
     headers={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection":"gzip, deflate",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0",
    'Referer':"http://bbs.byr.cn/index",
    'Connection':"keep-alive",
    'x-requested-with':"XMLHttpRequest"
     }
     def start_requests(self):
         return [Request('http://bbs.byr.cn/user/ajax_login.json',headers=self.headers,meta={'cookiejar':1},callback=self.post_login)]

     def post_login(self,response):
         return [FormRequest.from_response(
             response,
             meta={'cookiejar':response.meta['cookiejar']},
             headers=self.headers,
             formdata={
                 'id':"luyiiib",
                 'passwd':"833221",
                 'mode':"0",
                 'CookieDate':"0"
             },
             callback=self.after_login,
         )

         ]

     def after_login(self, response) :
        for url in self.start_urls :
            yield self.make_requests_from_url(url)

     def parse_item(self,response):
         sel=Selector(response)
         item=ByrItem()
         item['title']=sel.xpath('//section[@id="body"]/div[2]/span[2]/text()').extract()
         return item