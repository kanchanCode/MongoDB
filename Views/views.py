"""
* @Author: Kanchan
* @Date: 20-01-2022
* @Last Modified by: Kanchan
* @Last Modified time: 21-01-2022 
* @Title: : Python program to create views on MongoDB.
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

    def show_all(self):
            """Description: This method will display all the documents in the collection """
            try:
                
                result=self.collection.find()
                for data in result:
                    #print(data)
                    logger.info(data)
                logger.info("Data displayed successfully")

            except Exception as e:
                logger.error(e)
    
  

    def view_data(self):
        """Description: This method will create view on iris_data """
        try:
            self.database.createView("myView2","iris_data",[{'$project':{"_id":0,'sepal_width':1,'petal_width':1}}])
            logger.info("View created")

        except Exception as e:
            logger.error(e)

    def show_all(self):
            """Description: This method will display view data """
            try:
                
                result=self.database.myView.find()
                for data in result:
                    print(data)
                    logger.info(data)
                logger.info("Data displayed successfully")

            except Exception as e:
                logger.error(e)

if __name__ == "__main__":

    db='import_export'
    collect='iris_data'
    
    #create database and collection
    mongo_db=MongoPython(dBName=db,collectionName=collect)
    mongo_db.view_data()
    mongo_db.show_all()

