import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class AmazonspiderSpider(scrapy.Spider):
    name = "amazonspiderspider"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com/s?k=free+shipping"]

    def parse(self, response):
        products = response.css('div.s-result-item.s-asin')

        for product in products:
            asin = product.css('::attr(data-asin)').get()
            index = product.css('::attr(data-index)').get()
            
            if asin and index:
                name = product.css('a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal::attr(href)').get()
                price = product.css('span.a-price-whole::text').get()
                pricefraction = product.css('span.a-price-fraction::text').get()

                yield{
                    'Asin': asin,
                    'Index': index,
                    'Name': name,
                    'Price': price,
                    'Pricefraction': pricefraction
                }