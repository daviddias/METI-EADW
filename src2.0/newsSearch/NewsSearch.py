import BM25
import TFIDF
import operator


#Does the search in whoosh and returns and array of tupples with {doc: [BM25, TFIDF, SUM(BM25,TFIDF)]} sorted
def searchAndSort(terms, rule):
  return sort(searchInsideWhoosh(terms, rule))



#Sorts a search
def sort(search):
  tuppleEvalValues = []
  for doc in search:
    tuppleEvalValues.append((doc,search[doc][0],search[doc][1],search[doc][2]))

  evalValuesSorted = sorted(tuppleEvalValues, key=operator.itemgetter(3), reverse=True)

  #print evalValuesSorted 
  return evalValuesSorted


def mixSearchAndSort(search1, search2):
  return sort(mixSearch(search1,search2))

#mixes the results of two searches
def mixSearch(search1, search2):
  for key,value in search1.iteritems(): 	 
    if key in search2:
      search2[key][0] = search2[key][0] + value[0]
      search2[key][1] = search2[key][1] + value[1]
      search2[key][2] = search2[key][2] + value[2]
    else:
      search2[key] = value	
  return search2


#Search with OR or AND rule and returns an dict of {doc: [BM25, TFIDF, SUM(BM25,TFIDF)]}
def searchInsideWhoosh(terms, rule):
  queryResultBM25 = BM25.bm25(terms, rule)
  queryResultTFIDF = TFIDF.tfidf(terms, rule)

  # titulo : [BM25, TFIDF, SUM]
  evalValues = {}
  #templateList = [0,0] #BM25 ; TFIDF ; PageRank; Y

  for docBM25 in queryResultBM25:
    templateList = [queryResultBM25[docBM25],0,0]
    evalValues[docBM25] = templateList

  for docTFIDF in queryResultTFIDF:
    if docTFIDF in evalValues:
      evalValues[docTFIDF][1] = queryResultTFIDF[docTFIDF]
    else:
 	  templateList = [0,queryResultBM25[docBM25],0] 
 	  evalValues[docTFIDF] = templateList

  #Values Mix (Simple sum)
  for doc in evalValues:
    evalValues[doc][2] = evalValues[doc][0] + evalValues[doc][1]

  return evalValues






#print mixSearchAndSort(searchInsideWhoosh("renunciar ao mandato de deputado", "OR"), searchInsideWhoosh("onde consta ainda", "AND"))

#searchAndSort("entrevista", "OR")

