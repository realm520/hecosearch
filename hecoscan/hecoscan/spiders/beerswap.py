# -*- coding: utf-8 -*-
import scrapy


class BeerswapSpider(scrapy.Spider):
    name = 'beerswap'
    allowed_domains = ['hecoinfo.com']
    start_urls = ['https://hecoinfo.com/token/0x2866A32f364B67437c442f5a15Fdc992be83CD6f']

    # def start_requests(self):
    #     base_url = "https://hecoinfo.com/token/generic-tokentxns2?contractAddress=0x2866A32f364B67437c442f5a15Fdc992be83CD6f&mode=&sid=0413716dd70ded016028feea87870f6a&m=normal&p="
    #     for page in range(10):
    #         yield scrapy.Request(url=base_url+page, callback=self.parse)

    def parse(self, response):

        pass
