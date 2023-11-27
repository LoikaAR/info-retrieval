import scrapy
import time

class HikeSpider(scrapy.Spider):

    name = "hikes_ch2"

    start_urls = ["https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/"]
    
    def parse_inner(self, response):
        description = response.xpath("//div[@class='richtext']/p/text()").getall()[2]
        yield {'description': description}


    def parse(self, response):
        for element in response.xpath("//article[@class='OfferTeaser grid']"):
            hike_name_full = element.xpath(".//div[@class='OfferTeaser--content']/h3[@class='OfferTeaser--title']/span/text()").get()
            hike_region_full = element.xpath(".//div[@class='OfferTeaser--content']/div[@class='OfferTeaser--text']/text()").get()
            
            hike_name_parsed = str(hike_name_full).strip()
            hike_region_parsed = str(hike_region_full).strip()
            hike_distance = element.xpath(".//div[@class='OfferTeaser--content']/div[@class='OfferTeaser--meta']/table[@class='OfferTeaser--meta--data']/tr/td[@class='OfferTeaser--meta--data--value']/text()").get()
            hike_time = element.xpath(".//div[@class='OfferTeaser--content']/div[@class='OfferTeaser--meta']/table[@class='OfferTeaser--meta--data']/tr[2]/td[@class='OfferTeaser--meta--data--value']/text()").get()

            link = response.xpath("//a[@class='OfferTeaser--link']/@href").get()
            desc = scrapy.Request(response.urljoin(link), callback=self.parse_inner)
            # print("DESCPTION:", desc)

            yield {'hike_name': hike_name_parsed, 'hike_region': hike_region_parsed, 'hike_distance': hike_distance, 'hike_time': hike_time, 'description': desc}


        all_next_pages = response.css("a.Pagination--link::attr(href)").getall()
        next_page = all_next_pages[-1]
        if next_page:
            print("following to the next page:")
            print(next_page)
            yield response.follow(next_page, callback=self.parse)