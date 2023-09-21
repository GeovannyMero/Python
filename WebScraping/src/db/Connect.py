from pymongo import MongoClient

client = MongoClient()

# DataBase 
database = client.get_database("test")


user_table = database.users


result = user_table.find()
print(result[0])