import re
import time
import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options

# i spent a day with this bs

class HikeSpider(scrapy.Spider):

    name = "hikes_ch1"

    start_urls = ["https://www.zermatt.ch/en/Media/Planning-hikes-tours/"]

    def __init__(self):
        chrome_options = Options()

        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options= chrome_options)

    def parse(self, response): 
        self.driver.get(response.url)
        print("before:")
        print([m.start() for m in re.finditer('line-view__text-column', str(self.driver.page_source))])

        button = self.driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        button.click()
        self.driver.execute_script("window.scrollBy(0, 5000)","")

        time.sleep(2)

        self.driver.execute_script("window.scrollBy(0, 5000)","")
        
        time.sleep(2)

        self.driver.execute_script("window.scrollBy(0, 5000)","")
        
        time.sleep(2)

        see_more = self.driver.find_element(By.CSS_SELECTOR, 'div.ias_trigger a').get_attribute('href')
        print(see_more)

        print("after:")
        print([m.start() for m in re.finditer('line-view__text-column', str(self.driver.page_source))])
        for element in response.xpath("//div[@class='line-view__text-column']"):
            hike_name = element.xpath(".//div[@class='line-view__body']/h2/a/text()").get()
            
            # hike_name = element.xpath(".//div[@class='flex flex-col']/div[@class='title']/text()").get()

            # category = element.xpath(".//div[@class='category']/text()").get()	           
            # tags = hike.xpath(".//div[@class='tags']/a[@class='tag']/text()").getall()

            yield {'hike_name': hike_name}

        next_page = response.xpath("//li[@class='nav navbar-primary']/a/@href").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)