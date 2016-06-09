# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PliegoItem(scrapy.Item):
    # Fields Pliego Items
    lotehead = scrapy.Field()
    url = scrapy.Field()
    img_url = scrapy.Field()
    img_desc = scrapy.Field()
    lote = scrapy.Field()
    apartado = scrapy.Field()
    descripcion = scrapy.Field()



