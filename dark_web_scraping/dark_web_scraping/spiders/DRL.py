import scrapy


class DrlSpider(scrapy.Spider):
    name = 'DRL'
    allowed_domains = ['onion']
    start_urls = ['http://link6i54qxpk3ac7.onion/']

    def parse(self, response):
        yield {'text': response.text}
