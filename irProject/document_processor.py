import os
from bs4 import BeautifulSoup
from nltk import word_tokenize

def process_and_tokenize_document(self, filepath, url):
        # Open the file and read all lines except the first
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()[1:]  # Skip the first line containing the URL
        text_content = ''.join(lines)
        tokens = word_tokenize(text_content)  # Tokenize the text content

        # Add to saved_files list
        #self.saved_files.append({'url': url, 'tokens': tokens})
        self.log(f'Tokens stored for {url}')

print('This is requested document: ')


def process_directory(directory):
    """
    Processes each HTML file in a directory.

    Args:
    directory (str): The directory containing HTML files to process.

    Returns:
    list: A list of dictionaries with URLs and tokenized content from all files.
    """
    documents = []
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            doc_data = process_and_tokenize_document(filepath)
            documents.append(doc_data)
    return documents


directory_path = 'output'
processed_data = process_directory(directory_path)
print(processed_data)
