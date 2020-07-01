# -*- coding: utf-8 -*-
import scrapy
import json


class GetframeworkSpider(scrapy.Spider):
    name = 'getframework'
    allowed_domains = ['trafic.ro', 'whatcms.org']
    api_key = 'YOUR_WHATCMS.ORG_API_KEY_HERE'
    store_urls = []
    frameworks = {}
    counter = 0

    def start_requests(self):
        start_urls = ['http://www.trafic.ro/vizitatori/top-siteuri-comert-electronic/saptamana',
                'http://www.trafic.ro/vizitatori/top-siteuri-comert-electronic/saptamana-pg2',
                'http://www.trafic.ro/vizitatori/top-siteuri-comert-electronic/saptamana-pg3',
                'http://www.trafic.ro/vizitatori/top-siteuri-comert-electronic/saptamana-pg4',
                'http://www.trafic.ro/vizitatori/top-siteuri-comert-electronic/saptamana-pg5',
                'http://www.trafic.ro/vizitatori/top-siteuri-comert-electronic/saptamana-pg6',
                'http://www.trafic.ro/vizitatori/top-siteuri-comert-electronic/saptamana-pg7',
                'http://www.trafic.ro/vizitatori/top-siteuri-comert-electronic/saptamana-pg8',
                'http://www.trafic.ro/vizitatori/top-siteuri-comert-electronic/saptamana-pg9',
                'http://www.trafic.ro/vizitatori/top-siteuri-comert-electronic/saptamana-pg10',
                'http://www.trafic.ro/vizitatori/top-siteuri-comert-electronic/saptamana-pg11']
        for url in start_urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        # Gets all ecommerce site names
        pre_selectors = response.css('span.titlu_site')
        for selector in pre_selectors:
            text = selector.xpath("text()").extract_first()
            self.store_urls.append(text)
        for link in self.store_urls:
            yield scrapy.Request(url = 'https://whatcms.org/API/CMS?key=' +
                self.api_key + '&url=' + link, callback = self.parse_store)

    def parse_store(self, response):
        # Gets CMS name
        cms = json.loads(response.body)['result']['name']
        # Adds it to dictionary if it doesn't exist
        if cms not in self.frameworks:
            self.frameworks[cms] = 0
        self.frameworks[cms] += 1
        self.counter += 1
        self.logger.info("Crawling info for {} ({}/{})".format(response.url[107:], self.counter, len(self.store_urls)))
        # Writes to file when finished
        if(self.counter == len(self.store_urls)):
            with open('cmslist.txt', 'w') as file:
                file.write(json.dumps(self.frameworks))
            for cms in self.frameworks:
                print("{} -> {}%".format(cms, round(self.frameworks[cms] * 100 / self.counter, 2)))
