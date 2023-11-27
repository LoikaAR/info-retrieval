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

            yield {'name': name, 'region': 'Valais', 'category': category, 'distance': distance, 'duration': duration, 'ascent': ascent}