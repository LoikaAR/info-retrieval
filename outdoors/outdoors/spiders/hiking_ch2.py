import scrapy

class OutdoorSpider(scrapy.Spider):

    name = "hiking_ch2"

    start_urls = ["https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/"]
    
    def parse_inner(self, response):
        description = response.xpath("//div[@class='richtext']/p/text()").getall()[2]
        yield {'description': description}


    def parse(self, response):
        for element in response.xpath("//article[@class='OfferTeaser grid']"):
            name_full = element.xpath(".//div[@class='OfferTeaser--content']/h3[@class='OfferTeaser--title']/span/text()").get()
            region_full = element.xpath(".//div[@class='OfferTeaser--content']/div[@class='OfferTeaser--text']/text()").get()
            
            name = str(name_full).strip()
            region = str(region_full).strip()
            distance = element.xpath(".//div[@class='OfferTeaser--content']/div[@class='OfferTeaser--meta']/table[@class='OfferTeaser--meta--data']/tr/td[@class='OfferTeaser--meta--data--value']/text()").get()
            duration = element.xpath(".//div[@class='OfferTeaser--content']/div[@class='OfferTeaser--meta']/table[@class='OfferTeaser--meta--data']/tr[2]/td[@class='OfferTeaser--meta--data--value']/text()").get()

            duration = duration if duration is not None else 'n/a h'
            # TODO 
            # get ascent, description

            # link = response.xpath("//a[@class='OfferTeaser--link']/@href").get()
            # desc = scrapy.Request(response.urljoin(link), callback=self.parse_inner)
            # print("DESCPTION:", desc)

            yield {'name': name, 'region': region, 'category': 'Hike', 'distance': distance, 'duration': duration, 'ascent': 'n/a m'}


        all_next_pages = response.css("a.Pagination--link::attr(href)").getall()
        next_page = all_next_pages[-1]
        if next_page:
            print("following to the next page:")
            print(next_page)
            yield response.follow(next_page, callback=self.parse)