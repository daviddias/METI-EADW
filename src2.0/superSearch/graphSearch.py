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

  personalitiesFile = open ("../entityExtraction/personalities.txt", 'rb')
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



#graphSearch('Vasco Cordeiro')
#personalityPopularity ('Carlos Silva')
