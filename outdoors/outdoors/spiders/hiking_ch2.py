import scrapy

class OutdoorSpider(scrapy.Spider):

    name = "hiking_ch2"

    start_urls = ["https://www.myswitzerland.com/en-ch/experiences/summer-autumn/hiking/hiking-search/"]
    
    def parse(self, response):
        print("status:",response.status)
        for element in response.xpath("//article[@class='OfferTeaser grid']"):
            name_full = element.xpath(".//div[@class='OfferTeaser--content']/h3[@class='OfferTeaser--title']/span/text()").get()
            region_full = element.xpath(".//div[@class='OfferTeaser--content']/div[@class='OfferTeaser--text']/text()").get()
            
            name = str(name_full).strip()
            region = str(region_full).strip()
            duration = element.xpath(".//div[@class='OfferTeaser--content']/div[@class='OfferTeaser--meta']/table[@class='OfferTeaser--meta--data']/tr/td[@class='OfferTeaser--meta--data--value']/text()").get()
            distance = element.xpath(".//div[@class='OfferTeaser--content']/div[@class='OfferTeaser--meta']/table[@class='OfferTeaser--meta--data']/tr[2]/td[@class='OfferTeaser--meta--data--value']/text()").get()
            distance = distance if distance is not None else 'n/a h'
            
            link = element.xpath(".//a[@class='OfferTeaser--link']/@href").get()

            yield scrapy.Request (
                url=response.urljoin(link),
                callback=self.parse_inner,
                cb_kwargs={
                            'name': name, 
                            'region': region, 
                            'category': 'Hike', 
                            'distance': distance, 
                            'duration': duration, 
                            'ascent': 'n/a m', 
                            'link': link
                           }
            )

        all_next_pages = response.css("a.Pagination--link::attr(href)").getall()
        next_page = all_next_pages[-1]
        if next_page:
            print("following to the next page:")
            print(next_page)
            yield response.follow(next_page, callback=self.parse)


    def parse_inner(self, response, name, region, category, distance, duration, ascent, link):
        desc_intro = response.xpath("//div[@class='LeadText--text']/p/text()").get()
        desc_main =  response.xpath("//div[@class='ArticleSubSection--content']/div[@class='richtext']/p/text()").getall()
        
        description = [desc_intro] + desc_main
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