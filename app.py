import os
from flask import Flask, render_template, request
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI) if MONGO_URI else None
db = client["survey_db"]
collection = db["users"]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
    data = {
        "age": request.form.get("age"),
        "gender": request.form.get("gender"),
        "income": request.form.get("income"),

        "utilities": request.form.get("utilities_amount"),
        "entertainment": request.form.get("entertainment_amount"),
        "school_fees": request.form.get("school_fees_amount"),
        "shopping": request.form.get("shopping_amount"),
        "healthcare": request.form.get("healthcare_amount")
    }

    collection.insert_one(data)

    return "Data submitted successfully!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
