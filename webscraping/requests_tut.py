import requests

#r = requests.get('https://xkcd.com/353/')

#print(r) # only prints out 200 which is normal connection, no erroir

#print(dir(r)) # prints the object's class's library content (requests)

#print(r.text) # prints the webpage content in html

# ------------------------------------
r = requests.get('https://imgs.xkcd.com/comics/python.png')
#with open('comic.png','wb') as f:   # can write image with writing in binary mode
#	f.write(r.content)
#print(r.status_code) # 
#print(r.ok) # return true if <400 response False if >400
print(r.headers) # prints metadata info from the page: for ex. server, content type, last modified etc.

# -----------------------------------
#r = request.get('https://httpbin.org/get?page=2&count=25')
#payload = {'page': 2, 'count':25}
#r = requests.get('https://httpbin.org/get', params=payload) # same as above but we can pass in as parameters

#print(r.text)
#print(r.url) # prints the url


# ------------------------------------
# Posting data
#payload = {'username': 'Bence', 'password':'testing'}
#r = requests.post('https://httpbin.org/post', data=payload) 

#print(r.text) # prints out the forms data with the setted usr and pw

#r_dict = r.json() # creates a python dict from a json response (basically same as import json and use json.loads(r) on the response text)
#print(r_dict['form']) 

# --------------------------------------

#r = requests.get('https://httpbin.org/basic-auth/Bence/testing', auth=('Bence','testing')) 

#print(r.text)

























