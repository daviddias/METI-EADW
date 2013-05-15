#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import urllib

def articleContent(html):
 	aux = unicode("") 
 	html = urllib.urlopen(html).read()
 	soup = BeautifulSoup(html)
 	soup.encode('utf-8')
 	text = soup.find(id="Article")

 	if(text == None): #Somethings the new is down 
 		return aux
 	#print "text"
 	#print text

 	for string in text.strings:
  		aux += string
 	#print aux
 	return aux



#http://feeds.dn.pt/~r/DN-Politica/~3/mUn_D0WVDEg/story01.htm