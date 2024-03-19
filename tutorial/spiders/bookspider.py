import scrapy
from ..items import ProductItem,BookItem
from urllib.parse import urlencode
from bs4 import BeautifulSoup


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    start_urls = ["https://books.toscrape.com/"]

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], self.parse)

    def parse(self, response):
        """
        Parse the response and extract information from the page.

        Args:
            response (scrapy.http.Response): The response object containing the page data.

        Yields:
            scrapy.Request: A request object for each book's page.
        """
        books = response.css('#default > div > div > div > div > section > div:nth-child(2) > ol > li')
        for book in books:
            each_book = book.css('article > h3 > a::attr(href)').get()
            each_book = response.urljoin(each_book)
            yield scrapy.Request(url=each_book, callback=self.inner_parse)

        next_page = response.css('#default > div > div > div > div > section > div:nth-child(2) > div > ul > li.next a::attr(href)').get()
        print(next_page)
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)

 
    def inner_parse(self, response):
        """
        Parse the response to extract book information.

        Args:
            response (scrapy.http.Response): The response object.

        Returns:
            A scrapy.Item object representing the book information.
        """
        book_description = response.css('#content_inner > article > p::text').get()
        book_price = response.css('#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color ::text').get()
        book_name = response.css('#content_inner > article > div.row > div.col-sm-6.product_main > h1::text').get()
        book = BookItem()
        book['name'] = book_name
        book['price'] = book_price 
        book['description'] = book_description
        print(book)
        yield book




