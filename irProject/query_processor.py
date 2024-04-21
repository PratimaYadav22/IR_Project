from flask import Flask, request, jsonify
from indexing_module import load_index, search  # Ensure correct import path

app = Flask(__name__)

# Load the index and document metadata outside of the Flask route
vectorizer, tfidf_matrix, document_metadata = load_index()

@app.route('/search', methods=['POST'])
def process_query():
    data = request.get_json(force=True)
    
    # Validate that the query is present and is a string
    if 'query' not in data or not isinstance(data['query'], str):
        return jsonify({"error": "Invalid or missing 'query' in JSON payload."}), 400
    
    query = data['query']
    similarities = search(query, vectorizer, tfidf_matrix)
    
    # Get the top K results and include document metadata
    top_k = 5  # Adjust the number of results as needed
    top_indices = similarities.argsort()[-top_k:][::-1]
    top_results = [
        {
            'document_name': document_metadata[idx]['filename'],
            'score': float(similarities[idx]),
            'url': document_metadata[idx]['url']
        }
        for idx in top_indices
    ]
    
    return jsonify(top_results)

if __name__ == '__main__':
    app.run()
