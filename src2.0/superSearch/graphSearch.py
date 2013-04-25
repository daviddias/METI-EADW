import pymongo
from pymongo import Connection

def graphSearch(nameForSearch):
 count = {}
 dbName = "eadw"
 collectionNameNews = "news"
 collectionNamePersonalities = "newsPersonality"
 mongodbPort = 27017 #default
 mongoURL = 'localhost'

 mongodb = Connection(mongoURL, 27017)
 db = mongodb[dbName]
 #news = db[collectionNameNews]
 pers = db[collectionNamePersonalities]

 personalitiesFile = open ("personalities.txt", 'rb')
 for line in personalitiesFile:
     personalitiesList = eval(line)
 
 if nameForSearch in personalitiesList['listPersonalities']:
  
  cursor = pers.find()
  doc = next(cursor, None) #no pymongo nao existe hasNext()
  while (doc != None): 
    if nameForSearch in doc["personalities"]:
       
       #print doc["personalites"]
       for name in doc["personalities"]:
           if name == nameForSearch:
               continue
           else:
               if name in count.keys():
                   count[name] = count[name] + 1
               else: count[name] = 1
    doc = next(cursor, None)
  return count           


def personalitiesPopularity(nameForSearch):
 count = {}
 result = 0
 dbName = "eadw"
 
 collectionNamePersonalitiesSentiment = "newsPersonalitySentiment"
 mongodbPort = 27017 #default
 mongoURL = 'localhost'

 mongodb = Connection(mongoURL, 27017)
 db = mongodb[dbName]
 #news = db[collectionNameNews]
 pers = db[collectionNamePersonalitiesSentiment]

 personalitiesFile = open ("personalities.txt", 'rb')
 for line in personalitiesFile:
     personalitiesList = eval(line)
 
 if nameForSearch in personalitiesList['listPersonalities']:
  
  cursor = pers.find()
  doc = next(cursor, None) #no pymongo nao existe hasNext()
  while (doc != None): 
    if nameForSearch in doc["personalities"]:
       
       #print doc["personalites"]
       for name in doc["personalities"]:
           if name == nameForSearch:
               
               result = result + doc["personalities"][name]
           else:
               continue
    doc = next(cursor, None)
 return result
#graphSearch('Vasco Cordeiro')
#personalitiesPopularity ('Carlos Silva')
