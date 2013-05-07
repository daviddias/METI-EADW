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




while True:
  var = raw_input("Enter something: ")
  personalitiesFile = open("../entityExtraction/personalities.txt", 'rb')
  for line in personalitiesFile:
    personalitiesList = eval(line)
 
  if var in personalitiesList['listPersonalities']:
    print 'Personality: '+ var
    print 'Popularity: ' + "Positive: " + str(personalitiesPopularity(var)[1]) + " Negative :" + str(personalitiesPopularity(var)[2]) + " TotalOfNews: " + str(personalitiesPopularity(var)[0]) + " Total: " + str(personalitiesPopularity(var)[0])
  else:
    print '-------------------------'
    print 'News'
    aux1 = NewsSearch.search(var)
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

  aux = graphSearch.graphSearch(var)
  print "FIZ GRAPH Search"
  if len(aux) != 0:
    print '\n-------------------------'
    print 'Graph Search'
    print aux
    print '-------------------------\n\n'
 
  print '-------------------------'
  print 'News'
  aux1 = NewsSearch.search(var)
  for i in range(0, len(aux1)):
    cursor = news.find({"title" : aux1[i][0]})
    doc = next(cursor, None) #no pymongo nao existe hasNext()
      
    print "title: " + doc['title'] + " \n"
    print "description: " + doc['description'] + " \n"
    print "link: " + doc['link'] + " \n"
    print "##\n\n"
  print '-------------------------'
