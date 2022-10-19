from bs4 import BeautifulSoup
#from matplotlib.ticker import NullFormatter
import requests

#Aquí el link entra como una variable del loop
# url = "https://www.imdb.com/showtimes/location?ref_=sh_lc"

def get_movies (url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    dates = soup.find('div', class_ = 'datepicker').find_all('a', href=True)        # Obtain the links for all days in the web

    movies_info = []
    checking_movies = []

    for date in dates:

        d = date['href']
        url = f'https://www.imdb.com{d}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        movie_urls1 = soup.find_all('div', class_ = 'lister-item-image ribbonize')

        for movie1 in movie_urls1:

            try_name = movie1.find('div', class_ = 'title').text.strip()
            if try_name not in checking_movies:

                checking_movies.append(try_name)

                movie_info = []
                murl1 = "https://www.imdb.com" + movie1.a['href']
                page = requests.get(murl1)
                soup = BeautifulSoup(page.content, 'html.parser')

                movie = "https://www.imdb.com" + soup.find('td', class_ = 'overview-top').h4.a['href']
                # print(movie)

                html_movie = requests.get(movie)
                movie_soup = BeautifulSoup(html_movie.content, 'html.parser')

                #Movie Title
                try:
                    title = movie_soup.find('h1').text.strip()
                    #print(title)
                    movie_info.append(title)
                except:
                    title = None
                    movie_info.append(title)
                        
                data_tech = movie_soup.find_all('a', class_ = 'ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh')

                #Movie Release Date
                try:
                    release_date = data_tech[0].text
                    movie_info.append(release_date)
                except:
                    release_date = None
                    movie_info.append(release_date)

                #Movie Rating
                try:
                    rating = data_tech[1].text
                    movie_info.append(rating)
                except:
                    rating = None
                    movie_info.append(rating)

                #Movie duration
                try:
                    duration = movie_soup.find('ul', class_ = 'ipc-inline-list ipc-inline-list--show-dividers sc-8c396aa2-0 kqWovI baseAlt').find_all('li')[2].text.strip()
                    movie_info.append(duration)
                except:
                    duration = None
                    movie_info.append(duration)

                #Movie Poster
                try:
                    poster = movie_soup.find('img', class_ = 'ipc-image')['src']
                    movie_info.append(poster)
                except:
                    poster = None
                    movie_info.append(poster)

                #Movie genre
                try:
                    genre = movie_soup.find('span', class_ = 'ipc-chip__text').text.strip()
                    movie_info.append(genre)
                except:
                    genre = None
                    movie_info.append(genre)

                #Movie summary
                try:
                    summary = movie_soup.find('span', class_= 'sc-16ede01-1 kgphFu').text
                    movie_info.append(summary)
                except:
                    summary = None
                    movie_info.append(summary)

                #Movie Score
                try:
                    score = movie_soup.find('span', class_ = 'sc-7ab21ed2-1 jGRxWM').text
                    movie_info.append(score)
                except:
                    score = None
                    movie_info.append(score)

                #Movie Director
                try:
                    director = movie_soup.find('a', class_ = 'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link').text.strip()
                    movie_info.append(director)
                except:
                    director = None
                    movie_info.append(director)

                #Cast
                try:
                    ct = movie_soup.find_all('ul', class_ = 'ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content baseAlt', role = 'presentation')[2]

                    cast = []
                    for act in ct.find_all('a', href = True):
                        cast.append(act.text)

                    movie_info.append(cast)
                except:
                    cast = None
                    movie_info.append(cast)

                #Trailer
                try:
                    trailer = "https://www.imdb.com/" + movie_soup.find('a', class_ = 'ipc-lockup-overlay sc-e4a5af48-0 zjJJX ipc-focusable')['href']
                    movie_info.append(trailer)
                except:
                    trailer = None
                    movie_info.append(trailer)


                # print(movie_info)
                movies_info.append(movie_info)

        # print("---------------------------------------")
        # print(movies_info)
    return movies_info


# print(get_movies("https://www.imdb.com/showtimes/location?ref_=sh_lc"))