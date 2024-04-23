# IR_Project

**Setup:**
1. **Scrapy**:
   pip install scrapy

2. **Spider**: 
scrapy startproject irProject 

3. **NLTK library:**
pip install nltk
import nltk
pip install nltk beautifulsoup4

4. **For tf-idf:**
pip install scikit-learn

5. **For flask application:**
pip install flask

**Steps for running the application:**
1. **Run below query to run the app on cli:**
python irProject\\\query_processor.py --cli --query 'will his wise advice give her the courage'

**Result output:**
![image](https://github.com/PratimaYadav22/IR_Project/assets/143662393/9b7d01d9-20dc-4b81-9441-364d510a11d8)

2. **Run below query to run the app on web:**
python irProject\\\query_processor.py

The project has also been rendered on html. 
For running the application on web page, simply run query_processor.py. It will direct to the localhost.
Below is the output for the same:
![image](https://github.com/PratimaYadav22/IR_Project/assets/143662393/1aa569f7-4d9b-487d-83a9-15f91d4cdac5)

![image](https://github.com/PratimaYadav22/IR_Project/assets/143662393/805835ca-fb33-4727-bcfa-4d2c27d6cda4)

Output:
![image](https://github.com/PratimaYadav22/IR_Project/assets/143662393/34af2d24-870a-4b50-8b7d-7cf816610921)


# **Abstract**
This project aimed to develop a robust system capable of efficiently crawling, indexing, and querying web documents without the use of a web interface for user interactions. Utilizing Python and several key libraries, the system automates the downloading of HTML content from specific domains and indexes this content for quick retrieval using advanced text processing techniques. Future developments will explore enhanced natural language processing features to improve the accuracy of query results and expand the system to handle a wider range of document types and languages.

# **Overview**
The proposed system consists of three interconnected modules:
1. Web Crawler (Scrapy-based): This module downloads web documents in HTML format, targeting specific allowed domains with maximum pages and depth limit to be crawled.
2. Indexer (Scikit-Learn-based): After crawling, documents are indexed using a TF-IDF vectorization for efficient retrieval.
3. Query Processor (Flask-based): A web service that allows users to submit queries and retrieve documents based on relevance.

**Web Crawler (Scrapy-based):**
Purpose and Functionality:
1. Objective: To autonomously navigate and download web documents from specified domains.
2. peration: The crawler starts from a seed URL and explores pages within the predefined constraints of maximum depth and number of pages to ensure focused and efficient data collection.
3. Custom Settings:
   **CLOSESPIDER_PAGECOUNT**: Limits the number of pages to crawl, preventing excessive bandwidth use and focusing the crawl on relevant content.
   **AUTOTHROTTLE_ENABLED:** Dynamically adjusts the speed of crawling based on the server response to maintain polite crawling behavior.
   **DEPTH_LIMIT:** Restricts the depth of navigation from the seed page, which helps in managing the scope of the crawl and avoiding unnecessary subdomains or external sites.
4. Technical Implementation:
   Implemented using Scrapy, a robust framework that provides built-in support for collecting data from websites using spider routines that simulate browsing from a user's perspective.
   Uses selectors and rules to intelligently navigate through hyperlinks and gather HTML content which is then saved for subsequent indexing.

**Indexer (Scikit-Learn-based):**
Purpose and Functionality:
1. Objective: To process the HTML documents downloaded by the crawler and construct an index using TF-IDF vectorization, facilitating efficient and relevant retrieval of documents.
2. Operation: Reads the raw HTML files, extracts text using BeautifulSoup, and then applies natural language processing techniques to tokenize and vectorize the content.
3. Technical Implementation:
   Utilizes the Scikit-Learn library, specifically its TfidfVectorizer, to transform text into a numerical format that represents the importance (weight) of words within the documents in relation to the corpus as a whole.
   The indexer creates a sparse matrix where each row corresponds to a document and each column represents a word from the corpus, with TF-IDF values as matrix entries.
   This matrix serves as the foundation for querying and similarity comparisons using cosine similarity metrics to determine document relevance.

**Query Processor (Flask-based):**
Purpose and Functionality:
1. Objective: To provide an interface for users to submit textual queries and retrieve documents ranked by relevance based on the indexed data.
2. Operation: Receives user queries, processes them against the indexed data, and returns a list of documents that best match the query criteria.
3. Technical Implementation:
   Built using Flask, a lightweight web framework suitable for setting up web applications quickly and with minimal code.
   Queries are received via HTTP POST requests, processed using the indexed TF-IDF matrix to find similarity scores, and results are returned in a structured format, often JSON, listing the documents that most closely match the user's search terms.
   The query processing is designed to handle errors and validate inputs to ensure that only meaningful queries are processed, optimizing the retrieval efficiency and user experience.

# **Design**
1. System Capabilities: The crawler is configured with auto-throttle to manage request rates, ensuring server-friendly interactions. The indexer supports cosine similarity for relevance scoring. The query processor handles JSON requests and supports error checking and response ranking.
2. Interactions: Each module interacts through well-defined interfaces, with data passing seamlessly from the crawler to the indexer, and indexed results being queried through the processor.
3. Integration: The system integrates data handling and processing capabilities to provide a user-friendly querying interface via a web service.

# **Architecture**
1. Software Components: The system uses Scrapy for crawling, BeautifulSoup for HTML parsing, Scikit-Learn for indexing, and Flask for the web interface.
2. Interfaces: Data flows through the system via files (HTML and pickle files) and through in-memory data structures (TF-IDF matrices).
3. Implementation: Each module is implemented as a separate Python script, encapsulating specific functionalities, which are then integrated to function as a unified service.

# **Operation**
1. Commands: System operations are primarily executed through Python scripts, with the Flask app serving the query interface.
2. Inputs: The system accepts URLs as input for crawling and free-text queries for document retrieval.
3. Installation: Setup requires Python with necessary dependencies installed via pip (e.g., pip install Flask scrapy scikit-learn nltk bs4).

# **Conclusion**
1. Results: The system successfully crawls, indexes, and queries documents with high efficiency and relevance.
2. Outputs: Outputs include HTML documents, indexed files, and query results in JSON format.
3. Caveats/Cautions: The system is currently limited to predefined domains and lacks full-scale error handling in real-world scenarios.

# **Data Sources**
1. Primary Source: Books to Scrape, used for initial testing and setup. https://books.toscrape.com/index.html
3. Access Information: All data is accessed programmatically via the crawler, with no manual download required.

# **Test Cases**
1. Framework: Testing is conducted using Python’s unittest framework for modular tests of each component.
2. Coverage: Tests cover functionalities such as crawling depth, page count compliance, indexing accuracy, and query response correctness.

# **Documentation**: 
Inline comments and README files explain usage and configuration.
# **Dependencies:** 
Open-source Python libraries (Scrapy, Scikit-Learn, Flask, etc.).

# **Bibliography**
1. "Scrapy 2.5 documentation," Scrapy. [Online]. Available: https://docs.scrapy.org/en/latest/
2. "Beautiful Soup Documentation," Crummy. [Online]. Available: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
3. "scikit-learn: machine learning in Python," Scikit-Learn. [Online]. Available: https://scikit-learn.org/stable/
4. "Flask Documentation," Pallets Projects. [Online]. Available: https://flask.palletsprojects.com/en/2.0.x/
