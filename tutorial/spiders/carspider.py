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
            cars=response.css('html body div#main-container section div.container div#featured-carousel.carousel.slide.pos-rel.lazy-slider.carousel-feature div.carousel-inner ul.list-unstyled.car-featured-used-home.car-slide-0.item.active.clearfix li.col-md-3')
            for car in cars:
                #  print(car)
                 each_car=car.css('div.cards div.cards-content h3.nomargin.truncate a::attr(href)').get()
                 each_car_page = response.urljoin(each_car)
                 yield scrapy.Request(url=each_car_page, callback=self.inner_parse)
            # next_page= response.css('html.no-js body#default.default div.container-fluid.page div.page_inner div.row div.col-sm-8.col-md-9 section div div ul.pager li.next a::attr(href)').get()     
            # if next_page:
            #     next_page = response.urljoin(next_page)
            #     yield scrapy.Request(url=next_page, callback=self.parse)     
            #      yield {
            #     'product':new
            #    }
 
    def inner_parse(self, response):
        car_region=response.css('#scroll_car_detail > li:nth-child(2)::text').get()
        car_price=response.css('#scrollToFixed > div.side-bar > div.well.price-well.pos-rel.mb20 > div.price-box > strong ::text').get()
        car_name=response.css('#scroll_car_info > h1::text').get()
        car=ProductItem()
        car['name']=car_name
        car['price']=car_price 
        car['region']=car_region
        yield car 

    
        # if each_product_page:
        #         each_product_page = response.urljoin(each_product_page)
        #         print(each_product_page)
        #         yield scrapy.Request(url=each_product_page, callback=self.inner_parse)

