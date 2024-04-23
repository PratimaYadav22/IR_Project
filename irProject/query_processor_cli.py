from flask import Flask, request, jsonify
from indexing_module import *  # Ensure this import is correct based on your project structure
import argparse
import json
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Load the index outside of the route to load it into memory only once
# Load the index and document metadata outside of the Flask route
vectorizer, tfidf_matrix, document_metadata = load_index()

'''
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

'''
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        json_str = request.form['json_input']
        try:
            print("1")
            data = json.loads(json_str)
            query = data.get('query', '')
            if query:
                print("2")
                similarities = search(query, vectorizer, tfidf_matrix)
                top_k = 5  # Adjust the number of results as needed
                top_indices = similarities.argsort()[-top_k:][::-1]
                print("3")
                results = [{
                    'document_id': document_metadata[idx]['doc_id'],
                    'document_name': document_metadata[idx]['filename'],
                    'score': float(similarities[idx]),
                    'url': document_metadata[idx]['url']
                } for idx in top_indices]  # Limiting results to top 5 for brevity
                print("4")
                return jsonify(results)
        except ValueError:
            return jsonify({"error": "Invalid JSON format"}), 400
    return render_template_string('''
        <form action="/" method="post">
            <label for="json_input">Enter JSON input:</label><br>
            <textarea id="json_input" name="json_input" rows="4" cols="50" placeholder='{"query": "example"}'></textarea><br>
            <input type="submit" value="Search">
        </form>
    ''')


parser = argparse.ArgumentParser(description='Search Documents via Web or CLI')
parser.add_argument('--cli', action='store_true', help='Enable CLI mode')
parser.add_argument('--query', type=str, help='Query string for CLI mode')
args = parser.parse_args()

if __name__ == '__main__':

        
    # Perform the search
        if args.cli:
            if args.query:
                similarities = search(args.query, vectorizer, tfidf_matrix)
        # Get the top-K results; here we use K=5 as an example
                top_k = sorted(enumerate(similarities), key=lambda x: x[1], reverse=True)[:5]
        # Format the results: (index, score)
                results = [{
                    'document_id': document_metadata[idx]['doc_id'],
                    'document_name': document_metadata[idx]['filename'],
                    'score': float(score),
                    'url': document_metadata[idx]['url']} for idx, score in top_k]
                print(json.dumps(results, indent=4))
        else:
            app.run(debug=True)
'''if __name__ == '__main__':
    
    app.run()'''