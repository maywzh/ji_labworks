# -*- coding: utf-8 -*-
from naive_bayes_sentiment_analyzer import SentimentAnalyzer


model_path = './data/bayes.pkl'
userdict_path = './data/userdict.txt'
stopword_path = './data/stopwords.txt'
corpus_path = './data/review.csv'


analyzer = SentimentAnalyzer(model_path=model_path, stopword_path=stopword_path, userdict_path=userdict_path)
text ='这个电影好傻逼'
analyzer.analyze(text=text)
