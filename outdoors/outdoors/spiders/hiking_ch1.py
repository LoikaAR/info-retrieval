import scrapy

class QuoteSpider(scrapy.Spider):

    name = "hikes_ch1"

    start_urls = ["https://schweizmobil.ch/en/hiking-in-switzerland/regional-routes"]

    def parse(self, response): 
        for element in response.xpath("//a[@class='flex flex-col bg-white shadow-card mouse:mouse:hover:bg-[#ffffff30] mouse:hover:shadow-card-deep']"):
            

            print(element)
            hike_name = element.xpath(".//div[@class='flex h-full flex-col justify-between p-[16px] xxl:p-[20px]']/div[@class='flex flex-col']/p[@class='card-title  sm:pb-[12px]  break-words pb-[8px]']/text()").get()
            # hike_name = element.xpath(".//div[@class='flex flex-col']/div[@class='title']/text()").get()


            # category = element.xpath(".//div[@class='category']/text()").get()	           
            # tags = hike.xpath(".//div[@class='tags']/a[@class='tag']/text()").getall()

            yield {'hike_name': hike_name}

        next_page = response.xpath("//li[@class='nav navbar-primary']/a/@href").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)