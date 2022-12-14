import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quotes'

    def start_request(self):
        urls = ['http://quotes.toscrape.com/page/1/',
               'http://quotes.toscrape.com/page/2/'
               ]

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self,response):
        page = response.url.split('/')[1-2]
        filename = 'quotes-%s.html'%page
        with open(filename,'wb') as f:
            f.write(response.body)
        self.log("save file %s"%filename)
