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
 
            link = element.xpath(".//a[@class='OfferTeaser--link']/@href").get()

            yield scrapy.Request (
                url=response.urljoin(link),
                callback=self.parse_inner,
                cb_kwargs={
                            'name': name, 
                            'region': region, 
                            'category': 'Hike', 
                            'link': link
                           }
            )

        all_next_pages = response.css("a.Pagination--link::attr(href)").getall()
        next_page = all_next_pages[-1]
        if next_page:
            print("following to the next page:")
            print(next_page)
            yield response.follow(next_page, callback=self.parse)


    def parse_inner(self, response, name, region, category, link):
        desc_intro = response.xpath("//div[@class='LeadText--text']/p/text()").get()
        desc_main =  response.xpath("//div[@class='ArticleSubSection--content']/div[@class='richtext']/p/text()").getall()
        
        description = [desc_intro] + desc_main

        distance = response.xpath("//div[@class='Summary']"\
                                  "/div[@class='Summary--item']"\
                                  "/div[@class='SidebarWidget condensed']"\
                                  "/div[@class='SidebarWidget--body']/span[contains(text(), ' km')]/text()").get() \
                                  .strip(' ').replace('\n', '').replace('\r', '').lstrip()

        ascent = response.xpath("//div[@class='Summary']"\
                                  "/div[@class='Summary--item']"\
                                  "/div[@class='SidebarWidget condensed']"\
                                  "/div[@class='SidebarWidget--body']/span[contains(text(), ' m\r')]/text()").get() \
                                  .strip(' ').replace('\n', '').replace('\r', '').lstrip()

        if response.xpath("//div[@class='Summary']"\
                                  "/div[@class='Summary--item']"\
                                  "/div[@class='SidebarWidget condensed']"\
                                  "/div[@class='SidebarWidget--body']/span[contains(text(), ' h')]/text()") != []:
        
            duration = response.xpath("//div[@class='Summary']"\
                                  "/div[@class='Summary--item']"\
                                  "/div[@class='SidebarWidget condensed']"\
                                  "/div[@class='SidebarWidget--body']/span[contains(text(), ' h')]/text()")\
                                    .get().strip(' ').replace('\n', '').replace('\r', '').lstrip()
        else: duration = 'varies'

        # print('duration:', duration)

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