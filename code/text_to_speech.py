from newspaper import Article 
import nltk
import os 
from gtts import gTTS #google text-to-speech python module
nltk.download('punkt')
language = 'en'


url = "https://www.damninteresting.com/private-wojteks-right-to-bear-arms/"
ToRead = Article(url)

ToRead.download()
ToRead.parse()
ToRead.nlp() 

text = ToRead.text


speech = gTTS(text=text, lang=language, slow= False)
speech.save("text-to-speech.mp3")
os.system("mpg321 text-to-speech.mp3")


