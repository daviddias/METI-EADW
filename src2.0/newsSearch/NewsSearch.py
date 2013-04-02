import BM25
import TFIDF
import operator

def search(terms):
	
	queryResultBM25 = BM25.bm25(terms)
 	queryResultTFIDF = TFIDF.tfidf(terms)

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


	tuppleEvalValues = []
	for doc in evalValues:
			tuppleEvalValues.append((doc,evalValues[doc][0],evalValues[doc][1],evalValues[doc][2]))

	evalValuesSorted = sorted(tuppleEvalValues, key=operator.itemgetter(3), reverse=True)

	print evalValuesSorted


search("entrevista")

