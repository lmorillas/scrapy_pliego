# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from pliego.items import PliegoItem

BASE = 'http://subastas.numismaticaycoleccionismo.es/'


class PliegoSpider(scrapy.Spider):
    name = "pliego"
    allowed_domains = ["subastas.numismaticaycoleccionismo.es"]
    start_urls = ('http://subastas.numismaticaycoleccionismo.es/index/viewBatch/18193/26a-subasta-online-24-05-16', )


    def parse(self, response):
        next = response.xpath('//a[@title="View Next Lot"]/@href').extract()
        if next:
            yield Request( BASE + next[0] )

        item = PliegoItem()
        item['url'] = response.url
        item['lotehead'] = response.xpath('//div[@id="table_bids"]//h1/text()').extract()
        item['img_url'] = response.xpath('//img[@class="list_logo"]/@src').extract()
        item['img_desc'] = response.xpath('//img[@class="list_logo"]/@alt').extract()

        _desc = response.xpath('//div[@class="description"]//text()').extract()
        _desc = [d.strip() for d in _desc if d.strip()]
        _desc = [d.strip() for d in _desc if d != '.']

        item['lote'] = _desc[0]
        item['apartado'] = _desc[1]
        item['descripcion'] = _desc[2]

        precio = response.xpath('//td[strong/text()[contains(., "Price")]]/text()').extract()
        if precio:
            precio = precio[-1].strip()
        item['precio'] = precio



        yield item
