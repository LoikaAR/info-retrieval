import scrapy
import time

class QuoteSpider(scrapy.Spider):

    name = "hikes_ch2"

    start_urls = ["https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=2",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=3",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=4",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=5",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=6",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=7",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=8",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=9",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=10",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=11",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=12",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=13",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=14",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=15",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=16",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=17",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=18",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=19",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=20",
                  "https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/?p=21"]

    def parse(self, response):
        for element in response.xpath("//article[@class='OfferTeaser grid']"):
            hike_name_full = element.xpath(".//div[@class='OfferTeaser--content']/h3[@class='OfferTeaser--title']/span/text()").get()
            hike_name_parsed = str(hike_name_full).strip()

            hike_region_full = element.xpath(".//div[@class='OfferTeaser--content']/div[@class='OfferTeaser--text']/text()").get()
            hike_region_parsed = str(hike_region_full).strip()

            hike_distance = element.xpath(".//div[@class='OfferTeaser--content']/div[@class='OfferTeaser--meta']/table[@class='OfferTeaser--meta--data']/tr/td[@class='OfferTeaser--meta--data--value']/text()").get()

            hike_time = element.xpath(".//div[@class='OfferTeaser--content']/div[@class='OfferTeaser--meta']/table[@class='OfferTeaser--meta--data']/tr[2]/td[@class='OfferTeaser--meta--data--value']/text()").get()
            
            yield {'hike_name': hike_name_parsed, 'hike_region': hike_region_parsed, 'hike_distance': hike_distance, 'hike_time': hike_time}

        all_next_pages = response.css("a.Pagination--link::attr(href)").getall()
        # next_page = all_next_pages[-1]
        # if next_page:
        #     print("following to the next page:")
        #     print(next_page)
        #     yield response.follow(next_page, callback=self.parse)