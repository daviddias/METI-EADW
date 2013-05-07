import pymongo
from pymongo import Connection
import graphSearch
import popularity
import sys
sys.path.append("../newsSearch")
import NewsSearch


dbName = "eadw"
collectionNameNews = "news"
mongodbPort = 27017 #default
mongoURL = 'localhost'

mongodb = Connection(mongoURL, 27017)
db = mongodb[dbName]
news = db[collectionNameNews]

#Fetch personalities List
personalitiesFile = open("../entityExtraction/personalities.txt", 'rb')
for line in personalitiesFile:
  personalitiesList = eval(line)
 

while True:
  readSearch = raw_input("Type your search: ")

  #1. 
  



  if readSearch in personalitiesList['listPersonalities']:
    print 'Personality: '+ readSearch
    print 'Popularity: ' + "Positive: " + str(popularity.personalityPopularity(readSearch)[1]) + " Negative: " + str(popularity.personalityPopularity(readSearch)[2]) + " Total of news: " + str(popularity.personalityPopularity(readSearch)[0]) + " Total: " + str(popularity.personalityPopularity(readSearch)[3])
  else:
    print '-------------------------'
    print 'News'
    aux1 = NewsSearch.search(readSearch, "OR")
    for i in range(0, len(aux1)):
      cursor = news.find({"title" : aux1[i][0]})
      doc = next(cursor, None) #no pymongo nao existe hasNext()
      
      print "title: " + doc['title'] + " \n"
      print "description: " + doc['description'] + " \n"
      print "link: " + doc['link'] + " \n"
      print "##\n\n"
    print '-------------------------' 
    continue
  



  print "CHEGUEI AQUI"

  aux = graphSearch.graphSearch(readSearch)
  print "FIZ GRAPH Search"
  if len(aux) != 0:
    print '\n-------------------------'
    print 'Graph Search'
    print aux
    print '-------------------------\n\n'
 
  print '-------------------------'
  

  print 'News'
  aux1 = NewsSearch.search(readSearch)
  for i in range(0, len(aux1)):
    cursor = news.find({"title" : aux1[i][0]})
    doc = next(cursor, None) #no pymongo nao existe hasNext()
      
    print "title: " + doc['title'] + " \n"
    print "description: " + doc['description'] + " \n"
    print "link: " + doc['link'] + " \n"
    print "##\n\n"
  print '-------------------------'
