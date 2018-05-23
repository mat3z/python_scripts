import requests
from bs4 import BeautifulSoup
from csv import writer


def fetch_data():
	url = 'http://www.imdb.com/chart/top?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=0YACBGCPEXB7G47FJB10&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=toptv&ref_=chttvtp_ql_3'
	headers = {
		'Accept': 'application/json',
		'Accept-Language': 'en-US,en;q=0.5'
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

def write_ranking_to_file(movies, ids):
	with open('ranking.csv', 'w') as csv_file:
		csv_writer = writer(csv_file)
		csv_writer.writerow(['rank', 'title', 'id'])
		for rank, movie, id in zip(range(1, len(movies)+1), movies, ids):
			csv_writer.writerow([rank, movie, id])


data = fetch_data()
movies = get_ranking(data)
ids = get_ids(data)
write_ranking_to_file(movies, ids)