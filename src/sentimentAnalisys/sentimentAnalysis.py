#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymongo
from pymongo import Connection
import sentimentFlex

#1 Ir buscar um artigo com personalidades
#(2nd phase) - Partir em frases
#2 Analisar a polaridade
#3 Adicionar a polaridade as personalidades desse artigo (2nd phase) - Adicionar só a polaridade de uma frase a pessoa que se encontra nela

def analyseSentiment():
  dbName = "eadw"
  collectionNamePersonalities = "newsPersonality"
  collectionNamePersonalitiesSentiment = "newsPersonalitySentiment"
    
  mongodbPort = 27017 #default
  mongoURL = 'localhost'

  mongodb = Connection(mongoURL, 27017)
  db = mongodb[dbName]
  newsPersonality = db[collectionNamePersonalities]
  newsPersonalitySentiment = db[collectionNamePersonalitiesSentiment]

  sentilex = sentimentFlex.sentiLexFlexToDict() # dict to use to know the sentiment
  
  cursor = newsPersonality.find()
  doc = next(cursor, None) #no pymongo nao existe hasNext()
  while (doc != None):
    if (len(doc["personalities"]) == 0): # 
      doc = next(cursor, None)   
      continue

    sentimentValue = sentimentFlex.polarity(sentilex,doc["description"])
    
    personalities = doc["personalities"]
    doc["personalities"] = {} # convert to dic

    for person in personalities:
      doc["personalities"][person] = sentimentValue

    newsPersonalitySentiment.update({"title": doc["title"] }, doc, True); # upsert like a BOSS!
    doc = next(cursor, None)   

analyseSentiment()  