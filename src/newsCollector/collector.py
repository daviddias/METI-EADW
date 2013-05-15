import pymongo
import feedparser
from pymongo import Connection
import contentCollector

#1. Collect the news 
#2. Check if they are on MongoDB Already (using upsert =)
#3. If not, add
def collect(feedURL):
	dbName = "eadw"
	collectionName = "news" 
	mongodbPort = 27017 #default
	mongoURL = 'localhost'

	mongodb = Connection('localhost', 27017)
	db = mongodb[dbName] 
	news = db[collectionName] 
	#how to do a query: item = news.find();
	feed = feedparser.parse(feedURL)
	for i in range(0,len(feed["items"])):	
		item = {}
		pTitle = feed.entries[i].title
		item["title"] = pTitle
		pLink = feed.entries[i].link
		item["link"] = pLink
		pDescription = feed.entries[i].description

		#Download a pristine version of the content
		item["description"] = contentCollector.articleContent(pLink)
		#item["description"] = pDescription
		#pCategory = feed.entries[i].category #Not all feeds has :(
		#item["category"] = pCategory
		pPubdate = feed.entries[i].published
		item["pubdate"] = pPubdate
		news.update({"title": pTitle }, item, True); # upsert like a BOSS!

#run
feedFilePath = "feeds.txt"
feedInputFile = open(feedFilePath, "rb")

for line in feedInputFile:
	if(line.startswith("#")):
		continue;
	collect(line)

feedInputFile.close()