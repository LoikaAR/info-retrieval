import scrapy

class QuoteSpider(scrapy.Spider):

    name = "hikes_ti"

    start_urls = ["https://www.ticinotopten.ch/en/trekking", 
                  "https://www.ticinotopten.ch/en/views",
                  "https://www.ticinotopten.ch/en/parks"]

    def parse(self, response): 
        for element in response.xpath("//div[@class=' item-list col-md-6 col-sm-12 ']"):

            print(element)

            hike_name = element.xpath(".//div[@class='item-text']/div[@class='title']/text()").get()    
            category = element.xpath(".//div[@class='category']/text()").get()	           
            # tags = hike.xpath(".//div[@class='tags']/a[@class='tag']/text()").getall()

            yield {'hike_name': hike_name, 'category': category}

        next_page = response.xpath("//li[@class='nav navbar-primary']/a/@href").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)