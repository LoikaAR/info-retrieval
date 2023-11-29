import scrapy

class OutdoorSpider(scrapy.Spider):

    name = "hiking_ti"

    start_urls = ["https://www.ticinotopten.ch/en/trekking", 
                  "https://www.ticinotopten.ch/en/views",
                  "https://www.ticinotopten.ch/en/parks"]

    def parse(self, response): 
        for element in response.xpath("//div[@class=' item-list col-md-6 col-sm-12 ']"):

            name = element.xpath(".//div[@class='item-text']/div[@class='title']/text()").get()
            category = element.xpath(".//div[@class='category']/text()").get()

            link = element.xpath('a/@href').get()
            link = 'https://www.ticinotopten.ch' + str(link)

            yield scrapy.Request(
                url=response.urljoin(link),
                callback=self.parse_inner,
                cb_kwargs={
                            'name': name, 
                            'region': 'Ticino', 
                            'category': category, 
                            'distance': 'n/a km', 
                            'duration': 'n/a h', 
                            'ascent': 'n/a m', 
                            'link': link
                        }
            )

    def parse_inner(self, response, name, region, category, distance, duration, ascent, link):
        desc_short = response.xpath("//div[@class='border-right-lg']/p[@id='short-text']/em/text()").get()
        desc_main = response.xpath("//div[@id='text']/p/text()").getall()

        description = [desc_short] + desc_main

        yield {
                'name': name, 
                'region': region, 
                'category': category, 
                'distance': distance, 
                'duration': duration, 
                'ascent': ascent, 
                'link': link,
                'description': description
               }