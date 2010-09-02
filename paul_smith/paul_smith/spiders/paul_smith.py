from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import random

class PaulSmithSpider(BaseSpider):
	domain_name = "paulsmith.co.uk"
	start_urls = ["http://www.paulsmith.co.uk/paul-smith-jeans-253/category.html"]
	
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		sites = hxs.select('//div[@class="yui-u"]')
		random.shuffle(sites)
		for site in sites[:3]:
			title = site.select('a/strong[@class="thumbnail-text"]/text()').extract()
			hlink = site.select('a/@href').extract()
			price = site.select('a/strong[@class="sale"]/text()').extract()
			image = site.select('a/img/@src').extract()

			print '<div><div style="width:150px;float:left;text-align:center">\
				<img src="%s" alt="" /><br />\
				<p><a href="http://www.paulsmith.co.uk/%s">%s</a><br />%s</p>\
			</div></div>' % (''.join(image), ''.join(hlink), ''.join(title), ''.join(price))

SPIDER = PaulSmithSpider()