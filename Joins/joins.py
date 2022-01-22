"""
* @Author: Kanchan
* @Date: 21-01-2022
* @Last Modified by: Kanchan
* @Last Modified time: 21-01-2022 
* @Title: : Python program to create joins on MongoDB.
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
                    'country':'India',
                    'contact_no':'9876543210',
                    },
                    {
                    'e_id':'111',
                    'contact_no':'9876543210',
                    },
                    {
                    'e_id':'112',
                    'email':'vivek.yatri@gmail.com',
                    },
                     {
                    'e_id':'113',
                    'salary':'40000',
                    },
                    ]
            self.collection.insert_many(record)
            logger.info("Documents inserted sucessfully!")

        except Exception as e:
            logger.error(e)

    def join_data(self):
                """Description: This method will create join """
                try:
                    result=self.database.employee_information.aggregate(
                        [{'$lookup':{'from': "employee_new",'localField': "e_id",'foreignField': "country",'as':"country_name"}},
                        {'$match' : { 'e_id' : "110" } }])
                    for data in result:
                        print(data)
                        logger.info(data)
                    logger.info("Join created")
                    # localField specifies the key from the original/left collection – leftVal
                    # foreignField specifies the key from the right collection – rightVal
                except Exception as e:
                    logger.error(e)
#        {
#    $lookup:
#      {
#        from: <collection to join>,
#        localField: <field from the input documents>,
#        foreignField: <field from the documents of the "from" collection>,
#        as: <output array field>
#      }
#}

if __name__ == "__main__":

    db='employee'
    collect='employee_new'
    
    #create database and collection
    mongo_db=MongoPython(dBName=db,collectionName=collect)
    mongo_db.insert_to_db()
    mongo_db.join_data()
    # mongo_db.show_all()

