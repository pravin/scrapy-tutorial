from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import random

class PaulSmithSpider(BaseSpider):
	domain_name = "paulsmith.co.uk"
	start_urls = ["http://www.paulsmith.co.uk/paul-smith-jeans-253/category.html"]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		sites = hxs.select('//div[@class="product-group-1"]')
		random.shuffle(sites)
		sites = sites.select('//div[@class="grid c160 product clear"]')
		for site in sites[:3]:
			subsite = site.select('.//div[@class="details"]')
			title = subsite.select('h3[@class="desc"]/text()').extract()
			hlink = site.select('a/@href').extract()
			price = site.select('p[@class="price price-GBP"]/text()').extract()
			image = site.select('a/img/@src').extract()

			print '<div><div style="width:150px;float:left;text-align:center">\
				<img src="%s" alt="" /><br />\
				<p><a href="http://www.paulsmith.co.uk/%s">%s</a><br />%s</p>\
			</div></div>' % (''.join(image), ''.join(hlink), ''.join(title), ''.join(price))

SPIDER = PaulSmithSpider()
