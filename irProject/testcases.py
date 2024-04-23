import unittest
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher
from scrapy import signals

class TestIndexer(unittest.TestCase):
    def test_vectorization(self):
        print("testcase1 start............")
        """Test TF-IDF vectorization of documents."""
        from indexing_module import build_index, load_index
        build_index('test_data')  # Ensure 'test_data' directory has sample documents
        vectorizer, tfidf_matrix, metadata = load_index()
        # Assuming there's a document with known terms:
        feature_index = vectorizer.vocabulary_['courage']
        self.assertGreater(tfidf_matrix[0, feature_index], 0)  # Check if TF-IDF score is greater than zero for the term 'python'
        print("testcase1 end............")
    def test_cosine_similarity(self):
        print("testcase2 start ..................")
        """Test cosine similarity calculation accuracy."""
        from indexing_module import load_index, search
        vectorizer, tfidf_matrix, document_metadata = load_index()
        query = "courage"
        similarities = search(query, vectorizer, tfidf_matrix)
        self.assertIsNotNone(similarities)  # More detailed checks depending on expected results
        print("testcase2 end............")

import requests

class TestQueryProcessor(unittest.TestCase):
    def test_query_response(self):
        print("testcase3 start..............")
        """Test response to a valid query."""
        response = requests.post('http://127.0.0.1:5000/', data={'query': 'courage'})
        self.assertEqual(response.status_code, 500)
        self.assertIn('html', response.text)  # Assuming 'results' is part of the response HTML when results exist
        print("testcase3 end............")

    def test_invalid_query_handling(self):
        print("testcase4 start.............")
        """Test error handling for invalid queries."""
        response = requests.post('http://127.0.0.1:5000/', data={'query': ''})
        self.assertIn('error', response.text)  # Assuming 'error' is part of the response HTML when an error occurs
        print("testcase4 end............")

# Run the tests
if __name__ == '__main__':
    unittest.main()


