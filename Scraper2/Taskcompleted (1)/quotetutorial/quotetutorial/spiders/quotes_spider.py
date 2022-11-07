from gc import callbacks
import scrapy
from scrapy.http import FormRequest
from ..items import QuotetutorialItem
from scrapy.utils.response import open_in_browser
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls= [
        'https://quotes.toscrape.com/login'
    ]

    # def parse(Self,response):
    #     title = response.css('title::text').extract()
    #     yield {'titletext': title}
    def parse(self,response):
       token = response.css('form input::attr(value)').extract_first()
       return FormRequest.from_response(response,formdata={
           'csrf_token': token,
           'username': 'attreya01@gmail.com',
           'password':  'dsadsdsa'
       },callback=self.start_scraping)
       
    def start_scraping(self,response):
        open_in_browser(response)
        items = QuotetutorialItem()
        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:

            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
            items['title'] = title
            items['author'] = author
            items['tag'] = tag


            yield items