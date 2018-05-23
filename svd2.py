from nltk.corpus import reuters
from sklearn.feature_extraction.text import TfidfVectorizer
# import nltk
# nltk.download('reuters')
tfidf = TfidfVectorizer()

tfidf.fit([reuters.raw(file_id) for file_id in reuters.fileids()])

X = tfidf.transform([reuters.raw('test/14829')])

print([X[0, tfidf.vocabulary_['year']]])