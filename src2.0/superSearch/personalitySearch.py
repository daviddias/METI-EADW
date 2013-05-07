import graphSearch
import popularity
import nltk

def getPersonality(text):
    names = []
    personalitiesFile = open ("personalities.txt", 'rb')
    personalitiesList = {}
    for line in personalitiesFile:
        personalitiesList = eval(line)
    #print personalitiesList
    for sent in nltk.sent_tokenize(text):    
      for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
                #print "CHUNK"
                #print chunk
                if hasattr(chunk, 'node'):
                    if chunk.node == "PERSON":
                        aux = ' '.join(c[0] for c in chunk.leaves())
                        #1. Filtrar
                        if aux in personalitiesList["listPersonalities"]: 
                            names.append(aux)
                            
                      
    return names


def relatedPersonalities(names):
    relatePersonalities = {} 
    if len(names) == 0:
      return
    else:
        for name in names:
           relatePersonalities[name] = graphSearch.graphSearch(name)
    #print relatePersonalities
    return relatePersonalities         

def personPopularity(names):
     result = {}
     if len(names) == 0:
      return
     else:
        for name in names:
            result[name] = popularity.personalityPopularity(name)
     return result
 
def printPersonality(text):
    related = {}
    popularity = {}
    names = []
    names = getPersonality(text)
    related = relatedPersonalities(names)
    popularity = personPopularity(names)  
    
    for i in range(0,len(names)):
        print '-------------------------'
        print 'Personality: ' + names[i]
        
        if popularity[names[i]][0] != 0 or popularity[names[i]][1] != 0 or popularity[names[i]][2] != 0 or popularity[names[i]][3]:
          print 'Popularity:' + str(popularity[names[i]][3])  
          print 'Appears in : ' +  str(popularity[names[i]][0]) + ' News'
          print 'PositiveScore: ' + str(popularity[names[i]][1])
          print 'NegativeScore: ' + str(popularity[names[i]][2])
        if len (related[names[i]]) != 0 :
         print 'Related Graph: ' + str(related[names[i]])
        print '-------------------------'
        print '\n'  


printPersonality("ola eu sou o Miguel Relvas e o Carlos Zorrinho")
#print relatedPersonalities(getPersonality("ola eu sou o Miguel Relvas e o Carlos Zorrinho"))
