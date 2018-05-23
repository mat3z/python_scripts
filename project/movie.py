import os

class Movie:
	def __init__(self, title):
		self.title = title
		self.reviews = []
		self.concepts = []
		self.load_reviews()

	def __repr__(self):
		return f'{self.title} with {self.count_reviews()} reviews'

	# @property
	# def reviews(self):
	# 	return self.reviews

	# @reviews.setter
	# def reviews(self, review):
	# 	self.reviews.append(review)

	def count_reviews(self):
		return len(self.reviews)

	def load_reviews(self):
		root = os.path.dirname(os.getcwd())
		folder = f'reviews/{self.title}'
		movie_directory = os.path.join(root, folder)
		review_files = [files for files in os.walk(movie_directory)][0][2]
		for name in review_files:
			path = os.path.join(movie_directory, name)
			self.reviews.append(self.load_review_file(path))

	def load_review_file(self, name):
		with open(name) as file:
			data = file.read()
		return data

	def get_review(self, i):
		return self.reviews[i]

	def get_reviews(self):
		return self.reviews