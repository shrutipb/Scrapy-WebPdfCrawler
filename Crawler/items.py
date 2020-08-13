# -*- coding: utf-8 -*-
import scrapy

class DownloadingFilesItem(scrapy.Item):
    files_urls = scrapy.Field()
    files= scrapy.Field()
