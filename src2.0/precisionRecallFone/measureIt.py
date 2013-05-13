#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../newsSearch")
sys.path.append("../superSearch")
import NewsSearch
import personalitySearch
import measures


#qrdd {query: [relevantDocs]}
def createQueryRelevantDocDict():
  filename = "relevantDocs.txt"
  fd = open (filename, "rb")

  qrdd = {}
  query = ""
  relevantDocs = []
  for line in fd:
    line = line.replace("\n","")
    if(line[0:3] == "#--"):
      continue
    if(line[0:5] == "Query"):
      query = line[7:]
      #print query	
    if(line[0:5] == "Title"):
      relevantDocs.append(line[7:])
      #print relevantDocs	
  qrdd[query] = relevantDocs
  return qrdd
 

qrdd = createQueryRelevantDocDict() 


query = qrdd.keys()[0]
names = personalitySearch.getPersonality(query)

if len(names) != 0:# Do And + OR Search
  stringNames = "".join(names)
  result = NewsSearch.mixSearchAndSort(NewsSearch.searchInsideWhoosh(stringNames, "AND"), NewsSearch.searchInsideWhoosh(query, "OR"))
else: # Do only OR Search
  result = NewsSearch.searchAndSort(query, "OR")

#print result

returnedDocuments = []
for tupple in result:
  returnedDocuments.append(tupple[0])

relevantDocuments = []
for rd in qrdd.values()[0]:
  relevantDocuments.append(rd)

print "RESULT"
print returnedDocuments

print "RELEVANT DOCS"
print relevantDocuments




print "Precision"
print measures.precision(returnedDocuments,relevantDocuments) # adaptar o measures para papar titles em vez de ID 


print "Recall"
print measures.recall(returnedDocuments,relevantDocuments)


print "Fone"  	
print measures.fone(result,relevantDocuments)


  