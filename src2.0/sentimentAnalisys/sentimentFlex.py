
import nltk

palavras = {}
positive = 0
negative = 0
neutro = 0
result = 0
aux = {}

i = "abelhudo"



def DictionaryOfWords():
  fileName = "SentiLex-flex-PT02.txt"
  inputFile = open(fileName,"rb")  
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
        
        palavras[splitted[0].split(",")[0]] = DicionarioAux 
        palavras[splitted[0].split(",")[1]] = DicionarioAux
   
  return palavras


def checks(dict):
  #text1 = 'badalhoco ola es uma merda estarem sempre a bater na mesma tecla'
  #token = nltk.word_tokenize(text1)
  

  text = 'A Justica deve ter como pressuposto a, e nao ha Justica sem verdade. Apurar a nem sempre e facil mas sem  nao ha Justica'
  tokens = nltk.word_tokenize(text)
  result = 0
  
  for word in palavras.keys():
    if word in text:
       
       if ' ' in word:
          
          if palavras[word]['POL'] == '-1':
            result = result - 1 
          elif palavras[word]['POL'] == '1':
            result = result + 1 
          else: result = result + 0
      
       elif (word in tokens): 
           print word
           if palavras[word]['POL'] == '-1':
             result = result - 1 
           elif palavras[word]['POL'] == '1':
              result = result + 1 
           else: result = result + 0  


  print result
  return result             

checks(DictionaryOfWords())

#for i in range(0,len(tokens)):
#    if tokens[i] in palavras.keys():
#       if (palavras[tokens[i]]['POL'] == '-1'):
#         negative = negative + 1
#         
#       elif (palavras[tokens[i]]['POL'] == '1'):
#         positive = positive + 1
#       else: 
#         neutro = neutro + 1  

#print negative
#print positive
#print neutro
