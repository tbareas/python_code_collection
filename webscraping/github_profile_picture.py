import requests
from bs4 import BeautifulSoup as bs
import os

def get_usr(github_usr):
	"""
	Getting profile picture link of the given github user.
	"""
	try:
		url = 'https://github.com/'+github_usr
		r = requests.get(url)
	except:
		raise ValueError(f'User not found: {github_usr}')
	soup = bs(r.content, 'html.parser')
	profile_picture = soup.find('img', {'alt':'Avatar'})['src']
	print(f'Profile picture link: {profile_picture}')
	return profile_picture

def imagedown(github_usr, pic_url, folder):
	"""
	Optionally we can write the image to file.
	"""
	try:
		os.mkdir(os.path.join(os.getcwd(),folder))
	except:
		pass
	os.chdir(os.path.join(os.getcwd(), folder))

	img = requests.get(pic_url)
	with open(github_usr+'_profile_picture.jpg', 'wb') as f:
		f.write(img.content)
		print(f'Writing image of {github_usr} to file.')

if __name__ == '__main__':

	github_usr = input('Input the github user name: ')
	usr_picture = get_usr(github_usr)
	imagedown(github_usr, usr_picture, 'gh_profpic')


