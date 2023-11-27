import scrapy

class HikeSpider(scrapy.Spider):

    name = "hikes_ch1"

    start_urls = ["https://www.zermatt.ch/en/Media/Planning-hikes-tours"]

    def parse(self, response): 
        for element in response.xpath("//li[@class=']"):
            

            print(element)
            hike_name = element.xpath(".//div[@class='line-view line-view--alpstein_tour alpsteinTracking thumbnail_line ez_ias").get()
            # hike_name = element.xpath(".//div[@class='flex flex-col']/div[@class='title']/text()").get()


            # category = element.xpath(".//div[@class='category']/text()").get()	           
            # tags = hike.xpath(".//div[@class='tags']/a[@class='tag']/text()").getall()

            yield {'hike_name': hike_name}

        next_page = response.xpath("//li[@class='nav navbar-primary']/a/@href").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)