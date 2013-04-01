import feedparser
from whoosh.fields import *
from whoosh.index import *


dn = feedparser.parse("http://feeds.dn.pt/DN-Politica")
jn = feedparser.parse("http://feeds.jn.pt/JN-Politica")

#Title;Link;Description
schema = Schema(title = TEXT, link=TEXT, description=TEXT, category=TEXT, pubdate=DATETIME)

