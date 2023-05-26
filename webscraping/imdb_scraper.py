import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = "https://www.imdb.com/"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
r = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250').text
soup = BeautifulSoup(r, 'lxml')

table = soup.find('table', class_='chart full-width').tbody

filmlist = []

for em in table.find_all('tr')[:10]: # just to grab the first 10 of the list
	title = em.find('td', class_='titleColumn').a.text.strip()  # strip() just removes the whitespace from the beg and end of the string
	link = em.find('td', class_='titleColumn').a['href']
	year = em.find('td', class_='titleColumn').find('span',class_='secondaryInfo').text.strip()
	rating = em.find('td', class_='ratingColumn imdbRating').strong.text.strip()

	#print(f'Title: {title}, Year: {year}, Rating: {rating}')
	#print(f'Link: {baseurl}{link}')

	film = {
		'title': title,
		'year': year,
		'rating': rating,
		'link': baseurl+link
	}
	filmlist.append(film)

df = pd.DataFrame(filmlist)
print(df.head(10))





