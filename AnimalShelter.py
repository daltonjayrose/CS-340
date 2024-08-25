from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS, HOST, PORT, DB, COL):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'aacpass'
        #HOST = 'nv-desktop-services.apporto.com'
        #PORT = 30889
        #DB = 'AAC'
        #COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
# Create and insert a document based on the input dictionary data.
# Parameter data: Document data in dictionary format.
    def create(self, data):
        if data is not None:
            try:
                insert = self.database.animals.insert_one(data)  # data should be dictionary 
                if insert.inserted_id:
                    return True
                else:
                    return False     
            except:
                print("An exception occured when creating document.")
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
# Retrieve a list of documents, returning all documents if no query is specified in the optional parameters.
# Parameter query: MongoDB search query.
    def read(self, query=None):
        try:
            data = self.collection.find(query)
            document_list = []
            for document in data:
                document_list.append(document)
            return document_list
        except:
            print("An exception occured when reading documents.")
            
# Update one or more documents with parameters for search query and updated data.
# Parameter query: MongoDB search query.
# Parameter update: Updated fields in MongoDB syntax.
    def update(self, query, update):
        if query is not None and update is not None:
            try:
                updated = self.database.animals.update_many(query, {"$set": update})
                print(updated.modified_count, " documents updated.")
                return updated.modified_count
            except:
                print("An exception occured when updating documents.")
        else:
            raise Exception("No documents were updated due to invalid arguments.")
        
# Delete one or more documents with parameter for search query.
# Parameter query: MongoDB search query.
    def delete(self, query):
        if query is not None:
            try:
                deleted = self.database.animals.delete_many(query)
                print(deleted.deleted_count, " documents deleted.")
                return deleted.deleted_count
            except:
                print("An exception occured when deleting documents.")
        else:
            raise Exception("No documents were selected for deletion.")
            
    	    	

