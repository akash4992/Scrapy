import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_nav_0'
        ]

    def parse(self, response):
        items = AmazontutorialItem()
        product_name = response.css('.p13n-sc-truncated::text').extract()
        product_author = response.css('.a-link-normal+ .a-size-small .a-size-small').css('::text').extract()
        product_price = response.css('.p13n-sc-price').css('::text').extract()
        product_imagelink = response.css('.a-spacing-small img::attr(src)').extract()
        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink
        yield items


        
