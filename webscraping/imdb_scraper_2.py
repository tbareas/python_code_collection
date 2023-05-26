## Task:
## Writing a script that looks for a movie genre category in imdb, but only films or only tvshows
## link: https://www.imdb.com/search/title/?genres=adventure
## Then put this to pandas, csv, textfile, or sql table

#from requests_html import HTMLSession  # bs4 is much better than this way.. also easier usage
from bs4 import BeautifulSoup
import requests
import pandas as pd


def ask_usr():
	list_of_genres = ['comedy', 'fantasy', 'sci-fi', 'action', 'adventure', 'romance', 'drama', 'thriller', 'animation', 'biography', 'crime', 'family', 
						'film-noir', 'history', 'horror', 'music', 'musical', 'mystery', 'sport', 'war', 'western']	
	usr_req = input("Type in the genre of movies/TV series you want(in form eg.: comedy): ").lower()

	if usr_req not in list_of_genres:
		raise Error("Sorry, the given genre name is not found.")
	else:
		return request_handler(usr_req)


def request_handler(usr_req):
	r = requests.get(f'https://www.imdb.com/search/title/?genres={usr_req}').text
	soup = BeautifulSoup(r, 'lxml')
	filmlist = []

	table = soup.find('div',class_='lister-list')
	for em in table.find_all('div',class_='lister-item mode-advanced')[:10]:
		title = em.find('h3',class_='lister-item-header').a.text.strip()
		year = em.find('h3',class_='lister-item-header').find('span',class_='lister-item-year text-muted unbold').text.strip()
		year = year.split('(')[1].split(')')[0]
		baseurl = "https://www.imdb.com"
		link = em.find('div',class_='lister-item-content').h3.a['href']

		try:
			runtime = em.find('span',class_='runtime').text.strip()
			genre = em.find('span',class_='genre').text.strip()
			#certificate = em.find('span',class_='certificate').text.strip()
			imdb_rating = em.find('div',class_='ratings-bar').find('div',class_='inline-block ratings-imdb-rating').strong.text.strip()
			votes = em.find('p',class_='sort-num_votes-visible').select('span')[1].get_text(strip=True) # to select the second span child element
			desc = em.find('p', class_='text-muted').text.strip()
		except: # if one of these data are missing from the movie (it is common)
			pass

		#print(usr_req,title,year,genre,runtime,certificate,imdb_rating,votes,desc[:10])

		dic = {
			#"UsrRequest": usr_req,
			"Title": title,
			"Year": year,
			"Genre": genre,
			"Runtime": runtime,
			#"Certificate": certificate,
			"Rating": imdb_rating,
			"Votes": votes,
			#"Description": desc,
			"Link": baseurl+link,
		}
		filmlist.append(dic)

	return filmlist


if __name__ == "__main__":
	result = ask_usr()
	df = pd.DataFrame(result)
	print(df.head(5))





