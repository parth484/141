from flask import Flask, jsonify, request
import csv

all_articles = []

with open("articles.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []

app = Flask(__name__)

@app.route("/get-articless")
def get_article():
    return jsonify({
        "data": all_articles[0],
        "message": "success"
    })

@app.route("/liked-articles", methods=["POST"])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "message": "success"
    })

@app.route("/unliked-articles", methods=["POST"])
def unliked_article():
    article = all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "message": "success"
    })

if __name__ == "__main__":
    app.run()