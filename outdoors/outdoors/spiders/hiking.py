import scrapy

class QuoteSpider(scrapy.Spider):

    name = "hikes"    # Your spider name. Each instance of a QuoteSpider will share the same name.

    start_urls = ["https://www.myswitzerland.com/en-ch/scoprire-la-svizzera/estate-autunno/listicles/wandern-2020/"] # URLs list to start crawling.

    def parse(self, response): # Funcion called every crawled web page. The response parameter will contain the web site response.
        for element in response.xpath("//div[@class='site-content']"): 
            
            hike_name = element.xpath(".//div[@class='l-Gap m-down']/text()").get()    
            # author = hike.xpath(".//small[@class='author']/text()").get()	           
            # tags = hike.xpath(".//div[@class='tags']/a[@class='tag']/text()").getall()

            yield {'hike_name': hike_name}

        next_page = response.xpath("//li[@class='next']/a/@href").get()    # Extract next page link as a string.

        if next_page:	 # If next page is not None, that is, if we have a next page to visit...
            yield response.follow(next_page, callback=self.parse)    # ...follow the next page link. Return the next page response object.