var FeedParser = require('feedparser')
  , request = require('request');


request('http://feeds.dn.pt/DN-Politica')
  .pipe(new FeedParser())
  .on('error', function(error) {
    console.log("error of some sort");
  })
  .on('article', function (article) {
    console.log(article.title);
    //soup it!
    console.log(article.description);
    // do something else
  })



//function collect(url){



//}