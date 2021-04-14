
# pip3 install pymongo  => To Install pymongo
from pymongo import MongoClient

# Setup a connection
client = MongoClient(host="localhost", port=27017)

database = client['tempdb']
collection = database['users']

#insert the document 1M times
for i in range(1000000):
    collection.insert_one(
        {"StudentName":"Sumanshu",
        "RollNo": i,
        }
    )

cursor = collection.find().limit(4)  # it returns the cursor object

# print the records
for record in cursor:
    print(record)