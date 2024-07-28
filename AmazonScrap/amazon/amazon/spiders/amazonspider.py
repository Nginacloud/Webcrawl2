import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scrapy.http import HtmlResponse
#import pandas as pd

class AmazonSpider(scrapy.Spider):
    name = "amazonspider"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://www.amazon.com/s?k=free+shipping"]

    def __init__(self, *args, **kwargs):
        super(AmazonSpider, self).__init__(*args, **kwargs)
        
        # Setup Chrome driver with Selenium
        chrome_driver_path = 'C:/Users/USER/OneDrive/Desktop/AmazonScrap/chromedriver.exe'
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        
        chrome_options = Options()
        chrome_options.add_argument(f'user-agent={user_agent}')
        self.driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
    
    def start_requests(self):
        for url in self.start_urls:
            self.driver.get(url)
            #wait for products to load
            wait = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.s-result-item.s-asin')))
            html = self.driver.page_source
            yield scrapy.Request(url, callback=self.parse, meta={'html': html})
    
    def parse(self, response):
        # Convert Selenium HTML to Scrapy Response object
        html = response.meta['html']
        scrapy_response = HtmlResponse(url=response.url, body=html, encoding='utf-8')

        # Extract data with Scrapy
        products = scrapy_response.css('div.s-result-item.s-asin')
        
        for product in products:
            asin = product.css('::attr(data-asin)').get()
            index = product.css('::attr(data-index)').get()
            
            if asin and index:
                name = product.css('a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal::attr(href)').get()
                price = product.css('span.a-price-whole::text').get()
                pricefraction = product.css('span.a-price-fraction::text').get()

                yield {
                    'Asin': asin,
                    'Index': index,
                    'Name': name,
                    'Price': price,
                    'Pricefraction': pricefraction
                }
    
    def close(self, reason):
        self.driver.quit()