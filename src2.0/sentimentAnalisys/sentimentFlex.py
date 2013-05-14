#!/usr/bin/python
# -*- coding: utf-8 -*-
import nltk
import codecs

def sentiLexFlexToDict():
  fileName = "SentiLex-flex-PT02.txt"
  inputFile = codecs.open(fileName,"rb","utf-8")
  expressions = {}
  for line in inputFile:
        splitted = line.split(";")
        DicionarioAux = {}
        if(len(splitted[1].split('=')) == 1):
          DicionarioAux [splitted[1].split('=')[0]] = ''
        else:
          DicionarioAux [splitted[1].split('=')[0]] = splitted[1].split('=')[1] 
  
        DicionarioAux [splitted[2].split('=')[0]] = splitted[2].split('=')[1]
        DicionarioAux [splitted[3].split(':')[0]] = splitted[3].split(':')[1].split('=')[1]
  
        if (splitted[4].split('=')[0] == 'ANOT'):
          DicionarioAux [splitted[4].split('=')[0]] = splitted[4].split('=')[1]
        else:
          DicionarioAux [splitted[4].split('=')[0].split(':')[0] ] = splitted[4].split('=')[1]
        
        expressions[splitted[0].split(",")[0]] = DicionarioAux 
        expressions[splitted[0].split(",")[1]] = DicionarioAux
   
  return expressions #SentiLex-Flex em Dict



def polarity(dictOfExpressions,textToAnalyse):
  tokens = nltk.word_tokenize(textToAnalyse)
  result = 0
  
  for expression in dictOfExpressions.keys():
    if expression in textToAnalyse:
       
       if ' ' in expression: #ver se é expressão ou palavra
          if dictOfExpressions[expression]['POL'] == '-1':
            result = result - 1 
          elif dictOfExpressions[expression]['POL'] == '1':
            result = result + 1 
          else: result = result + 0
      
       elif (expression in tokens): 
           if dictOfExpressions[expression]['POL'] == '-1':
             result = result - 1 
           elif dictOfExpressions[expression]['POL'] == '1':
              result = result + 1 
           else: result = result + 0  


  #print result
  return result             
