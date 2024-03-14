# Web Scraping Project

This project uses Scrapy, a powerful open-source web crawling framework written in Python, to scrape data from websites. We have two spiders in this project: one for scraping book data and another for scraping car data.

## Dependencies

The dependencies for this project are listed in the `requirements.txt` file. You can install them using pip:



# Spiders

# Book Spider

The book spider scrapes data about books. It navigates through the website, goes into each book's detail page, and extracts information like the book's title, author, price, and description.

# Car Spider

The car spider scrapes data about cars. It navigates through the website, goes into each car's detail page, and extracts information like the car's make, model, year, and price.

# Proxy Requests

Both spiders use proxy requests to avoid getting blocked by the websites. The proxies are rotated for each request to further decrease the chance of getting blocked.

# Running the Spiders

You can run the spiders using the scrapy crawl command followed by the spider's name. For example, to run the book spider, you would use:
```bash
cd scrapy-demo-project
pip install -r requirements.txt
scrapy crawl carspider -o car.json
scrapy crawl bookspider -o book.json
