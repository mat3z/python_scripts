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

def get_years(soup):
	years = []
	years_rows = soup.find_all('span', class_="secondaryInfo")
	for row in years_rows:
		number = row.get_text()[1:5]
		years.append(number)
	return years

def write_ranking_to_file(movies, years, ids):
	with open('ranking.csv', 'w') as csv_file:
		csv_writer = writer(csv_file)
		csv_writer.writerow(['rank', 'title', 'year', 'id'])
		for rank, movie, year, id in zip(range(1, len(movies)+1), movies, years, ids):
			csv_writer.writerow([rank, movie, year, id])


data = fetch_data()
movies = get_ranking(data)
ids = get_ids(data)
years = get_years(data)
write_ranking_to_file(movies, years, ids)