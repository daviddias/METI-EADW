#see if it's special search, if it is, do it and return true#see if it's special search, if it is, do it and return true
import popularity

sortedDesc = popularity.orderedByPopularity()
def popular(text):
  if text == 'who is more popular':
    print popularity.whoIsMorePopular(sortedDesc)[0]
    return True
  else:
    return False

def hated(text):
  if text == 'who is more hated':
    print popularity.whoIsMoreHated(sortedDesc)[0]
    return True
  else:
    return False 

def checkIfSpecial(text):
  if popular(text):
  	return True
  if hated(text):
  	return True