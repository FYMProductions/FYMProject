#! /usr/bin/python

from pymongo import *

client = MongoClient('localhost', 27017)

db = client['mydb']

collection = db['testData']

post = {"Client" : "William Grant",
		"Project" : "projectname",
		"tags" : ["testtag", "anothertag"]}

posts = db.testData
post_id = posts.insert(post)
print post_id

print db.collection_names()