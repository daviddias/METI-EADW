import whoosh
from whoosh.fields import *
from whoosh.scoring import *
from whoosh.qparser import *
from whoosh.query import *
from whoosh.index import open_dir

#BM25
#This code must be run inside the folder
ix = open_dir("index_dir") #Index generated in previous lab


#Textual Similarity BM25
def bm25(queryTerms):
    #   list=[]
    dict={} # dict com ID do doc e Similiaridade 
    with ix.searcher() as searcher:
        query = QueryParser("description", ix.schema, group=OrGroup).parse(u(queryTerms))
        results = searcher.search(query, limit=100)
        #print results
        for i,r in enumerate(results):
            #list.append(r["id"])
            #print results[i], results.score(i)
            dict[r["title"]]= results.score(i)
        
        return dict  

       
