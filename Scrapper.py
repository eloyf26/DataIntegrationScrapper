from cgi import test
from bs4 import BeautifulSoup
import pandas as pd
import requests
def test():
    page = requests.get("https://cine.entradas.com/cine/madrid/yelmo-cines-ideal/shows/movies")

    if (page.status_code != 200):

        print("download not succesfull")
        exit
    
    soup=BeautifulSoup(page.content,'html.parser')
    print(page.content)
 
def GetMovieTheatersLink():
    # Load the xlsx file
    excel_data = pd.read_excel(r"C:\Users\eloyf\Downloads\Coordenadaslugaresculturale.xlsx")
    print("checkpint 1")
    # Read the values of the file in the dataframe
    cines = pd.DataFrame(excel_data, columns=['Nombre','Link Name']).head(10)
    # Print the content
    
    print(list(cines["Link Name"]))
    return list(cines["Link Name"])

GetMovieTheaters()