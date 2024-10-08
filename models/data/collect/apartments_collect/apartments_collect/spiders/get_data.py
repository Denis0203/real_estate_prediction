import scrapy


class Apartment_Spider(scrapy.Spider):
    name = "Apartment"

    def start_requests(self):
        urls = [
            "https://domclick.ru/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
