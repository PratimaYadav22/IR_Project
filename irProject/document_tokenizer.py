import os
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize

def tokenize_file(filepath):
    """Tokenize the contents of a given file, excluding the URL (first line)."""
    with open(filepath, 'r', encoding='utf-8') as file:
        url = file.readline()  # Read and skip the URL
        content = file.read()  # Read the rest of the file

    # Use BeautifulSoup to extract clean text from HTML
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text(separator=' ')  # Use space as a separator to maintain readability
    tokens = word_tokenize(text)  # Tokenize the text
    
    return url.strip(), tokens

def tokenize_directory(directory):
    documents = []
    for index, filename in enumerate(os.listdir(directory)):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            url, tokens = tokenize_file(filepath)
            doc_id = index + 1  # Simple document ID, starting at 1
            documents.append({'doc_id': doc_id, 'url': url, 'tokens': tokens})
            print(f"Processed Document ID: {doc_id}, URL: {url}")  # Printing out document IDs and URLs
    return documents
    

# Example usage:
if __name__ == '__main__':
    directory_path = 'output'  # Adjust this path as necessary
    document_list = tokenize_directory(directory_path)
    print(len(document_list))  # Printing out to see the results
    print(document_list[112])
