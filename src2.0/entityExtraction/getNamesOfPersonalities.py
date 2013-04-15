import nltk
import re
from nltk.tag import *
import pymongo
from pymongo import Connection

def extractNames():
    dbName = "eadw"
    collectionName = "news"
    mongodbPort = 27017 #default
    mongoURL = 'localhost'

    mongodb = Connection(mongoURL, 27017)
    db = mongodb[dbName]
    news = db[collectionName]

    personalityList = []
    cursor = news.find()
    doc = next(cursor, None) #no pymongo nao existe hasNext()
    while (doc != None):
        for sent in nltk.sent_tokenize(doc["description"]):
            for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
                print chunk
                if hasattr(chunk, 'node'):
                    if chunk.node == "PERSON":
                        aux = ' '.join(c[0] for c in chunk.leaves())
                        personalityList.append(aux)

        doc = next(cursor, None)
        print "Description"
        print doc["description"]
        print "Personalities"
        print personalityList
        raw_input("Check if Person took out well")                

extractNames()

# def _getNames(): 
#     text = "Rui afirmou na entrevista que constituiu o prefacio as suas aparicoes semanais na RTP que vinha para tomar a palavra e participar no debate publico. E ridiculo ter de o dizer mas esta no.O arquiteto Joaquim Soeiro e o candidato do PSD a Camara Municipal de Vendas Novas liderada pela CDU nas eleicoes autarquicas deste ano revelou hoje o proprio a agencia Lusa"
#     list = []  
#     for sent in nltk.sent_tokenize(text): 
#         for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))): 
#             print chunk
#             if hasattr(chunk, 'node'): 
#                 if chunk.node == "PERSON":
#                    aux = ' '.join(c[0] for c in chunk.leaves()) 
#                     list.append(aux) 
    
#     print list 
    
    
# _getNames()
