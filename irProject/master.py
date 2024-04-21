import os
from indexing_module import *

'''
def run_spider():
    # Run the scrapy spider
    subprocess.run(['scrapy', 'crawl', 'content_spider'], check=True)
'''

# Your existing indexing code here (as a function or module import)
directory = 'C:/Users/prati/OneDrive/IITC/Spring24/IR/Project/irProject/output'
vectorizer, tfidf_matrix, file_paths = build_index(directory)
# Example search, you might want to skip or modify this
search('heartbreaking work', vectorizer, tfidf_matrix)