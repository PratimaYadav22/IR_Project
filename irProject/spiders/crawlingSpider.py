import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from ..document_tokenizer import tokenize_directory

class ContentSpider(scrapy.Spider):
    name = 'content_spider'
    
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 100,  # Set your desired max pages
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 5,
        'AUTOTHROTTLE_MAX_DELAY': 60,
        'DEPTH_LIMIT': 3,  # Set your desired max depth
    }
    start_urls = ["https://books.toscrape.com/index.html"]

    allowed_domains = ['books.toscrape.com']

    excluded_urls = ['https://www.1mg.com/editorial-policy-processes/']
    saved_files = []
    
    def spider_closed(self, spider):
        # This method is called when the spider closes
        self.log('Spider closed: %s' % spider.name)
        document_list = tokenize_directory(self.output_dir)
        self.log('Document tokenization completed. Documents: {}'.format(len(document_list)))
    
    def parse(self, response):
        # Ensure the output directory exists
        output_dir = 'output'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Construct a filename based on URL components
        parts = response.url.strip('/').split('/')
        filename_safe_title = '$'.join(parts[-2:]) if len(parts) >= 2 else 'index'
        filename = f'{output_dir}/{filename_safe_title}.html'

        # Using BeautifulSoup to extract and clean text
        '''soup = BeautifulSoup(response.body, 'html.parser')
        text = ' '.join(soup.get_text().split())'''

        soup = BeautifulSoup(response.body, 'html.parser')
        text = '\n\n'.join([p.get_text(' ', strip=True) for p in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])])


        # Save the response with URL in the first line, followed by the cleaned text content
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.url + "\n" + text)
        
        self.log(f'Saved file with URL and cleaned text {filename}')

        # Add the path of the saved file to the list
        self.saved_files.append(filename)


        # Follow links to next pages within depth limit
        for next_page in response.css('a::attr(href)'):
                yield response.follow(next_page, self.parse)


 