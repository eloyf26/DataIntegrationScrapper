from bs4 import BeautifulSoup
import requests
import re

# Convert the 12 hours format to a 24h format
def to_24H (h, shift):
	if h[-2:] == "pm":
		shift = 12
		h = h[:-3]
	if h[-2:] == "am":
		h = h[:-3]


	splitted = h.split(':')
	if splitted[0] != "12":
		h = str(int(splitted[0]) + shift) + ":" + splitted[1]

	return h,shift


# url = "https://www.imdb.com/showtimes/ES/28912/"		#Get main page url

def get_cinemas (url):
	# id_file = open("Cines.txt","w")
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	dates = soup.find('div', class_ = 'datepicker').find_all('a', href=True)		# Obtain the links for all days in the web

	all_info = []
	dates_names = ["Day 1","Day 2","Day 3","Day 4","Day 5","Day 6","Day 7"]
	# Loop to get the showtimes for each day
	for ind, date in enumerate(dates):
		d = date['href']
		url = f'https://www.imdb.com{d}'
		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		cinemas_info = soup.find_all('div', class_ = ['list_item odd','list_item even'])

		# Loop to get each cinema's info
		for cine_inf in cinemas_info:

			# Date
			# date_to_date = date.span.text.strip() + ' ' + date.contents[1]
			# print(f'Date: {date_to_date}')

			try:
				cinema_name = cine_inf.find('div', class_ = 'fav_box').text.strip()
			except:
				cinema_name = None
			# print (cinema_name)

			# Get name and showtimes for each film
			films = cine_inf.find_all('div', class_ = 'list_item')


			for film in films:

				cinema_film_info = []
				cinema_film_info.append(dates_names[ind])
				cinema_film_info.append(cinema_name)
				
				try:
					film_name = film.find('span', itemprop = 'name').text.strip()		# Get films name

					# Removing the year from the movie title
					regex = re.findall(r'\(([^)]+)\)', film_name)[-1]
					year = f' ({regex})'
					film_name = film_name.replace(year, '')
				except:
					film_name = film.find('span', itemprop = 'name').text.strip()

				cinema_film_info.append(film_name)

				# Get the schedule
				try:
					shift = 0
					hours = []
					schedule = film.find('div', class_ = 'showtimes').contents

					while len(schedule) > 0:
						(h,shift) = to_24H (schedule[0].text.strip(), shift)
						schedule = schedule[2:]
						if h not in hours:
							hours.append(h)

					cinema_film_info.append(hours)

				except:

					hours = None
					cinema_film_info.append(hours)

				all_info.append(cinema_film_info)
			# 	print(f''' 
			# film name: {film_name}
			# schedule: {hours}
			# 	''')

	return all_info