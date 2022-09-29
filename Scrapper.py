from cgi import test
from bs4 import BeautifulSoup
import requests
def test():
    #cArray = 
    #for linkCinema in cArray:
        #page = requests.get(linkCinema)
    page = requests.get("https://cine.entradas.com/cine/madrid/yelmo-cines-ideal/shows/movies")

    if (page.status_code != 200):

        print("download not succesfull")
        exit
    print("hola julia")
    
    soup=BeautifulSoup(page.content,'html.parser')
    print(soup.prettify())

    #print ("Aqui llego")
    #gf = soup.find_all("movie_image")
    #print ("Aqui llego")
    #for i in gf:
    #    print ("Aqui llego")
    #    print(i)


test()