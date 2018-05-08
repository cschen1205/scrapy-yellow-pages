# -*- coding: utf-8 -*-
import scrapy


DOMAIN_NAME = 'www.yellowpages.com.sg'

class CrawlSgSpider(scrapy.Spider):
    name = 'crawl_sg'
    allowed_domains = [DOMAIN_NAME]

    def start_requests(self):
        categories = ['cleaning-services']
        for cat in categories:
            url = 'http://' + DOMAIN_NAME + '/category/' + cat
            print('navigate to ', url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        print('user agent: ', response.request.headers['User-Agent'])
        items = response.css('div.company_items').extract()
        for item in items:
            title = item.css('.normal_title::text').extract_first()
            print(title)
        urls = response.xpath('//a').extract()
        print('url:', urls)
        for url in urls:
            yield response.follow(url, callback=self.parse)
