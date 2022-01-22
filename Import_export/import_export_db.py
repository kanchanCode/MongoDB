"""
* @Author: Kanchan
* @Date: 20-01-2022
* @Last Modified by: Kanchan
* @Last Modified time: 21-01-2022 
* @Title: : Python program to import and export data from/to MongoDB.
"""

from multiprocessing import connection
import pymongo 
from log_details import logger
import pandas as pd
import json

class ImportExport:

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

    def import_db(self,path=None):
        """Description: This method will import data to MongoDB from csv file """
        try:
            data_frame=pd.read_csv(path)
            data=data_frame.to_dict("records")
            self.collection.insert_many(data,ordered=False)
            logger.info("Data imported sucessfully!")

        except Exception as e:
            logger.error(e)

    def export_db(self):
        """Description: This method will export data to MongoDB from csv file """
        try:
            cursor=self.collection.find()
            data_frame=pd.DataFrame(list(cursor))
            data_frame.to_csv("C:\\Users\\hp\\Desktop\\MongoDB\\Import_export\\export_file.csv")
            logger.info("Data exported sucessfully!")

        except Exception as e:
            logger.error(e)
    
if __name__ == "__main__":

    db='import_export'
    collect='iris_data'

    #create database and collection
    mongo_db=ImportExport(dBName=db,collectionName=collect)
    mongo_db.import_db(path="C:\\Users\\hp\\Desktop\\MongoDB\\Import_export\\iris.csv")
    mongo_db.export_db()
