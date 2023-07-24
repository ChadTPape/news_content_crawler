import scrapy
from readability import Document
from pymongo import MongoClient

class NewsSpider(scrapy.Spider):
    name = "news_spider"
    start_urls = [
        "https://www.theguardian.com/australia-news/2023/jul/24/labor-to-give-casuals-new-rights-to-full-time-employment-in-move-to-improve-job-security",
        "https://www.bbc.com/news/uk-66282387",
    ]

    def parse(self, response):
        doc = Document(response.body)
        article = {
            "url": response.url,
            "headline": doc.title(),
            "author": response.css("div.author::text").get(),
            "text": doc.summary(),
        }
        self.save_to_mongodb(article)
        yield article

    def save_to_mongodb(self, article):
        client = MongoClient("mongodb+srv://news_content_crawler:<news_content_crawler>@news-content-crawler-cl.r3rhmz1.mongodb.net/?retryWrites=true&w=majority")
        db = client["news_database"]
        collection = db["articles"]
        collection.insert_one(article)
