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
First run the flask application (query_processor_cli.py)
When the application is running open powershell terminal and run below command one after the other:

1. **Define the query:**
$query = @{
  query = 'will his wise advice give her the courage'
}
2. **Convert the query to JSON:**
$json = $query | ConvertTo-Json

3. **Make the POST request:**
$response = Invoke-WebRequest -Uri 'http://127.0.0.1:5000/search' -Method Post -Body $json -ContentType 'application/json'

4. **Output the response content**
$response.Content

**Result output:**
![image](https://github.com/PratimaYadav22/IR_Project/assets/143662393/567accc8-ad53-4fc3-b39b-9fe09ac65f28)


The project has also been rendered on html. Below is the output for the same:
For running the application on web page, simply run query_processor_html.py. It will direct to the localhost.
![image](https://github.com/PratimaYadav22/IR_Project/assets/143662393/9b24b7d2-325a-464a-a027-b7325e3741d6)


# **Abstract**
This project aimed to develop a robust system capable of efficiently crawling, indexing, and querying web documents without the use of a web interface for user interactions. Utilizing Python and several key libraries, the system automates the downloading of HTML content from specific domains and indexes this content for quick retrieval using advanced text processing techniques. Future developments will explore enhanced natural language processing features to improve the accuracy of query results and expand the system to handle a wider range of document types and languages.

# **Overview**
The proposed system consists of three interconnected modules:
Web Crawler (Scrapy-based): This module downloads web documents in HTML format, targeting specific allowed domains with maximum pages and depth limit to be crawled.
Indexer (Scikit-Learn-based): After crawling, documents are indexed using a TF-IDF vectorization for efficient retrieval.
Query Processor (Flask-based): A web service that allows users to submit queries and retrieve documents based on relevance.

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
