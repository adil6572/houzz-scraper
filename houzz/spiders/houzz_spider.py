import time
from bs4 import BeautifulSoup
import scrapy

from houzz.spiders.utils import extract_emails_from_url

class HouzzSpider(scrapy.Spider):
    name = "houzz_scraper"
    
    base_url="https://www.houzz.com"
    start_urls = ["https://www.houzz.com/professionals/interior-designer/carter-lake-ia-us-probr0-bo~t_11785~r_4850531"]

    custom_settings = {
        'FEEDS': {
            'output.csv': {
                'format': 'csv',
                'overwrite': True,  # Set to True to overwrite the file if it already exists
            },
        }
        }

    def __init__(self, *args, **kwargs):
        super(HouzzSpider, self).__init__(*args, **kwargs)
        self.start_time = time.time()

    def parse(self, response):
        
        target_elements = response.css('a.hz-pro-ctl::attr(href)').extract()
        for url in target_elements:
            yield response.follow(url, callback=self.parse_subpage)

        next_page=response.css("a.hz-pagination-link--next::attr(href)").get()

        if next_page:
          
            yield scrapy.Request(self.base_url+next_page, callback=self.parse)

    def parse_subpage(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        data = {"url": response.url}

        business_section = soup.find('section', id='business')
      
        for div in business_section.find_all('div'):
            h3 = div.find('h3')
            if h3:
                key = h3.get_text(strip=True)
                p = div.find('p')
                if p:
                    value = p.get_text()
                    data[key] = value

        if "Website" in data:
            found_emails = extract_emails_from_url(data["Website"])
            data["Emails"] = found_emails

        yield data



    def closed(self, reason):
        end_time = time.time()  # Record the end time
        total_time = end_time - self.start_time
        self.log(f"Total time taken for scraping: {total_time} seconds")
