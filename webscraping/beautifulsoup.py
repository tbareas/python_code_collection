import requests
from bs4 import BeautifulSoup
import csv

with open('simple.html','r') as f:
	soup = BeautifulSoup(f,'lxml') # using the lxml parser (need to be pip installed)

# print(soup.prettify()) # prettify just indent the html

#match = soup.title.text # grabs the title section in html, and only prints its content (text)
#footer = soup.find('div', class_='footer')
#article = soup.find('div', class_='article')
#headline = article.h2.a.text
#print(headline)
#print(article.p.text)

## But in the file we have two articles, and soup.find method only gives the first match
## so we need to use soup.find_all with for loop to get all of them
#for article in soup.find_all('div', class_='article'): # bcus find_all returns a list..
#	headline = article.h2.a.text
#	print(headline)
#	summary = article.p.text
#	print(summary)
#	print()

# ----------
# Using it on real website

source = requests.get('https://coreyms.com').text
bsoup = BeautifulSoup(source, 'lxml')
article = bsoup.find('article')

#headline = article.h2.a.text
#print(headline)
#summary = article.find('div', class_='entry-content').p.text
#print(summary)
#
#vid_src = article.find('iframe', class_='youtube-player')['src']
##print(vid_src)
#vid_id = vid_src.split('/')[4] # 4.th index in the list
#vid_id = vid_id.split('?')[0]
##print(vid_id) # now we got the video id
#
#yt_link = f'https://youtube.com/watch?v={vid_id}'
#print(yt_link)

# ----------------



with open('bsoup_tut.csv','w') as csvfile:
	csv_writer = csv.writer(csvfile, delimiter=',')
	csv_writer.writerow(['headline', 'summary', 'video_link'])

	for article in bsoup.find_all('article'):
		headline = article.h2.a.text
		print(headline)
		summary = article.find('div', class_='entry-content').p.text
		print(summary)

		try:
			vid_src = article.find('iframe', class_='youtube-player')['src']
			vid_id = vid_src.split('/')[4] # 4.th index in the list
			vid_id = vid_id.split('?')[0]
			yt_link = f'https://youtube.com/watch?v={vid_id}'
		except Exception as e:
			yt_link = None

		print(yt_link)
		print()

		csv_writer.writerow([headline, summary, yt_link]) # writes a new row with given data into csv
















