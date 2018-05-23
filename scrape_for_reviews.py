import requests
from bs4 import BeautifulSoup
import csv
import time
import os

def create_dir_of_film(title):
	if not os.path.exists(title):
		os.makedirs(title)

def get_reviews_webpage(id):
	url = f'https://www.imdb.com/title/{id}/reviews?ref_=tt_ov_rt'
	headers = {
		'Accept': 'application/json',
		'Accept-Language': 'en-US,en;q=0.5'
		}

	res = requests.get(url, headers = headers)
	soup = BeautifulSoup(res.text, 'html.parser')
	return soup

def retrieve_reviews(soup):
	reviews = []
	review_rows = soup.find_all('div', class_='text')
	for review in review_rows:

		reviews.append(review.get_text())

	return reviews

def save_reviews_to_files(reviews, dir_name):
	here = os.path.dirname(os.path.realpath(__file__))
	for i, review in zip(range(1, len(reviews)+1), reviews):
		file_name = f'{i}.txt'
		file_path = os.path.join(here, dir_name, file_name)
		create_dir_of_film(dir_name)
		with open(file_path, 'w') as file:
			file.write(str(review))

def read_ranking_file(name):
	with open(name) as csv_file:
		csv_reader = csv.reader(csv_file)
		next(csv_file)
		for row in csv_reader:
			reviews = []
			# create_dir_of_film(row[1])
			html_text = get_reviews_webpage(row[2])
			reviews = retrieve_reviews(html_text)
			save_reviews_to_files(reviews, row[1])
			time.sleep(10)

read_ranking_file('ranking.csv')