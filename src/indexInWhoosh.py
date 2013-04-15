import feedparser
from whoosh.fields import *
from whoosh.index import *
from whoosh.qparser import *



dn = feedparser.parse("http://feeds.dn.pt/DN-Politica")
jn = feedparser.parse("http://feeds.jn.pt/JN-Politica")



#Title;Link;Description
schema = Schema(title=TEXT(stored=True), link=TEXT(stored=True), description=TEXT(stored=True), category=TEXT(stored=True), pubdate=TEXT(stored=True))

#1 for True ; 0 for False
hasIndex = 1

if (hasIndex == 1):
	ix = open_dir("index_dir")
else:
	ix = create_in("index_dir", schema)
	hasIndex = 1


writer = ix.writer()
for i in range(0,len(dn["items"])):	

	pTitle = dn.entries[i].title
	
	if (hasIndex == 1):
		with ix.searcher() as searcher:	
			query = QueryParser("title", schema=ix.schema, group=AndGroup).parse(pTitle)
			results = searcher.search(query)
			if len(results) > 0: # if 1 or more feeds with the title are found, it's because it was already added
				print "Already existed"
				continue
			
		
	pLink = dn.entries[i].link
	pDescription = dn.entries[i].description
	pCategory = dn.entries[i].category
	pPubdate = dn.entries[i].published
	writer.add_document(title = pTitle, link= pLink, description= pDescription, category=pCategory, pubdate=pPubdate)



#Fazer depois para o DN

# for i in range(0,len(jn["items"])):
# 	pTitle = dn.entries[i].title

# 	with ix.searcher() as searcher:
# 		query = QueryParser("title", schema=ix.schema)
# 		results = searcher.search(query)
# 		print "Result da Query"
# 		print results["title"]
# 		if results["title"] is None:
# 			continue


# 	pLink = dn.entries[i].link
# 	pDescription = dn.entries[i].description
# 	pCategory = dn.entries[i].category
# 	pPubdate = dn.entries[i].published
# 	writer.add_document(title = pTitle, link=pLink, description=pDescription, category=pCategory, pubdate=pPubdate)


writer.commit()

#Test if it's there

	



