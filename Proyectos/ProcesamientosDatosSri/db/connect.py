from pymongo import MongoClient

client = MongoClient()

def ConectarMongoDB():
    # database
    database = client.get_database('test')
    return database

# data_sri_table = database.contribuyente

# data_sri_table.insert_many({});