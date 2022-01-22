"""
* @Author: Kanchan
* @Date: 20-01-2022
* @Last Modified by: Kanchan
* @Last Modified time: 21-01-2022 
* @Title: : Python program to perform CRUD operations to MongoDB.
"""

from multiprocessing import connection
import pymongo 
from log_details import logger

class MongoPython:

    def __init__(self, dBName=None , collectionName=None):
        """Description: This method will create the connection b/w python and Mongo_DB"""
        try:
            self.dbName=dBName
            self.collectionName=collectionName
            self.client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
            self.database=self.client[self.dbName]
            self.collection=self.database[self.collectionName]
            logger.info("Connection created successfully!")

        except Exception as e:
            logger.error(e)

    def insert_to_db(self):
        """Description: This method will insert the documents in the collection """
        try:
            record=[
            {
            'e_id':'110',
            'firstname':'vivek2',
            'lastname':'Yatri',
            'department':'Cloud computing2'
            },
            {
            'e_id':'111',
            'firstname':'Kanchan',
            'lastname':'jaiswal',
            'department':'Data engineering'
            },
            {
            'e_id':'112',
            'firstname':'Shilpi',
            'lastname':'jaiswal',
            'department':'Data governance'
            },
            {
            'e_id':'113',
            'firstname':'Priya',
            'lastname':'jaiswal',
            'department':'Financial Analyst'
            },
            {
            'e_id':'114',
            'firstname':'Abc',
            'lastname':'xyz',
            'department':'No'
            }
            ]
            self.collection.insert_many(record)
            logger.info("Documents inserted sucessfully!")

        except Exception as e:
            logger.error(e)
    
    def read_collect(self):
        """Description: This method will read data from the collection """
        try:
            
            result=self.collection.find()
            for data in result:
                #print(data)
                logger.info(data)
                logger.info("Data displayed successfully")
            #result=self.collection.find({'firstname':'vivek'}) # return the object
            #print(result)
            # result=self.collection.find_one()
            # {u'firstname':u'vivek2'}
            # print("READ",result)
            # logger.info("Data retrieved sucessfully!")
        except Exception as e:
            logger.error(e)


    def update_db(self):
        """Description: This method will update the document in the collection """
        try:
           #<method_name>(condition, update_or_replace_document, upsert=False, bypass_document_validation=False)
            """
            condition: A query that matches the document to replace.
            update_or_replace_document: The new document.
            upsert (optional): If True, perform an insert if no documents match the filter.
            bypass_document_validation: (optional) If True, allows the write to opt-out of document level validation. Default is False.
            """
            updating=self.collection.update_one(
            {'firstname':'Kanchan'},
            {"$set":{'firstname':'Kanchan2'}})
            print("UPDATE" ,updating)
            logger.info("Documents updated sucessfully!")

        except Exception as e:
            logger.error(e)
    
    def drop_collect(self):
        """Description: This method will drop the collection """
        try:
            #self.collection.drop()
            #logger.info("Collection dropped sucessfully!")

            self.collection.delete_one({'firstname':'Abc'})
            logger.info("Document deleted successfully")

        except Exception as e:
            logger.error(e)
   

if __name__ == "__main__":

    db='employee'
    collect='employee_information'

    #create database and collection
    mongo_db=MongoPython(dBName=db,collectionName=collect)

    # to insert collections
    mongo_db.insert_to_db()

    #to update 
    mongo_db.update_db()

    #to retrieve 
    results=mongo_db.read_collect()

    #to delete a document or to drop a collection
    mongo_db.drop_collect()

