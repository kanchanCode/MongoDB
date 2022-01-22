"""
* @Author: Kanchan
* @Date: 20-01-2022
* @Last Modified by: Kanchan
* @Last Modified time: 21-01-2022 
* @Title: : Python program to perform aggregation functions to MongoDB.
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
    
  

    def count_data(self):
        """Description: This method will display all the documents in the collection """
        try:
            
            result=self.collection.aggregate([{'$group':{"_id":'$by_user',"sepal_length_count":{'$sum':1}}}])
            for data in result:
                print(data)
                logger.info(data)

            logger.info("Count displayed")

        except Exception as e:
            logger.error(e)

    def average_data(self):
        """Description: This method will display average of petal length in the collection """
        try:
            
            result=self.collection.aggregate([{'$group':{"_id":'$by_user',"avg_petal_length":{'$avg':'$petal_length'}}}])
            for data in result:
                print(data)
                logger.info(data)

            logger.info("Average displayed")

        except Exception as e:
            logger.error(e)

    def sum_data(self):
        """Description: This method will display sum of sepal length in the collection """
        try:
            
            result=self.collection.aggregate([{'$group':{"_id":'$by_user',"sepal_length_sum":{'$sum':'$sepal_length'}}}])
            for data in result:
                print(data)
                logger.info(data)

            logger.info("Sum displayed")

        except Exception as e:
            logger.error(e)

    def min_data(self):
        """Description: This method will display minimum sepal length in the collection """
        try:
            
            result=self.collection.aggregate([{'$group':{"_id":'$by_user',"min_sepal_length":{'$min':'$sepal_length'}}}])
            for data in result:
                print(data)
                logger.info(data)

            logger.info("Minimum displayed")

        except Exception as e:
            logger.error(e)
    
    def max_data(self):
        """Description: This method will display maximum sepal length in the collection """
        try:
            
            result=self.collection.aggregate([{'$group':{"_id":'$by_user',"max_sepal_length":{'$max':'$sepal_length'}}}])
            for data in result:
                print(data)
                logger.info(data)

            logger.info("Maximum displayed")

        except Exception as e:
            logger.error(e)
    
    

    

if __name__ == "__main__":

    db='import_export'
    collect='iris_data'
    
    #create database and collection
    mongo_db=MongoPython(dBName=db,collectionName=collect)

    # to display documents from collections
    mongo_db.show_all()

    mongo_db.count_data()

    mongo_db.average_data()

    mongo_db.sum_data()

    mongo_db.min_data()

    mongo_db.max_data()

