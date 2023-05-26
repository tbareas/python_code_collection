from requests_html import HTMLSession

def weather_info(city):	
	s = HTMLSession()
	url = f'https://www.google.com/search?q=weather+{city}'
	req = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})

	temp = req.html.find('span#wob_tm', first=True).text
	#unit = req.html.find('div.UQt4rd', first=True).find('span.wob_t', first=True).text ## Not working :/
	desc = req.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text
	dtime = req.html.find('div.VQF4g', first=True).find('div#wob_dts.wob_dts', first=True).text

	print(f'Current weather info in {city}: {temp} °C, {desc} ({dtime})')

if __name__ == '__main__':
	query = input("Type in which city's weather data are you interested in: ")
	#query = 'Budapest'
	weather_info(query)