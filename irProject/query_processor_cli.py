from flask import Flask, request, jsonify
from indexing_module import *  # Ensure this import is correct based on your project structure

app = Flask(__name__)

# Load the index outside of the route to load it into memory only once
# Load the index and document metadata outside of the Flask route
vectorizer, tfidf_matrix, document_metadata = load_index()

@app.route('/search', methods=['POST'])
def process_query():
    data = request.get_json()

    # Validate the input query
    if not data or 'query' not in data:
        return jsonify({'error': 'No query provided.'}), 400
    
    query = data['query']

    # Error checking for query content
    if not query or not isinstance(query, str):
        return jsonify({'error': 'Invalid query.'}), 400

    # Perform the search
    try:
        similarities = search(query, vectorizer, tfidf_matrix)
        # Get the top-K results; here we use K=5 as an example
        top_k = sorted(enumerate(similarities), key=lambda x: x[1], reverse=True)[:5]
        # Format the results: (index, score)
        results = [{
                    'document_id': document_metadata[idx]['doc_id'],
                    'document_name': document_metadata[idx]['filename'],
                    'score': float(score),
                    'url': document_metadata[idx]['url']} for idx, score in top_k]
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()