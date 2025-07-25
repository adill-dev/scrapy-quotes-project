import scrapy

class TagSpider(scrapy.Spider):
    name = "tag"

    async def start(self):
        url = "https://quotes.toscrape.com/"
        tag =  getattr(self, "tag", None)

        if tag is not None:
            url = url + 'tag/' + tag
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get()
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)            

     