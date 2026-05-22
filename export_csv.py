from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb+srv://joannadave63_db_user:Theesosa%40231@survey-cluster.ti0l1aa.mongodb.net/?appName=survey-cluster")
db = client["surveyDB"]
collection = db["users"]

data = list(collection.find())

print(data)

df = pd.DataFrame(data)

if "_id" in df.columns:
    df.drop(columns=["_id"], inplace=True)

df.to_csv("survey_data.csv", index=False)

print("CSV exported successfully!")
