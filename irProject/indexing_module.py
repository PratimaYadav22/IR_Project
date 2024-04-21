import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to construct the URL from the filename
def construct_url_from_filename(filename):
    # Replace this with your own logic to construct the URL from a filename
    base_url = "https://books.toscrape.com/catalogue/"
    url = base_url + filename.replace('$', '/').replace('index.html.html', 'index.html').replace('output/', '')
    return url

def build_index(directory):
    corpus = []
    document_metadata = []
    
    for filename in os.listdir(directory):
        if filename.endswith('_tokens.txt'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                corpus.append(text)
            
            original_filename = filename.replace('_tokens.txt', '.html')
            url = construct_url_from_filename(original_filename)
            document_metadata.append({'filename': original_filename, 'url': url})
            
    if not corpus:
        print("No documents to process.")
        return

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    #print(len(tfidf_matrix))
    print(tfidf_matrix)
    with open('tfidf_vectorizer.pkl', 'wb') as vec_file:
        pickle.dump(vectorizer, vec_file)
    with open('tfidf_matrix.pkl', 'wb') as mat_file:
        pickle.dump(tfidf_matrix, mat_file)
    with open('document_metadata.pkl', 'wb') as meta_file:
        pickle.dump(document_metadata, meta_file)

    print("Indexing complete. Vectorizer, matrix, and metadata saved.")

    return vectorizer, tfidf_matrix, document_metadata

def load_index():
    with open('tfidf_vectorizer.pkl', 'rb') as vec_file:
        vectorizer = pickle.load(vec_file)
    with open('tfidf_matrix.pkl', 'rb') as mat_file:
        tfidf_matrix = pickle.load(mat_file)
    with open('document_metadata.pkl', 'rb') as meta_file:
        document_metadata = pickle.load(meta_file)
    
    return vectorizer, tfidf_matrix, document_metadata

def search(query, vectorizer, tfidf_matrix):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    return similarities

if __name__ == "__main__":
    directory = 'output'
    if not (os.path.exists('tfidf_vectorizer.pkl') and os.path.exists('tfidf_matrix.pkl') and os.path.exists('document_metadata.pkl')):
        build_index(directory)

    vectorizer, tfidf_matrix, document_metadata = load_index()
    query = "heartbreaking work"
    results = search(query, vectorizer, tfidf_matrix)
    # Add post-processing to format the search results if needed.
