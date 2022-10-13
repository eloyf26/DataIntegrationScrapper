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


# url = "https://www.imdb.com/showtimes/"		#Get main page url

def get_cinemas (url):
	id_file = open("Cines.txt","w")
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	dates = soup.find('div', class_ = 'datepicker').find_all('a', href=True)		# Obtain the links for all days in the web

	all_info = []
	# Loop to get the showtimes for each day
	for date in dates:
		d = date['href']
		url = f'https://www.imdb.com{d}'
		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		cinemas_info = soup.find_all('div', class_ = ['list_item odd','list_item even'])

		# Loop to get each cinema's info
		for cine_inf in cinemas_info:

			# Date
			date_to_date = date.span.text.strip() + ' ' + date.contents[1]
			# print(f'Date: {date_to_date}')

			cinema_name = cine_inf.find('div', class_ = 'fav_box').text.strip()
			# print (cinema_name)

			# Get name and showtimes for each film
			try:
				films = cine_inf.find_all('div', class_ = 'list_item')


				for film in films:

					cinema_film_info = []
					cinema_film_info.append(date_to_date)
					cinema_film_info.append(cinema_name)
					
					film_name = film.find('span', itemprop = 'name').text.strip()		# Get films name

					# Removing the year from the movie title
					regex = re.findall(r'\(([^)]+)\)', film_name)[-1]
					year = f' ({regex})'
					film_name = film_name.replace(year, '')

					cinema_film_info.append(film_name)

					# Get the schedule
					try:
						shift = 0
						hours = []
						schedule = film.find('div', class_ = 'showtimes').contents

						while len(schedule) > 0:
							(h,shift) = to_24H (schedule[0].text.strip(), shift)
							schedule = schedule[2:]
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

			except:

				film_name = None
				hours = None

				# print(f''' 
				# film name: {film_name}
				# schedule: {hours}
				# ''')
	return all_info
