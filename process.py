import logging
import re

from wordcloud import WordCloud
from nltk import word_tokenize, FreqDist
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

user_stop_words = ["language","model"]
logger = logging.getLogger("global")

class TextProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()
        self.wordcloud = WordCloud(width=800, height=400, background_color="white")

    def process_titles(self, titles):
        
        # 1. tokenize 2.filter stopwords 3.lemmatizer
        logger.info("Processing titles...")
        
        text = " ".join(titles)
        text = re.sub(r'<.*?>', '', text)
        words = word_tokenize(text)
        words = [word.lower() for word in words if word.isalnum() and word.lower() not in self.stop_words]
        words = [self.lemmatizer.lemmatize(word) for word in words]
        words = [word.lower() for word in words if word.lower() not in user_stop_words]
        
        # wordcloud
        word_freq = FreqDist(words)
        wordcloud_img = self.wordcloud.generate_from_frequencies(word_freq)
        logger.info("Successfully generate the word cloud.")
        return wordcloud_img

 