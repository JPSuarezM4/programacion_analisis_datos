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
            nombre_columnas = [th.get_text(strip=True) for th in tabla.thead.find_all('th')]
            #print(tabla)
            filas = []
            for tr in tabla.tbody.find_all('tr'):
                columnas = [ td.get_text(strip=True) for td in tr.find_all('td')]
                if len(columnas) == len(nombre_columnas):
                    filas.append(columnas)
            df = pd.DataFrame(filas,columns=nombre_columnas).rename(columns = {
                'Fecha': 'fecha',
                'Abrir': 'abrir',
                'Máx.': 'max',
                'Mín.': 'min',
                'CerrarPrecio de cierre ajustado para splits.': 'cerrar',
                'Cierre ajustadoPrecio de cierre ajustado para splits y distribuciones de dividendos o plusvalías.': 'cierre_ajustado',
                'Volumen':'volumen'
            })
            df = self.convertir_numericos(df)
            print("*******************************************************************")
            print("Datos Obtenidos ")
            print("*******************************************************************")
            print(df.head())

            return df
        except Exception as err:
            print("Error en la funcion obtener_datos")
            df = pd.DataFrame()


    def convertir_numericos(self,df=pd.DataFrame()):
        df= df.copy()
        if len(df)>0:
            #for col in (df.columns):
            for col in ('abrir',	'max',	'min',	'cerrar',	'cierre_ajustado',	'volumen'):
                df[col] = (df[col]
                           .str.replace(r"\.","",regex=True)
                           .str.replace(",",'.'))

        return df



#dw = Dataweb()
#dw.get_data()
#print(dw.url)        