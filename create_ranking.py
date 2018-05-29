import requests
from bs4 import BeautifulSoup
from csv import writer
import time

API_KEY='15d2ea6d0dc1d476efbca3eba2b9bbfb'
BASE_URL  = 'https://api.themoviedb.org/3/search/movie?api_key=15d2ea6d0dc1d476efbca3eba2b9bbfb&query='

def fetch_movies_data():
	url = 'http://www.imdb.com/chart/top?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=0YACBGCPEXB7G47FJB10&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=toptv&ref_=chttvtp_ql_3'
	headers = {
		'Accept': 'application/json',
		# 'Accept-Language': 'en-US,en;q=0.5'
		'Accept-Language': 'en-us;q=1.0, pl;q=0'
		}

	res = requests.get(url, headers = headers)
	soup = BeautifulSoup(res.text, 'html.parser')
	return soup

def get_ranking(soup):
	ranking = []
	title_rows = soup.find_all('td', class_='titleColumn')
	for movie in title_rows:
		a_tag = movie.find('a').get_text()
		ranking.append(a_tag)
	return ranking

def get_ids(soup):
	ids = []
	id_rows = soup.find_all('td', class_="watchlistColumn")
	for row in id_rows:
		ids.append(row.div['data-tconst'])
	return ids

def get_years(soup):
	years = []
	years_rows = soup.find_all('span', class_="secondaryInfo")
	for row in years_rows:
		number = row.get_text()[1:5]
		years.append(number)
	return years

def write_ranking_to_file(movies, years, image_urls, ids):
	with open('ranking.csv', 'w') as csv_file:
		csv_writer = writer(csv_file)
		csv_writer.writerow(['rank', 'title', 'year', 'imageUrl','id'])
		for rank, movie, imageUrl, year, id in zip(range(1, len(movies)+1), movies, image_urls, years, ids):
			csv_writer.writerow([rank, movie, year, imageUrl, id])


def fetch_images_urls(titles):
	# base_url = 'http://image.tmdb.org/t/p/w500'
	urls = []
	for title in titles:
		url = BASE_URL + title
		headers = {
			'Accept': 'application/json',
			'Accept-Language': 'en-US,en;q=0.5'
			}

		res = requests.get(url, headers = headers)
		if(res.json()['results'] and isinstance(res.json()['results'][0]['poster_path'], str)):
			image_url = res.json()['results'][0]['poster_path'][1:]
			print(image_url)
		else:
			image_url = 'blank'
			print('Nie ma plakatu ;(')
		urls.append(image_url)
		time.sleep(1)
	return urls

data = fetch_movies_data()
movies = get_ranking(data)
image_urls = fetch_images_urls(movies)
ids = get_ids(data)
years = get_years(data)
write_ranking_to_file(movies, years, image_urls, ids)