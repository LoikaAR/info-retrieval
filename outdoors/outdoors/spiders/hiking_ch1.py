import scrapy

# activity - type: hike, cycling, other

class OutdoorSpider(scrapy.Spider):

    name = "hiking_ch1"

    start_urls = ["https://www.zermatt.ch/en/Media/Planning-hikes-tours/(offset)/0",
                  "https://www.zermatt.ch/en/Media/Planning-hikes-tours/(offset)/15",
                  "https://www.zermatt.ch/en/Media/Planning-hikes-tours/(offset)/31",
                  "https://www.zermatt.ch/en/Media/Planning-hikes-tours/(offset)/45",
                  "https://www.zermatt.ch/en/Media/Planning-hikes-tours/(offset)/61",
                  "https://www.zermatt.ch/en/Media/Planning-hikes-tours/(offset)/75",
                  "https://www.zermatt.ch/en/Media/Planning-hikes-tours/(offset)/91",
                  "https://www.zermatt.ch/en/Media/Planning-hikes-tours/(offset)/105",
                  "https://www.zermatt.ch/en/Media/Planning-hikes-tours/(offset)/121",
                  "https://www.zermatt.ch/en/Media/Planning-hikes-tours/(offset)/135"]

    def parse(self, response): 
        for element in response.xpath("//div[@class='line-view__text-column']"):

            name = element.xpath(".//div[@class='line-view__body']/h2/a/text()").get()

            category_full = element.xpath(".//div[@class='line-view__body']/p/strong/text()").get()
            category = category_full.replace(' | ','')
            
            distance_full = element.xpath(".//div[@class='mb10']/span[@class='alpstein_tour_info']/abbr[@title='Distance']/text()").getall()[1]
            distance = distance_full.strip(' ').replace('\n', '').replace('\u00A0', '')

            duration_full = element.xpath(".//div[@class='mb10']/span[@class='alpstein_tour_info']/abbr[@title='Duration']/text()").getall()[1]
            duration = duration_full.strip(' ').replace('\n', '').replace('\u00A0', '')

            ascent_full = element.xpath(".//div[@class='mb10']/span[@class='alpstein_tour_info']/abbr[@title='Ascent']/text()").getall()[1]
            ascent = ascent_full.strip(' ').replace('\n', '').replace('\u00A0', '')

            link = element.xpath(".//div[@class='line-view__body']/h2/a/@href").get()

            link = 'https://www.zermatt.ch/' + str(link)

            yield scrapy.Request(
                url=response.urljoin(link),
                callback=self.parse_inner,
                cb_kwargs={
                            'name': name, 
                            'region': 'Valais', 
                            'category': category, 
                            'distance': distance, 
                            'duration': duration, 
                            'ascent': ascent, 
                            'link': link
                           }
            ) 

    def parse_inner(self, response, name, region, category, distance, duration, ascent, link):
        desc_main = response.xpath(".//div[@id='description']/p/text()").getall()
        desc_bullets = response.xpath(".//div[@id='description']/ul/li/text()").getall()

        description = desc_main + desc_bullets

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






# user similarity => determine a user's similarity to other users defined by some common aspects (e.g. type of products they buy),
#                    then make recommendation of new content/products based on judgements/requests of other users
# cold start problem => NEW USES: a new user arrives, need to gather some info about them (generic - gender, geo area, age etc). Give some free
#                       recommendations, and gather the interest data. Then make better recommendations, that will likely get the user
#                       to stay and pay
#                    => NEW DOC: how to start recommending products/content that nobody has ever seen? Use content-based filtering

# linear utility function => scoring all documents in a collection based on how relevant they are