import scrapy

class OutdoorSpider(scrapy.Spider):

    name = "activities_ti"

    start_urls = ["https://www.ticinotopten.ch/en/trekking", 
                  "https://www.ticinotopten.ch/en/monuments",
                  "https://www.ticinotopten.ch/en/villages",
                  "https://www.ticinotopten.ch/en/views",
                  "https://www.ticinotopten.ch/en/parks",
                  "https://www.ticinotopten.ch/en/water",
                  "https://www.ticinotopten.ch/en/museums",
                  "https://www.ticinotopten.ch/en/adventure",
                  "https://www.ticinotopten.ch/en/experience",
                  "https://www.ticinotopten.ch/en/specialties"]

    def parse(self, response): 
        for element in response.xpath("//div[@class=' item-list col-md-6 col-sm-12 ']"):
            print(element)
            name = element.xpath(".//div[@class='item-text']/div[@class='title']/text()").get()
            category = element.xpath(".//div[@class='category']/text()").get()

            yield {'name': name, 'region': 'Ticino', 'category': category, 'distance': 'n/a km', 'duration': 'n/a h', 'ascent': 'n/a m'}
