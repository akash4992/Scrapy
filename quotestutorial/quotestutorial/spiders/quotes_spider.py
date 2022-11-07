import scrapy
from ..items import QuotestutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
        ]
   
    def parse(self,response):
        # title = response.css("title::text").extract_first()
        # span_text = response.css("span.text::text")[0].extract()
        # author_text = response.css(".author::text")[0].extract()
        # response.xpath("//title/text()").extract()
        #response.xpath("//title::text").extract()
        #response.css("li.next a").xpath("@href").extract()
        items = QuotestutorialItem()
        all_div_quotes = response.css('div.quote')
        for quote in all_div_quotes:
            title = all_div_quotes.css('span.text::text').extract()
            author = all_div_quotes.css('.author::text').extract()
            tag = all_div_quotes.css('.tag::text').extract()
            items['title'] = title
            items['author']= author
            items['tag'] = tag
            yield items
