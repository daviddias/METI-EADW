import pymongo
from pymongo import Connection
import graphSearch
import popularity
import sys
sys.path.append("../newsSearch")
import NewsSearch
import personalitySearch
import specialSearch


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
 

  print "\n\n"
  print "####################################################################"
  print "                           SUPER SEARCH                             "
  print "         The best search engine about your favorite subject         "
  print "                             POLITICS                               "
  print "####################################################################"
  print "\n\n"


while True:
  readSearch = raw_input("Type your search: ")
  if specialSearch.checkIfSpecial(readSearch):
    continue

  personalitySearch.printPersonality(readSearch)


  print "\n\n"
  print "********************************************************************"
  print "                            Fresh News                              "
  print "\n\n"


  #1. ver se tenho personalities
  #1.1 se sim fazer uma And Search com as personalities
  #2. Or Search
  #3. Mix both =)


  names = personalitySearch.getPersonality(readSearch)
  if len(names) != 0: # Do And + OR Search
    stringNames = "".join(names)
    result = NewsSearch.mixSearchAndSort(NewsSearch.searchInsideWhoosh(stringNames, "AND"), NewsSearch.searchInsideWhoosh(readSearch, "OR"))
  else: # Do only OR Search
    result = NewsSearch.searchAndSort(readSearch, "OR")


  for i in range(0, len(result)):
    if i == 11: #Chega 10 :)
      break;
    
    cursor = news.find({"title" : result[i][0]})
    doc = next(cursor, None) #no pymongo nao existe hasNext()
      
    print "Title: " + doc['title'] + " \n"
    print "Description: " + doc['description'] + " \n"
    print "Link: " + doc['link'] + " \n"
    print "-----------------------------------------\n\n"
  print "********************************************************************"
