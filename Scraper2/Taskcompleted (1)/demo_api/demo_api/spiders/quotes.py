import scrapy
import json
from ..items import DemoApiItem
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/api/quotes?page=1']

    def parse(self, response):
        res = json.loads(response.body)
        items = DemoApiItem()
        quotes = res.get('quotes')
        for quote in quotes:

           author =  quote.get("author").get("name"),
           tags =  quote.get("tags"),
           text = quote.get("text")
           items['text'] = text
           items['author'] = author
           items['tag'] = tags

           yield items

        has_next = res.get('has_next')
        if has_next:
            next_page_number = res.get('page') + 1
            yield scrapy.Request(
                url = f'https://quotes.toscrape.com/api/quotes?page={next_page_number}',
                callback=self.parse
            )
