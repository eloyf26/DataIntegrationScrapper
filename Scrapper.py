from cgi import test
from bs4 import BeautifulSoup
import requests
def test():
    page = requests.get("https://cine.entradas.com/")

    if (page.status_code != 200):

        print("download not succesfull")
        exit
    print("hola julia")
    
    soup=BeautifulSoup(page.content,'html.parser')
    print(soup.prettify())


test()