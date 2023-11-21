import scrapy

class QuoteSpider(scrapy.Spider):

    name = "hikes"

    start_urls = ["https://www.ticinotopten.ch/en/trekking", 
                  "https://www.ticinotopten.ch/en/monuments",
                  "https://www.ticinotopten.ch/en/villages",
                  "https://www.ticinotopten.ch/en/views",
                  "https://www.ticinotopten.ch/en/parks",
                  "https://www.ticinotopten.ch/en/water",
                  "https://www.ticinotopten.ch/en/museums",
                  "https://www.ticinotopten.ch/en/adventure",
                  "https://www.ticinotopten.ch/en/experience",
                  "https://www.ticinotopten.ch/en/specialties"] # URLs list to start crawling.

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