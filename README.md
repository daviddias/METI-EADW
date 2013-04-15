eadw-ist
========

Data-Mining IST, Technical University of Lisbon Course

### How to run this

1. Start MongoDB
2. Clean db(if you have trash)
3. fire newsCollector/collector.py
4. Empty newsSearch/index_dir
5. fire newsSearch/indexInWhoosh.py



### Issues

[ ] feedparser is not sanitizing descriptions lot's of html there :(

### Ideas

[ ] Use BM25 and TF_IDF over Titles for search and give them more weigt in search, so Titles prove to be more relevant


### MongoDB

# Bootstrap MongoDB
	Windows:
		No idea :P Joking check this: http://www.mongodb.org/downloads
	Mac OS X
		brew install mongo
		mongod to run server
		mongo to run mongo shell (client)
		done :)


# db needed:
	eadw
	collections:
		news




