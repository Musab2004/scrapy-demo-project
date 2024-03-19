import scrapy
from ..items import ProductItem
from urllib.parse import urlencode
from bs4 import BeautifulSoup


class CarspiderSpider(scrapy.Spider):
    name = "carspider"
    start_urls = ["http://www.pakwheels.com/used-cars/?campaignid=17869391961&adgroupid=&keyword=&device=c&matchtype=&network=x&gclid=Cj0KCQjw-r-vBhC-ARIsAGgUO2ATI39iuy4KiaHlzkfYTSeQJSk6N27ffxeWQG2_b7GEHOimgyrR9HgaAviBEALw_wcB&utm_source=googleads&utm_medium=paid&utm_campaign=AutopartsPressurWashersSalesPerformanceMax&gad_source=1"]
    custom_settings = {
        'ITEM_PIPELINES': {
            'tutorial.pipelines.CarPipeline': 300,

        }
    }

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], self.parse)

    def parse(self, response):
        """
        Parse the response and extract information about each car.

        Args:
            response (scrapy.http.Response): The response object containing the HTML data.

        Yields:
            scrapy.Request: A request object for each car's page.

        """
        cars = response.css('html body div#main-container section div.container div#featured-carousel.carousel.slide.pos-rel.lazy-slider.carousel-feature div.carousel-inner ul.list-unstyled.car-featured-used-home.car-slide-0.item.active.clearfix li.col-md-3')
        for car in cars:
            each_car = car.css('div.cards div.cards-content h3.nomargin.truncate a::attr(href)').get()
            each_car_page = response.urljoin(each_car)
            yield scrapy.Request(url=each_car_page, callback=self.inner_parse)

 
    def inner_parse(self, response):
        """
        Parse the response to extract car details.

        Args:
            response (scrapy.http.Response): The response object containing the HTML data.

        Yields:
            ProductItem: A scrapy item representing a car with its name, price, and region.
        """
        car_region = response.css('#scroll_car_detail > li:nth-child(2)::text').get()
        car_price = response.css('#scrollToFixed > div.side-bar > div.well.price-well.pos-rel.mb20 > div.price-box > strong ::text').get()
        car_name = response.css('#scroll_car_info > h1::text').get()
        car = ProductItem()
        car['name'] = car_name
        car['price'] = car_price 
        car['region'] = car_region
        yield car


    


