import feedparser
from whoosh.fields import *
from whoosh.index import *
from whoosh.qparser import *

dn = feedparser.parse("http://feeds.dn.pt/DN-Politica")
jn = feedparser.parse("http://feeds.jn.pt/JN-Politica")


#Title;Link;Description
schema = Schema(title=TEXT(stored=True), link=TEXT, description=TEXT, category=TEXT, pubdate=TEXT)

ix = create_in("index_dir", schema)
writer = ix.writer()

for i in range(0,len(dn["items"])):	
	pTitle = dn.entries[i].title

	with ix.searcher() as searcher:
		query = QueryParser("title", schema=ix.schema)
		results = searcher.search(query)
		print "Result da Query"
		print results["title"]
		if results["title"] is None:
			continue


	pTitle = dn.entries[i].title
	pLink = dn.entries[i].link
	pDescription = dn.entries[i].description
	pCategory = dn.entries[i].category
	pPubdate = dn.entries[i].published
	writer.add_document(title = pTitle, link=pLink, description=pDescription, category=pCategory, pubdate=pPubdate)


for i in range(0,len(jn["items"])):
	pTitle = dn.entries[i].title

	with ix.searcher() as searcher:
		query = QueryParser("title", schema=ix.schema)
		results = searcher.search(query)
		print "Result da Query"
		print results["title"]
		if results["title"] is None:
			continue


	pLink = dn.entries[i].link
	pDescription = dn.entries[i].description
	pCategory = dn.entries[i].category
	pPubdate = dn.entries[i].published
	writer.add_document(title = pTitle, link=pLink, description=pDescription, category=pCategory, pubdate=pPubdate)


writer.commit()



