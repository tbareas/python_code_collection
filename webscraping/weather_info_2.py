from requests_html import HTMLSession

# Modif from version 1:
	# Also use try-except for error handling
	# use a list of cities to search
	# print it to a textfile

s = HTMLSession()

query = input("Type in which city's weather data are you interested in (format e.g.: Budapest, Moscow, New York, London): ")
list_query = query.split(',')

def check_city(list_q):
	""" Returns a fixed list of cities, if the given city cannot be found. """
	fixed_list = []
	for e in list_q:
		try:
			url = f'https://www.google.com/search?q=weather+{e}'
			req = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})
			temp_is_found = req.html.find('span#wob_tm', first=True).text
		except Exception:
			print(f"City name cannot be found: {e}")
		else:
			fixed_list.append(e)
	return fixed_list

new_list = check_city(list_query)

for e in new_list:
	url = f'https://www.google.com/search?q=weather+{e}'
	req = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})

	temp = req.html.find('span#wob_tm', first=True).text
	desc = req.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text
	dtime = req.html.find('div.VQF4g', first=True).find('div#wob_dts.wob_dts', first=True).text

	info = f"Current weather info in {e}: {temp}°C, {desc} ({dtime})\n"
	with open('city-weather.txt','a') as wf:
		wf.write(info)

	print(info) # also print out to console


