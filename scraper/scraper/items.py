# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from properties.models import Property


class ScraperItem(DjangoItem):
    django_model = Property

class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
SPIDER_MODULES = ['scraper.scraper.spiders']
NEWSPIDER_MODULE = 'scraper.scraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# replace this with your actual user-agent value
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# update the pipelines to this
ITEM_PIPELINES = {
   'scraper.scraper.pipelines.PropertyStatusPipeline': 100,
   'scraper.scraper.pipelines.PropertyPricePipeline': 200,
   'scraper.scraper.pipelines.ConvertNumPipeline': 300,
   'scraper.scraper.pipelines.ScraperPipeline': 400,
}
