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
      query = line[5:]
      print query	
    if(line[0:5] == "Title"):
      relevantDocs.append(line[5:])
      print relevantDocs	
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

print "Precision"
measures.Precision(result,query.values()) # adaptar o measures para papar titles em vez de ID 


print "Recall"



print "Fone"  	


  