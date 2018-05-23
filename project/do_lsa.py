from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from movie import Movie
import os

def get_titles():
	reviews_dir = f'{os.path.dirname(os.getcwd())}/reviews'
	return list(os.walk(reviews_dir))[0][1]

def get_movies_with_reviews(titles):
	return [Movie(title) for title in titles]

if __name__ == '__main__':
	titles_list = get_titles()
	# movies = get_movies_with_reviews(titles_list)
	# revs = movies[0].get_reviews()
	title = 'The Shawshank Redemption'
	movie = Movie(title)
	revs = movie.get_reviews()


	vectorizer = TfidfVectorizer(stop_words='english', use_idf=True, ngram_range=(1,3))
	X =vectorizer.fit_transform(revs)
	lsa = TruncatedSVD(n_components=25,n_iter=100,random_state=42)
	lsa.fit(X)
	terms = vectorizer.get_feature_names()

	# print(lsa.components_)

	for i,comp in enumerate(lsa.components_):
		termsInComp = zip(terms,comp)
		sortedterms = sorted(termsInComp, key=lambda x: x[1],reverse=True)[:10]
		print("Concept %d:" % i)
		for term in sortedterms:
			print(term[0], term[1])
		print(" ")

