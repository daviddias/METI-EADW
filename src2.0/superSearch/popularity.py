#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymongo
from pymongo import Connection
import operator


def orderedByPopularity():
  dbName = "eadw"
  collectionNamePersonalitiesSentiment = "newsPersonalitySentiment"
    
  mongodbPort = 27017 #default
  mongoURL = 'localhost'

  mongodb = Connection(mongoURL, 27017)
  db = mongodb[dbName]
  newsPersonalitySentiment = db[collectionNamePersonalitiesSentiment]

  personalities = {}

  cursor = newsPersonalitySentiment.find()
  doc = next(cursor, None) #no pymongo nao existe hasNext()
  while (doc != None):
    #print doc
    if (len(doc["personalities"]) == 0): # 
      doc = next(cursor, None)   
      continue

    for person in doc["personalities"]:
      if person not in personalities:
        personalities[person] = doc["personalities"][person]
      else: 
        personalities[person] = personalities[person] + doc["personalities"][person] 
    doc = next(cursor, None)
  
  #print personalities   
  #now sort and see who is :)
  personalitiesSorted = sorted(personalities.iteritems(), key=operator.itemgetter(1), reverse=True)
  #print personalitiesSorted     
  return personalitiesSorted

def whoIsMorePopular(sortedDesc):
  print sortedDesc[0]      

def whoIsMoreHated(sortedDesc):
  print sortedDesc[-1]      


def personalityPopularity(nameForSearch):
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
              result = result + doc["personalities"][name]
          else:
            continue
      doc = next(cursor, None)
  return result

#whoIsMorePopular(orderedByPopularity())  
#whoIsMoreHated(orderedByPopularity())