import scrapy
from scrapy_app.craigslist_sample.items import CraigslistSampleCars
from scrapy.http import Request
import time



class CarsSpider(scrapy.Spider):

	def __init__(self, model='', *args, **kwargs):
		print("Called")
		super(CarsSpider, self).__init__(*args, **kwargs)

		with open("states_2.csv", "r+") as file:
			lines = (line.rstrip() for line in file)
			# lines = ''.join("%s".join(line for line in lines if line) % "Ford")
			# lines = list(line.append("Ford") for line in lines if line)
			lines = [(line + model) for line in lines if line]

			self.start_urls = lines[:20]

	name = "cars"
	allowed_domains = ['craigslist.org']
	# start_urls = ["https://gadsden.craigslist.org/search/cta?postedToday=1&min_price=2000&max_price=2500"]
	# start_urls = "https://shoals.craigslist.org/search/cta?postedToday=1&min_price=2000&max_price=2500&query=Ford"

	# start_urls = lines


	def parse(self, response):
		cars = []

		hxs = scrapy.selector.HtmlXPathSelector(response)
		items = hxs.select("//p[@class='result-info']")[:1]

		for item in items:
			# car = CraigslistSampleCars
			car = {}
			print(item.select("a/@href").extract()[0])

			car["name"] = item.select("a/text()").extract()[0]

			car["link"] = item.select("a/@href").extract()[0]
			# link = "https://houston.craigslist.org/cto/d/2001-chevy-express-2500/6494745184.html"
			# print(car["link"])
			# yield Request(url=link, callback=self.parse_cars, meta={"car": car, "link": link})

			cars.append(car)
		return cars

	def parse_cars(self, response):
		hxs = scrapy.selector.HtmlXPathSelector(response)
		item = hxs.select("//time[@class='date timeago']/text()").extract()[0].replace("\n", "")

		print(item)

		# if "2" in item:
		#     print(item)
		# if hxs.select("time/text()").extract() == "about an hour ago":
		#     car["link"] = link
		#     return car

		pass
