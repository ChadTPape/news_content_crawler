from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/search", methods=["GET"])
def search_articles():
    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "Keyword parameter is required for the search."})

    try:
        connection_string = "mongodb+srv://news_content_crawler:<news_content_crawler>@news-content-crawler-cl.r3rhmz1.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(connection_string)
        db = client["news_database"]
        collection = db["articles"]
        articles = list(collection.find({"$text": {"$search": keyword}}))
        client.close()
        return jsonify(articles)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
