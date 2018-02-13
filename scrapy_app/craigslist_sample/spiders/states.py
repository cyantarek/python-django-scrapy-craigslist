import scrapy
from craigslist_sample.items import CraigslistSampleStates

class StatesSpider(scrapy.Spider):
    name = "states"
    allowed_domains = ['craigslist.org']
    start_urls = ["https://www.craigslist.org/about/sites"]

    def parse(self, response):
        states = []

        hxs = scrapy.selector.HtmlXPathSelector(response)
        items = hxs.select("//div[@class='colmask'][1]/div/ul/li")

        for item in items:
            state = CraigslistSampleStates()
            state["link"] = item.select("a/@href").extract()[0] + "search/cta?postedToday=1&min_price=2000&max_price=2500&query="
            states.append(state)

        return states

        #     print(item)

            # try:
            #     if item.select("a/@href").extract()[0][-4:] == "org/":
            #         state["link"] = item.select("a/@href").extract()[0] + "search/cta?postedToday=1&min_price=2000&max_price=2500"
            #         if not state["link"] == "":
            #             states.append(state)
            # except:
            #     print(states)
            #     return states