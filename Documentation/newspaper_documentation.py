import newspaper
#newspaper.languages(Swahili)
from newspaper import Article
import nltk
#nltk.download('punkt')

url = "https://www.damninteresting.com/private-wojteks-right-to-bear-arms/"
article = Article(url)
article.download() #-- downloads an article
article.html #extracts html from the code
article.parse()
article.authors #To find the name of authors in the article 
publish = article.publish_date#finds the date pf publication
article.text #finds texts in the article 
article.top_image #returns first image 
article.movies #returns 'movies' in the article
article.nlp()
article.keywords
article.summary #returns a summary of the text 

