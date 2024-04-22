from flask import Flask, request, render_template_string
from indexing_module import load_index, search  # Ensure correct import path

app = Flask(__name__)

# Load the index and document metadata outside of the Flask route
vectorizer, tfidf_matrix, document_metadata = load_index()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            similarities = search(query, vectorizer, tfidf_matrix)
            top_k = 5  # Adjust the number of results as needed
            top_indices = similarities.argsort()[-top_k:][::-1]
            results = [
                {
                    'document_id': document_metadata[idx]['doc_id'],
                    'document_name': document_metadata[idx]['filename'],
                    'score': float(similarities[idx]),
                    'url': document_metadata[idx]['url']
                }
                for idx in top_indices
            ]
            return render_template_string(HTML_TEMPLATE, results=results, query=query)
        return render_template_string(HTML_TEMPLATE, error="Please enter a search term.", results=None)
    return render_template_string(HTML_TEMPLATE, results=None)

HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document Search</title>
</head>
<body>
    <h1>Search for Documents</h1>
    <form method="post" action="{{ url_for('index') }}">
        <input type="text" name="query" placeholder="Enter search term..." value="{{ query }}">
        <button type="submit">Search</button>
    </form>
    {% if results %}
    <h2>Results for "{{ query }}":</h2>
    <ul>
        {% for result in results %}
        <li>
            <strong>ID:</strong> {{ result.document_id }},
            <strong>Name:</strong> {{ result.document_name }},
            <strong>URL:</strong> <a href="{{ result.url }}">{{ result.url }}</a>,
            <strong>Score:</strong> {{ "%.4f"|format(result.score) }}
        </li>
        {% endfor %}
    </ul>
    {% elif error %}
    <p>{{ error }}</p>
    {% endif %}
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
