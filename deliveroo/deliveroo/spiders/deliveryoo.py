import scrapy
import csv 
from ..items import DeliverooItem
import  pandas as pd
class QuoteSpider(scrapy.Spider):
    name = 'deliveryoo'
    start_urls = [
        'https://deliveroo.co.uk/menu/london/soho/wingmans-soho'
        ]
   
    def parse(self,response):
        items = DeliverooItem()
        header = ['title']
        title = response.css("title::text").extract_first()
        heading = response.css("li p::text").extract()
        detail = response.css(".ccl-91a59d84c8a54641 .ccl-9d0a5327c911d0f3::text").extract()
        print("the detail",detail)
        items['title'] = heading
        
        list_data = []
        for data in heading:
            if data not in list_data:
                list_data.append(data)
        list_data.remove("placeholder text")
        list_data.remove("…")
        df = pd.DataFrame()
        df['title'] = list_data
        to_drop = ["placeholder text","…"]
        # df.drop(to_drop)
        df.to_csv('out.csv', index=False)
        # data_list = []
        # for data in heading:
        #     if data not in data_list:
        #         data_list.append(data)
        # print(data_list)
        
        # span = response.css(".ccl-dfaaa1af6c70149c::text").extract()
        # span_text = response.xpath("//*[@class='orderweb__47414d10']//ul/li//*[@class='ccl-91a59d84c8a54641']//p//span//span").extract()
        # span_text = response.css("span.text::text")[0].extract()
        # author_text = response.css(".author::text")[0].extract()
        # response.xpath("//title/text()").extract()
        #response.xpath("//title::text").extract()
        #response.css("li.next a").xpath("@href").extract()
        # print(span_text)
        yield items
