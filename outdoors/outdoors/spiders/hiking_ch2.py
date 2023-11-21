import scrapy

class QuoteSpider(scrapy.Spider):

    name = "hikes_ch2"

    start_urls = ["https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/"]

    def parse(self, response): 
        for element in response.xpath("//article[@class='OfferTeaser grid']"):

            # print(element)
            hike_name_full = element.xpath(".//div[@class='OfferTeaser--content']/h3[@class='OfferTeaser--title']/span/text()").get()
            hike_name_parsed = str(hike_name_full).strip()
            # hike_name = element.xpath(".//div[@class='flex flex-col']/div[@class='title']/text()").get()

            # category = element.xpath(".//div[@class='category']/text()").get()	           
            # tags = hike.xpath(".//div[@class='tags']/a[@class='tag']/text()").getall()

            yield {'hike_name': hike_name_parsed}

        next_page = response.xpath("//li[@class='nav navbar-primary']/a/@href").get()
        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)