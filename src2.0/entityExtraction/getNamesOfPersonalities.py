#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
import re
from nltk.tag import *
import pymongo
from pymongo import Connection




def extractNames():
    dbName = "eadw"
    collectionNameNews = "news"
    collectionNamePersonalities = "newsPersonality"
    mongodbPort = 27017 #default
    mongoURL = 'localhost'

    mongodb = Connection(mongoURL, 27017)
    db = mongodb[dbName]
    news = db[collectionNameNews]
    pers = db[collectionNamePersonalities]

    personalitiesFile = open ("personalities.txt", 'rb')
    personalitiesList = {}
    for line in personalitiesFile:
    	personalitiesList = eval(line)

   
    cursor = news.find()
    doc = next(cursor, None) #no pymongo nao existe hasNext()
    while (doc != None):
       	peopleList = [] 
        for sent in nltk.sent_tokenize(doc["description"]):
            for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
                #print "CHUNK"
                #print chunk
                if hasattr(chunk, 'node'):
                    if chunk.node == "PERSON":
                        aux = ' '.join(c[0] for c in chunk.leaves())
                        #1. Filtrar
                        if aux in personalitiesList["listPersonalities"]: #Verificar se é personalidade
                        	peopleList.append(aux)	
                        else:
                        	continue
                      

        # aqui "peopleList" tem a lista de personalidades deste doc
        # 2 . Inserir na base de dados o doc + personalities
        newDoc = doc
        newDoc["personalities"] = peopleList
        pers.insert(newDoc);
        #print "Description"
        #print doc["description"]
        #print "Personalities"
        #print peopleList
        #raw_input("Check if Person took out well")  
        doc = next(cursor, None)              




#def personalityFilter(personList):







extractNames()
