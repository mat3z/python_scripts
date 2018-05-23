import os

def get_review_file(name):
	with open(name) as file:
		data = file.read()
	return data

def show_reviews_in_dirs(dir_name):
	reviews = []
	for root, dirs, files in os.walk(dir_name):
		for name in files:
			path = os.path.join(root, name)
			if os.path.isfile(path): 
				reviews.append(get_review_file(path))
	return reviews

def scan_reviews_directory(dir_name):
	# all_movies_reviews = {}
	# for root, dirs, files in os.walk(dir_name):
	# 	for name in dirs:
	# 		path = os.path.join(dir_name, name)
	# 		all_movies_reviews[name] = show_reviews_in_dirs(path)
	# return all_movies_reviews
	#### OR #####
	titles = list(os.walk(dir_name))[0][1]
	return {title: show_reviews_in_dirs(os.path.join(dir_name, title)) for title in titles}

alljson = scan_reviews_directory('reviews')
# print(alljson)

# for k, v in alljson.items():
# 	print(k, len(v))