import pymongo
from pymongo import Connection
from graphSearch import graphSearch
from graphSearch import personalitiesPopularity
from NewsSearch import search

dbName = "eadw"
collectionNameNews = "news"
mongodbPort = 27017 #default
mongoURL = 'localhost'

mongodb = Connection(mongoURL, 27017)
db = mongodb[dbName]
news = db[collectionNameNews]




while True:
  var = raw_input("Enter something: ")
  personalitiesFile = open ("personalities.txt", 'rb')
  for line in personalitiesFile:
    personalitiesList = eval(line)
 
  if var in personalitiesList['listPersonalities']:
    print 'Personality: '+ var
    print 'Popularity: ' + str(personalitiesPopularity(var))
  else:
    print '-------------------------'
    print 'News'
    aux1 = search(var)
    for i in range(0, len(aux1)):
      cursor = news.find({"title" : aux1[i][0]})
      doc = next(cursor, None) #no pymongo nao existe hasNext()
      
      print "title: " + doc['title'] + " \n"
      print "description: " + doc['description'] + " \n"
      print "link: " + doc['link'] + " \n"
      print "##\n\n"
      
      
      
    print '-------------------------' 
    continue
  aux = graphSearch(var)
  if len(aux) != 0:
    print '\n-------------------------'
    print 'Graph Search'
    print aux
    print '-------------------------\n\n'
 
  print '-------------------------'
  print 'News'
  aux1 = search(var)
  for i in range(0, len(aux1)):
    cursor = news.find({"title" : aux1[i][0]})
    doc = next(cursor, None) #no pymongo nao existe hasNext()
      
    print "title: " + doc['title'] + " \n"
    print "description: " + doc['description'] + " \n"
    print "link: " + doc['link'] + " \n"
    print "##\n\n"
  print '-------------------------'
