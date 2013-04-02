import pymongo
from pymongo import Connection
from whoosh.fields import *
from whoosh.index import *
from whoosh.qparser import *


dbName = "eadw"
collectionName = "news" 
mongodbPort = 27017 #default
mongoURL = 'localhost'

mongodb = Connection('localhost', 27017)
db = mongodb[dbName] 
news = db[collectionName] 

	
#1 for True ; 0 for False
hasIndex = 1
if (hasIndex == 1):
	ix = open_dir("index_dir")
else:
	schema = Schema(title=TEXT(stored=True), link=TEXT(stored=True), description=TEXT(stored=True), pubdate=TEXT(stored=True))
	ix = create_in("index_dir", schema) 
	hasIndex = 1

writer = ix.writer()


cursor = news.find()
doc = next(cursor, None) #no pymongo não existe hasNext()
while(doc != None):
	with ix.searcher() as searcher:	#Check if it's already there
 		query = QueryParser("title", schema=ix.schema, group=AndGroup).parse(doc["title"])
 		results = searcher.search(query)
 		if len(results) > 0: # if 1 or more feeds with the title are found, it's because it was already added
 			print "Already existed"
 			continue
	writer.add_document(title = doc["title"], link= doc["link"], description= doc["description"], pubdate=doc["pubdate"])
	doc = next(cursor, None)

writer.commit()




