import scrapy
class create_spider(scrapy.Spider):
     
    # Name of the spider or scrapy
    name = "spid"
 
    # Request function for getting response object from urls.
    def start_requests(self):
        urls = [
            'https://www.amazon.com/?&tag=googleglobalp-20&ref=pd_sl_7nnedyywlk_e&adgrpid=159651196451&hvpone=&hvptwo=&hvadid=675114638367&hvpos=&hvnetw=g&hvrand=11327950320931798126&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1011082&hvtargid=kwd-10573980&hydadcr=2246_13468515&gad_source=1',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        # Split the url 
        page = response.url.split("/")[-2]
         
        # Creating a file with html extension
        filename = f'spdr-{page}.html'
         
        # Open the file 
        with open(filename, 'wb') as f:
            # writing the content of the response into file
            f.write(response.body)
            print(response.body)
            # saving the file
        self.log(f'Saved file {filename}')         
         
      