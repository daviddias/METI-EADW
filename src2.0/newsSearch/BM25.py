import whoosh
from whoosh.fields import *
from whoosh.scoring import *
from whoosh.qparser import *
from whoosh.query import *
from whoosh.index import open_dir

#BM25
#This code must be run inside the folder
ix = open_dir("../newsSearch/index_dir") #Index generated in previous lab


#Textual Similarity BM25
def bm25(queryTerms, rule):
    #   list=[]
    dict={} # dict com ID do doc e Similiaridade 
    with ix.searcher() as searcher:
        if rule == "OR":
            query = QueryParser("description", ix.schema, group=OrGroup).parse(u(queryTerms))
        elif rule == "AND":
            query = QueryParser("description", ix.schema, group=AndGroup).parse(u(queryTerms))
        else:
            print "Rule must be OR or AND"

        results = searcher.search(query, limit=100)
        #print results
        for i,r in enumerate(results):
            #list.append(r["id"])
            #print results[i], results.score(i)
            dict[r["title"]]= results.score(i)
        
        return dict  

       
