from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

# wrapping the password

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://mplesson:{password}@cluster0.tfnr20a.mongodb.net/"

client = MongoClient(connection_string)

# Checking the list of databases

dbs =client.list_database_names()

print(dbs)

# accessing a database/ the collections inside the database

testcompass_db = client.testcompass
collections = testcompass_db.list_collection_names()

print(collections)

def insert_testcompass_doc():
    collection = testcompass_db.testcompass
    testcompass_document = {
        "name": "Vic",
        "type": "Test"
    }
    inserted_id = collection.insert_one(testcompass_document).inserted_id
    print(inserted_id)

insert_testcompass_doc()