"# news_content_crawler" 

news_spider.py = 
The provided code is a Python script that defines a web scraper using the Scrapy framework to extract news article data from two specific URLs. It then uses the Readability library to parse the web page and extract relevant information from the HTML. Finally, it stores the extracted data into a MongoDB database.

app.py = 
The provided code is a simple Flask web application that acts as a search API for articles stored in a MongoDB database. The application receives a search keyword as a query parameter, performs a text search for articles containing that keyword in the MongoDB database, and returns the matching articles in JSON format.
