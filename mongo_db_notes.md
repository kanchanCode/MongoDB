# DBMS
Collection of related information -> Database
Database Management Systems (DBMS) are software systems used to store, retrieve, and run queries on data. 
A DBMS serves as an interface between an end-user and a database, allowing users to create, read, update, and delete data in the database.

# Types of Database
1. Relational Database(SQL) - organize data into one or more tables
2. Non-Relational(noSQL)- traditional table key-value stores, documents(like JSON),graphs,flexible tables 
noSQL DBMS- mongoDB,dynamoDB,firebase etc

# noSQL Database
NoSQL Database is a non-relational Data Management System, that does not require a fixed schema.
NoSQL is used for Big data and real-time web apps.

* Why noSQL?
The system response time becomes slow when you use RDBMS for massive volumes of data.
The alternative for this issue is to distribute database load on multiple hosts whenever the load increases. This method is known as “scaling out.”(Horizontal scaling)

* Features of noSQL:
1. Non-relational - No complex features like query languages, query planners,referential integrity joins, ACID
2. Schema-free - Offers heterogeneous structures of data in the same domain
3. Simple API - Offers easy to use interfaces for storage and querying data provided
4. Distributed - Multiple NoSQL databases can be executed in a distributed fashion
Shared Nothing Architecture. This enables less coordination and higher distribution.

# Types of NoSQL Databases:

1. Key-value Pair Based : 
Key-value pair storage databases store data as a hash table where each key is unique, and the value can be a JSON, BLOB(Binary Large Objects), string, etc.
This kind of NoSQL database is used as a collection, dictionaries, associative arrays, etc. Key value stores help the developer to store schema-less data. 
They work best for shopping cart contents.

Redis, Dynamo, Riak are some NoSQL examples of key-value store DataBases

2. Column-oriented Graph : 

Column-oriented databases work on columns.Every column is treated separately. Values of single column databases are stored contiguously.


Column-based NoSQL databases are widely used to manage data warehouses, business intelligence, CRM, Library card catalogs,

HBase, Cassandra, HBase, Hypertable are NoSQL query examples of column based database.

3. Graphs based

A graph type database stores entities as well the relations amongst those entities. 
The entity is stored as a node with the relationship as edges. 
An edge gives a relationship between nodes. Every node and edge has a unique identifier.

Graph base database mostly used for social networks, logistics, spatial data.

Neo4J, Infinite Graph, OrientDB, FlockDB are some popular graph-based databases.

4. Document-oriented
Document-Oriented NoSQL DB stores and retrieves data as a key value pair but the value part is stored as a document. 
The document is stored in JSON or XML formats.

The document type is mostly used for CMS systems, blogging platforms, real-time analytics & e-commerce applications. 

Amazon SimpleDB, CouchDB, MongoDB, Riak, Lotus Notes, MongoDB, are popular Document originated DBMS systems.

# MongoDB is a document-oriented noSQL database

# MongoDB
1. MongoDB is a document designed for ease of development and scaling.
2. It is intuitive and easy to use NoSQL Database.

# MongoDB and mongod
* 'mongo' is the command-line shell that connects to a specific instance of mongod(to issue command)
* 'mongod' is the 'Mongo Daemon' it's basically the host process for the database (to take action on issued command)

# MongoDB atlas
* MongoDB Atlas is a cloud service by MongoDB.
* It is the worldwide cloud database service for modern applications that give best-in-class automation and proven practices guarantee availability, scalability, and compliance with the foremost demanding data security and privacy standards.

# MongoDb and MySQL
* In MySQL -> We have tables, rows , column ,schema
*  In MongoDB -> We have collection(like tables in BSON format), documents(like rows ), fields

Table -> Collection
Row   -> JSON Document
Index -> Index
Join  -> Embedding & Linking
Partition -> Shard

# D/b JSON and BSON
* JSON(JavaScript Object Notation) shows up in many different cases: APIs,Configuration files,Log messages and Database storage. 
but it only supports a limited number of basic data types and it's a text-based format, and text parsing is very slow

* BSON(Binary JSON),a binary representation to store data in JSON format,with specific extensions for broader applications, and optimized for data storage and retrieval.
* Binary structure encodes type and length information, which allows it to be parsed much more quickly.
* BSON has been extended to add some optional non-JSON-native data types, like dates and binary data,
* It also allows for comparisons and calculations to happen directly on data in ways that simplify consuming application code.
Anything you can represent in JSON can be natively stored in MongoDB, and retrieved just as easily in JSON

           JSON                                          BSON    
Type	   Standard file format	                         Binary file format
Speed	   Comparatively less fast	                     Faster
Space	   Consumes comparatively less space.	           More space is consumed.
Usage	   Transmission of data.	                       Storage of data.
Encoding   UTF-8 String                                Binary 
Data 
Support     String, Boolean, Number, Array             String, Boolean, Number (Integer, Float, Long, Decimal128)
                                                      Array, Date, Raw Binary
Readability Human and Machine                          Machine Only

# Data models in MongoDB

MongoDB provides two types of data models:— 
Embedded data model and Normalized data model. 
Based on the requirement, we can use either of the models while preparing our document.

1. Embedded data model :
In this model, all the related data are embedded in a single document, it is also known as de-normalized data model.

example -
{
	_id: ,
	Emp_ID: "10025AE336"
	Personal_details:{
		First_Name: "Radhika",
		Last_Name: "Sharma",
		Date_Of_Birth: "1995-09-26"
	},
	Contact: {
		e-mail: "radhika_sharma.123@gmail.com",
		phone: "9848022338"
	},
	Address: {
		city: "Hyderabad",
		Area: "Madapur",
		State: "Telangana"
	}
}

2. Normalized data model :
In this model, sub documents referes the original document using references.

example - 

Employee:
{
	_id: <ObjectId101>,
	Emp_ID: "10025AE336"
}

Personal_details:
{
	_id: <ObjectId102>,
	em1pDocID: " ObjectId10",
	First_Name: "Radhika",
	Last_Name: "Sharma",
	Date_Of_Birth: "1995-09-26"
}

Contact:
{
	_id: <ObjectId103>,
	empDocID: " ObjectId101",
	e-mail: "radhika_sharma.123@gmail.com",
	phone: "9848022338"
}

Address:
{
	_id: <ObjectId104>,
	empDocID: " ObjectId101",
	city: "Hyderabad",
	Area: "Madapur",
	State: "Telangana"
}


# Keys 

Primary Key:
In MongoDB, _id field as the primary key for the collection so that each document can be uniquely identified in the collection. The _id field contains a unique ObjectID value. 


# Relationships in MongoDB

1. Embedded Relationships
If it will be embedded within the documents, queries will run faster than if we spread them on multiple documents. This will provide acceleration in the performance, especially with a large amount of data.

a. One-to-one relationship:
It is where the parent document has one child, and the child has one parent.

eg
db.singers.insert(
  {
     _id : 2,
     artistname : "XYZ",
     address : {
                  street : "Apollo Street",
                  city : "Mumbai",
                  state : "Maharashtra",
                  country : "India"
                }
    }
)

b. One to Many Relationships in MongoDB
It is a MongoDB relationship, in which a parent can have many child documents in it. But child document can have only one parent.

eg
db.singers.insert(
  {
     _id : 3,
     artistname : "XYZ",
     albums : [
             {
               album : "DEF",
               year : 2000,
               genre : "Blues"
               }, 
               {
                    album : "ABC",
                    year : 2013,
                    genre : "Classical Music"
               }
          ]
     }
)


2. Documented Reference Relationships:
Rather than implanting a child document into the parent document, we separate the child and parent document respectively. 
When data needs to be repeated across many documents, it is helpful to have them in their own separate document.

a. Parent Document


db.singers.insert(
  {
    _id : 4,
    artistname : "UVW"
   }
)


b. Child Documents:


db.instruments.insert(
{
    _id : 9,
    singer_name : "GHI",
    instrument : [ "Accordion", "Jaw Harps", "Keyboards" ],
    artist_id : 4
  }
)

db.instruments.insert(
  {
    _id : 10,
    name : "ABC",
    instrument : [ "Banjo", "Cello" ],
    artist_id : 4
  }
)

db.instruments.insert(
 {
    _id : 11,
    name : "LMN",
    instrument : "Membranophones",
    artist_id : 4
  }
)


c. Querying the MongoDB Relationships

After inserting these documents now we will use $lookup to perform left outer join on the two collections.
Here, we will use aggregate() method and $match, so that we get the details of artist, and we get the child and parent documents together.

db.singers.aggregate([
  {
     $lookup:
       {
         from: "instruments",
         localField: "_id",
         foreignField: "artist_id",
         as: "band_members"
       }
        },
        { $match : { artistname : "UVW" } }
]).pretty()

Output:
{
“_id” : 4,
“artistname” : “UVW”,
“band_members” : [
{
“_id” : 9,
“singer_name” : “GHI”,
“instrument” : [ “Accordion”, “Jaw Harps”, “Keyboards” ],
“artist_id” : 4
},
{
“_id” : 10,
name : “ABC”,
instrument : [ “Banjo”, “Cello” ],
artist_id : 4
},
{
“_id” : 11,
“name” : “LMN”,
“instrument” : “Membranophones”,
“artist_id” : 4
}
]
}

We can see that 2 fields are from singers collection and rest are from instruments collection.

# Advantages of MongoDB
MongoDB provides Dynamic and flexible schema when compared to the rigid, tabular data models used by relational databases.

Fields can vary from document to document within a single collection (analogous to table in a relational database). Documents make modeling diverse record attributes easy for developers, elegantly handling data of any structure.

If a new field needs to be added to a document, it can be created without affecting all other documents in the collection, without updating central system

Features:Ad-hoc Queries,Schema-Less Database,Document-Oriented,Indexing,Replication,Aggregation,GridFS,Sharding,High Performance

# Install MongoDB
mongoDB community ->download ->add path(for ease) 
* MongoDB Compass (GUI) to create and use database 


# Commands in MongoDB

Database commands
1. show dbs; -> view all databases
2. use db_name-> to create a new or switch to database
3. db -> to check the current db 
4. db.dropDatabase() -> to Delete database

Collection commands
1. show collections -> to show all the collections
2. db.createCollection('comments') -> to create a collection
3. db.collection_name.drop() -> to delete collection

Rows commands
1. db.collection_name.find() -> to show all rows in collection
   db.collection_name.find().pretty() -> prettified output
2. db.collection_name.insert({
    'name':'Kanchan',
    'lang':'Python',
    'members':5
})                                 -> to insert Rows

3. db.collection_name.insertMany
([{
    'name':'Priya',
    'lang':'Tally',
    'members':3
},
{
    'name':'Shilpi',
    'lang':'SQL',
    'members':7
},
{
    'name':'Hritik',
    'lang':'None',
    'members':4
}])                                 -> to insert many rows

4. db.collection_name.insert({
    'name':'Kanchan',
    'lang':'Python',
    'members':5,
    'date':new Date()
})                                 ->to add field in a collection     

5. db.collection_name.find({lang:"Python"})  -> to search

6. db.collection_name.find().pretty().limit(2)  -> limit output

7. db.collection_name.find().count() -> to count

8. db.collection_name.find().sort({members:-1}).pretty()  -> to sort asc
   db.collection_name.find().sort({members:-1}).pretty()  -> to sort desc

9. db.collection_name.findOne({lang:"Python"}) -> to find the first row matching in the output

10. db.collection_name.update({name:'Kanchan'},
{
name:"Kanchan",
lang:"Python",
members:52,
})                                             -> to update the collection_name                        

11. db.collection_name.update({name:'Kanchan25'},
{
name:"Kanchan",
lang:"Python",
members:78,
}, {upsert:true})                               -> to make upsert =true

12. Update operators inc, min, max, mul, currentDate, rename, set, setOnInsert, unset etc
 
{
name:"Kanchan",
lang:"Python",
members:78,
}, {upsert:true}) 

13. db.collection_name.update({name: 'Hritik'},
{$inc:{
    members: 2
}})                                                  -> Increment operator use

14. db.collection_name.update({name: 'Hritik'},
{$rename:{
    members: 'member_since'
}})                                                  -> Rename operator use
 
15. db.collection_name.remove({name: 'Kanchan'})              -> to delete a row

16. db.collection_name.find({members: {$lt: 90}})
    db.collection_name.find({members: {$lte: 90}})
    db.collection_name.find({members: {$gt: 90}})
    db.collection_name.find({members: {$gte: 90}})    -> Less than/Greater than/ Less than or Eq/Greater than or Eq

17. create View

    db.createView("<viewName>","<source>",[<pipeline>],{"collation" : { <collation> }})
    
    db.createView("firstView","demo113", [ { $project: { "Name": "$Details.Name", Subject: 1 } } ] )

    Display fields from a view with the help of find() method −
    db.firstView.find();