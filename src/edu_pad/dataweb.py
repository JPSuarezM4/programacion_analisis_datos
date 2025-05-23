import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime



class Dataweb:
    """
    Class to handle data web operations.
    """

    def __init__(self):
        """
        Initialize the Dataweb class with the given URL.

        Args:
            dataweb_url (str): The URL of the data web.
        """
        self.url = 'https://es.finance.yahoo.com/quote/SOL-USD/history/'

    def get_data(self):
        try:
            # URL | Cabeceras
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
                }
            
            response = requests.get(self.url, headers=headers)
            if response.status_code != 200:
                print(f"Failed to retrieve data: {response.status_code}")
            #print(response.text)
            soup = BeautifulSoup(response.text, 'html.parser')
            tabla = soup.select_one('div[data-testid="history-table"] table')
            print(tabla)

        except Exception as e:
            print(f"An error occurred: {e}")
   

dw = Dataweb()
dw.get_data()
#print(dw.url)        