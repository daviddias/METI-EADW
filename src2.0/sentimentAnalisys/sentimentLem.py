import nltk

#def sentilexToPython():

palavras = {}
positive = 0
negative = 0
neutro = 0
aux = {}
fileName = "SentiLex-lem-PT02.txt"
inputFile = open(fileName,"rb")
i = "abelhudo"
text = "Antonio Joss Seguro ja leu a carta e prosseguiu a agenda do dia De momento nada mais ha a acrescentar disse a mesma fonte da direcao do PS fazendo contudo a seguinte ressalva Mas seria a primeira vez que um lider da oposicao nao estaria num encontro apos convite do primeiro ministro O primeiro ministro Pedro Passos Coelho convidou hoje o secretario geral do PS para um encontro a realizar na quarta feira de manha tendo em vista um entendimento sobre as medidas para a consolidacao orcamental Em particular torna se urgente garantir o cumprimento da execucao orcamental de 2013 e do quadro orcamental de medio prazo e concertar as medidas que garantam esse objetivo dado ate que algumas delas se encontram para alem do prazo da legislatura que cobre a acao do Governo escreve Pedro Passos Coelho numa carta enviada hoje a Antonio Jose Seguro a que a agencia Lusa teve acesso."
tokens = nltk.word_tokenize(text)

for line in inputFile:
        splitted = line.split(";")
        DicionarioAux = {}
    
        DicionarioAux [splitted[1][:2]] = splitted[1][3:]
        DicionarioAux [splitted[2][:3]] = splitted[2][3:].split("=")[1]
        
        DicionarioAux [splitted[3][:4]] = splitted[3][5:]
        DicionarioAux [splitted[0].split(".")[1].split("=")[0]] = splitted[0].split(".")[1].split("=")[1]
         
      
    
        palavras[splitted[0].split(".")[0]] = DicionarioAux 
        


     
for i in range(0,len(tokens)):
    if tokens[i] in palavras.keys():
       if (palavras[tokens[i]]['POL'] == '-1'):
         negative = negative + 1
         print 'ola'
       elif (palavras[tokens[i]]['POL'] == '1'):
         positive = positive + 1
       else: 
         neutro = neutro + 1  

print negative
print positive
print neutro


if negative > positive & negative > neutro:
     print "sent is negative"
     print negative
elif negative < positive & positive > neutro:    
     print "sent is positive"
     print positive
else:
     print "sent is neutro"
     print neutro   
