# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

"""
职位名：positionName
职位链接：positionLink
职位类型：positionType
职位人数：positionNumber
工作地点：workLocation
发布时点：publishTime
"""

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #职位名
    positionName =scrapy.Field()
    #职位链接
    positionLink =scrapy.Field()
    #职位类型
    positionType =scrapy.Field()
    #职位人数
    positionNumber =scrapy.Field()
    #工作地点
    workLocation =scrapy.Field()
    #发布时间
    publishTime =scrapy.Field()

