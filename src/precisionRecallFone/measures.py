#F1 ; Precison ; Recall

#Recall
def recall(listOfReturnedDocumentsID, relevantDocuments):
    counter = 0;
    if len(listOfReturnedDocumentsID) == 0:
        return 0
    
    for docID in listOfReturnedDocumentsID:
        if docID in relevantDocuments:
            counter = counter + 1
    return counter/float(len(relevantDocuments))


#Precision 
def precision(listOfReturnedDocumentsID, relevantDocuments):
    counter = 0;
    if len(listOfReturnedDocumentsID) == 0:
        return 0
    
    for docID in listOfReturnedDocumentsID:
        if docID in relevantDocuments:
            counter = counter + 1

    return counter/float(len(listOfReturnedDocumentsID))

#F1
def fone(listOfReturnedDocumentsID, relevantDocuments):
    re = recall(listOfReturnedDocumentsID, relevantDocuments)
    pr = precision(listOfReturnedDocumentsID, relevantDocuments)
    if re == 0 and pr == 0:
        return 0
    return 2 * re * pr/(re + pr)