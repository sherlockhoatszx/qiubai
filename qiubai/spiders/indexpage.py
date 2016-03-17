# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 01:20:29 2016

@author: sherlock
"""

import scrapy
from scrapy.http import Request

from qiubai.items import QiubaiItem


class QiuBaiSpider(scrapy.Spider):
    name = 'qiubai'
    start_urls=['http://www.qiushibaike.com']
    
    def parse(self, response):        
        for href in response.xpath('//span[@class="stats-comments"]/a/@href').extract():
            detail_url = response.urljoin(href)
            req = Request(detail_url,self.parse_detail_page) #小括号实例化
            item = QiubaiItem()
            req.meta['item']=item
            yield req 
            #如果返回的是item实例，传给pipeline，如果返回的是request对象，
            # scrapy会智能判断，通过request对象进行请求
            # response抓取下来,回调函数处理它
    def parse_detail_page(self,response):
        item = response.meta['item']
        item['author']=response.xpath('//div[@class="author clearfix"]/a[2]/h2\
        /text()').extract()[0] if response.xpath('//div[@class = "author clearfix"]'\
        ).extract() else ""
        item['content']=response.xpath('//div[@class="content"]/text()').extract()[0]
        #but the crawl content only include one line
        comments = []
        for comment in response.xpath('//div[starts-with (@class,"comment-block \
        clearfix floor")]'):
            comment_author=comment.xpath('./div[2]/a/text()').extract()[0]
            comment_content= comment.xpath('./div[2]/span/text()').extract()[0]
            comments.append({"comment_author":comment_author,"comment_content":\
            comment_content})# comment seems not workding
        item['comments']=comments
        yield item 
            
        
        
        
    