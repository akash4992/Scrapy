from gc import callbacks
import scrapy
from ..items import AmazontutorialItem
class QuotesSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls= [
        'https://www.amazon.in/s?k=books&crid=1LTR5L5UKZU08&sprefix=books%2Caps%2C196&ref=nb_sb_noss_1'
    ]

    def parse(self,response):
        item = AmazontutorialItem()
        produt_name = response.css('.a-color-base.a-text-normal').extract()
        product_author = response.css('a-row .a-size-base').extract()
        product_price = response.css('.a-price span').extract()
        product_price = response.css('.s-image::attr(src)').extract()

        item['product_name'] = produt_name
        item['product_author'] = product_author
        item['product_price'] = product_price
        item['product_price'] = product_price

        return item


