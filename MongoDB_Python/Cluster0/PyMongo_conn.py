from pymongo import MongoClient
import os

if __name__ == "__main__":
    print("Welcome to Pymongo")

    client = MongoClient("mongodb+srv://mplesson:Viccid11006622@cluster0.tfnr20a.mongodb.net")
    print(client)

    # This is to check the number of database:
    
    allDatabases =client.list_database_names()
    print(allDatabases)

    # This how to check sampole collection in a database:
    
    collection = client["test"]

    print(collection.list_collection_names())

    # To insert_one documents into a collection(table) and creating a new database:
    
    database = client["mplesson"]

    collection1 = database["studentinfo"]

    
    # dictionary = {"name": "Victor", 
    #           "age": 32, 
    #           "location": "Ibadan"
    #          }
    
    # collection1.insert_one(dictionary)

    # # To insert_many documents into a collection(table):
    
    # insertlist = [ {"name": "Dave", 
    #           "age": 22, 
    #           "location": "Osogbo"
    #          },
    #          {"name": "Gilbert", 
    #           "age": 38, 
    #           "location": "Zaria"
    #          },
    #          {"name": "Sam", 
    #           "age": 36, 
    #           "location": "Portharcourt"
    #          }
    # ]

    # collection1.insert_many(insertlist)


    # dictionary = {"_id": 1, "name": "Ashraf", 
    #           "age": 31, 
    #           "location": "Ilorin"
    #          }
    
    # collection1.insert_one(dictionary)

    # How to read_one document from collection

    read = collection1.find_one({"name":"Victor"})
    print(read)

    # How to read_many document from collection

    # allDocs = collection1.find({"name":"Victor"})

    # for item in allDocs:
    #     print(item)

    # To Update document in collection

    # prev = {"name":"Victor"}
    # nextt = {"$set": {"location":" Finland"}}

    # modf = collection1.update_one(prev, nextt)

 # How to update_many
    
    prev = {"name":"Victor"}

    nextt = {"$set": {"location": "Australia"}}

    modf = collection1.update_many(prev, nextt)


# How to delete_one
    
    doc = {"name":"Victor"}

    collection1.delete_one(doc)

# How to delete_many
    
    doc = {"name":"Victor"}

    collection1.delete_many(doc)

# How to delete_database / Drop the database_one:
    
    # database_name = 'your_database_name'

    # client.drop_database(database_name)


