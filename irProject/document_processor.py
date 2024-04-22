'''
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
'''
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def create_tfidf_index(documents):
    # Initialize a TfidfVectorizer
    vectorizer = TfidfVectorizer(stop_words='english', token_pattern=r'\b\w+\b')
    # Fit and transform the documents
    tfidf_matrix = vectorizer.fit_transform(documents)
    return tfidf_matrix, vectorizer

def save_index(tfidf_matrix, vectorizer, filename="tfidf_model.pkl"):
    # Save the vectorizer and matrix using pickle
    with open(filename, 'wb') as f:
        pickle.dump((vectorizer, tfidf_matrix), f)

def load_index(filename="tfidf_model.pkl"):
    # Load the vectorizer and matrix from a pickle file
    with open(filename, 'rb') as f:
        vectorizer, tfidf_matrix = pickle.load(f)
    return vectorizer, tfidf_matrix

def search_documents(query, vectorizer, tfidf_matrix):
    # Transform the query to the same TF-IDF vector space as the documents
    query_tfidf = vectorizer.transform([query])
    # Calculate cosine similarity between the query and all documents
    cosine_similarities = cosine_similarity(query_tfidf, tfidf_matrix).flatten()
    # Get the sorted document indices based on similarity scores
    sorted_doc_indices = np.argsort(-cosine_similarities)  # - for descending order
    return sorted_doc_indices, cosine_similarities

# Example Usage:
if __name__ == "_main_":
    documents = [
        "the martian has landed on the latin pop sensation ricky martin",
        "discover new scientific insights from the Mars rover expedition"
    ]

    # Create the TF-IDF index
    tfidf_matrix, vectorizer = create_tfidf_index(documents)

    # Save the TF-IDF index and vectorizer
    save_index(tfidf_matrix, vectorizer)

    # Optionally load the TF-IDF index and vectorizer
    vectorizer, tfidf_matrix = load_index()

    # Search for documents relevant to a query
    query = "mars expedition"
    sorted_doc_indices, cosine_similarities = search_documents(query, vectorizer, tfidf_matrix)

    # Print the results
    print("Document rankings by relevance:")
    for idx in sorted_doc_indices:
        print(f"Document {idx}, Score: {cosine_similarities[idx]}")