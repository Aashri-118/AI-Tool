<<<<<<< HEAD
from pymongo import MongoClient
def get_db_handle(db_name, host, port, username, password):

 client = MongoClient(host=host,
                      port=int(port),
                      username=username,
                      password=password
                     )
 db_handle = client['db_name']
 return db_handle, client


MONGO_URI = 'mongodb+srv://tpmongo:tp%4004@cluster0.4azcsav.mongodb.net/ibmproject'
client = MongoClient(MONGO_URI)
db = client['ibmproject']
=======
from pymongo import MongoClient
def get_db_handle(db_name, host, port, username, password):

 client = MongoClient(host=host,
                      port=int(port),
                      username=username,
                      password=password
                     )
 db_handle = client['db_name']
 return db_handle, client


MONGO_URI = 'mongodb+srv://tpmongo:tp%4004@cluster0.4azcsav.mongodb.net/ibmproject'
client = MongoClient(MONGO_URI)
db = client['ibmproject']
>>>>>>> 6621396420f49a39bc883d5c11ad0986228186eb
users_collection = db['users']