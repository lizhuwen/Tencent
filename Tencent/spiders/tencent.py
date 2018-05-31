#  -*- coding: utf-8 -*-

import scrapy
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
	name = 'tencent'
	allowed_domains = ['tencent.com']
	url = "http://hr.tencent.com/position.php?&start="
	offset = 0
	start_urls = [url+str(offset)]

	def parse(self,response):
		node_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
		for node in node_list:
			item = TencentItem()

			# 文本内容, 取列表的第一个元素[0], 并且将提取出来的Unicode编码 转为 utf-8
			item['positionName'] = node.xpath("./td[1]/a/text()").extract()[0]#.encode("utf-8")
			item['positionLink'] = node.xpath("./td[1]/a/@href").extract()[0]#.encode("utf-8")
			
			try:
				item['positionType'] =node.xpath("./td[2]/text()").extract()[0]#.encode("utf-8")
			except:
				item['positionType'] = ''

			item['positionNumber'] = node.xpath("./td[3]/text()").extract()[0]#.encode("utf-8")
			item['workLocation'] = node.xpath("./td[4]/text()").extract()[0]#.encode("utf-8")
			item['publishTime'] = node.xpath("./td[5]/text()").extract()[0]#.encode("utf-8")
			print(item)
			yield item

		#offset设置
		## 第一种写法：拼接URL，适用场景：页面没有可以点击的请求链接，必须通过拼接URL才能获取响应
		'''if self.offset < 20:
			self.offset += 10
			url = self.url + str(self.offset)
		
			yield scrapy.Request(url,callback=self.parse)
		'''
		#第二种方法：直接从response获取需要爬取得连接，并发送请求处理，知道全部提取完
		if len(response.xpath("//a[@class='noactive' and @id='next']")) == 0:
			url = response.xpath("//a[@id='next']/@href").extract()[0]
			yield scrapy.Request("http://hr.tencent.com/"+ url, callback=self.parse)

