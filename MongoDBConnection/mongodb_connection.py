# import pymongo
from pymongo import MongoClient

#Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

#Access the DB

db_name = client['AT-5StudentsData']
collection_name = db_name['Student_Storage']

collection_name.insert_one({"Name": "Krshna","Salary": None,"Language":None})

# all_data = collection_name.find()
print(dir(collection_name))
# for documents in all_data:
#     print(documents)
