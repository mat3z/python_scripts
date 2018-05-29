import csv
import pymongo

client = pymongo.MongoClient()
db = client.reviews_app
movies = db.movies
# movie = {"title": "Up", "year": "2009"}
# movie_id = movies.insert_one(movie).inserted_id
# print(movie_id)

with open('ranking.csv') as csv_file:
	csv_reader = csv.reader(csv_file)
	next(csv_file)
	for row in csv_reader:
		imdbRank = row[0]
		title = row[1]
		imageUrl = '' if row[2] == 'blank' else row[2]
		year = row[3]
		imdbId = row[4]
		movie = {"imdbRank": imdbRank, "title": title, "imageUrl": imageUrl, "year": year, "imdbId": imdbId}
		movies.insert_one(movie)