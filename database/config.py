from pymongo import MongoClient

client = MongoClient("mongodb+srv://anikrish2804:anirudh2804@cluster0.pewuuxt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.get_database('lap')
collection = db.get_collection('laptops')
owner_collection = db.get_collection('owners')
user_collection = db.get_collection('users')

shop_collection = db.get_collection("shops")