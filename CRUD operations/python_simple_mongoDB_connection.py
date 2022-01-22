"""
* @Author: Kanchan
* @Date: 20-01-2022
* @Last Modified by: Kanchan
* @Last Modified time: 20-01-2022 
* @Title: : Python program to create MongoDB connection and perform queries.
"""

import pymongo 

client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
#(protocol://ip_add:prt_no)

#name of the database
mydb=client['employee']

#collection
information=mydb.employee_information

#document insertion
record={
    'firstname':'vivek',
    'lastname':'Yatri',
    'department':'Cloud computing'
    }
    
information.insert_one(record)