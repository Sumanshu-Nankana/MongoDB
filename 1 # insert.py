
# pip3 install pymongo  => To Install pymongo
from pymongo import MongoClient

# Setup a connection
client = MongoClient(host="localhost", port=27017)

database = client['tempdb']
collection = database['users']

document = {
        "name":"Mr.Shaurya",
        "eid":14,
        "location":"delhi"
        }

# insert the document
collection.insert_one(document)

cursor = collection.find().limit(4)  # it returns the cursor object

# print the records
for record in cursor:
    print(record)