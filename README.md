# IR_Project

**Abstract**
The project aimed to develop a comprehensive text retrieval system that crawls, indexes, and queries web documents. The primary goal was to build a scalable and efficient platform capable of handling large volumes of data, with future objectives focusing on enhancing the robustness and accuracy of the search capabilities through advanced natural language processing techniques.

**Overview**
The proposed system consists of three interconnected modules:
Web Crawler (Scrapy-based): This module downloads web documents in HTML format, targeting specific allowed domains.
Indexer (Scikit-Learn-based): After crawling, documents are indexed using a TF-IDF vectorization for efficient retrieval.
Query Processor (Flask-based): A web service that allows users to submit queries and retrieve documents based on relevance.

**Design**
•	System Capabilities: The crawler is configured with auto-throttle to manage request rates, ensuring server-friendly interactions. The indexer supports cosine similarity for relevance scoring. The query processor handles JSON requests and supports error checking and response ranking.
•	Interactions: Each module interacts through well-defined interfaces, with data passing seamlessly from the crawler to the indexer, and indexed results being queried through the processor.
•	Integration: The system integrates data handling and processing capabilities to provide a user-friendly querying interface via a web service.

**Architecture**
•	Software Components: The system uses Scrapy for crawling, BeautifulSoup for HTML parsing, Scikit-Learn for indexing, and Flask for the web interface.
•	Interfaces: Data flows through the system via files (HTML and pickle files) and through in-memory data structures (TF-IDF matrices).
•	Implementation: Each module is implemented as a separate Python script, encapsulating specific functionalities, which are then integrated to function as a unified service.

**Operation**
•	Commands: System operations are primarily executed through Python scripts, with the Flask app serving the query interface.
•	Inputs: The system accepts URLs as input for crawling and free-text queries for document retrieval.
•	Installation: Setup requires Python with necessary dependencies installed via pip (e.g., pip install Flask scrapy scikit-learn nltk bs4).

**Conclusion**
•	Results: The system successfully crawls, indexes, and queries documents with high efficiency and relevance.
•	Outputs: Outputs include HTML documents, indexed files, and query results in JSON format.
•	Caveats/Cautions: The system is currently limited to predefined domains and lacks full-scale error handling in real-world scenarios.

**Data Sources**
•	Primary Source: Books to Scrape, used for initial testing and setup.
•	Access Information: All data is accessed programmatically via the crawler, with no manual download required.

**Test Cases**
•	Framework: Testing is conducted using Python’s unittest framework for modular tests of each component.
•	Coverage: Tests cover functionalities such as crawling depth, page count compliance, indexing accuracy, and query response correctness.

**Documentation**: Inline comments and README files explain usage and configuration.
Dependencies: Open-source Python libraries (Scrapy, Scikit-Learn, Flask, etc.).

**Bibliography**
"Scrapy 2.5 documentation," Scrapy. [Online]. Available: https://docs.scrapy.org/en/latest/
"Beautiful Soup Documentation," Crummy. [Online]. Available: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"scikit-learn: machine learning in Python," Scikit-Learn. [Online]. Available: https://scikit-learn.org/stable/
"Flask Documentation," Pallets Projects. [Online]. Available: https://flask.palletsprojects.com/en/2.0.x/
