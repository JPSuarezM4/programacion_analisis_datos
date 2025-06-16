import pandas as pd
import requests
from bs4 import BeautifulSoup


class YahooFinanceScraper:
    """
    Clase para extraer y procesar datos históricos desde Yahoo Finance.
    """

    def __init__(self, ticker="SOL-USD"):
        self.url = f"https://es.finance.yahoo.com/quote/{ticker}/history/"
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/114.0.0.0 Safari/537.36"
            )
        }

    def extraer_datos(self) -> pd.DataFrame:
        """Realiza la solicitud HTTP y parsea los datos en una tabla de pandas."""
        try:
            respuesta = requests.get(self.url, headers=self.headers)
            respuesta.raise_for_status()

            soup = BeautifulSoup(respuesta.text, "html.parser")
            tabla = soup.select_one('div[data-testid="history-table"] table')

            encabezados = [th.get_text(strip=True) for th in tabla.thead.find_all("th")]
            registros = []

            for fila in tabla.tbody.find_all("tr"):
                celdas = [td.get_text(strip=True) for td in fila.find_all("td")]
                if len(celdas) == len(encabezados):
                    registros.append(celdas)

            df = pd.DataFrame(registros, columns=encabezados)
            return self._procesar_dataframe(df)

        except Exception as e:
            print(f"❌ Error al extraer los datos: {e}")
            return pd.DataFrame()

    def _procesar_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Renombra columnas y convierte datos numéricos al formato adecuado."""
        nombres = {
            'Fecha': 'fecha',
            'Abrir': 'abrir',
            'Máx.': 'max',
            'Mín.': 'min',
            'CerrarPrecio de cierre ajustado para splits.': 'cerrar',
            'Cierre ajustadoPrecio de cierre ajustado para splits y distribuciones de dividendos o plusvalías.': 'cierre_ajustado',
            'Volumen': 'volumen'
        }

        df = df.rename(columns=nombres)

        for campo in ['abrir', 'max', 'min', 'cerrar', 'cierre_ajustado', 'volumen']:
            if campo in df.columns:
                df[campo] = (
                    df[campo]
                    .str.replace(".", "", regex=False)
                    .str.replace(",", ".", regex=False)
                    .astype(str)
                )

        print("✅ Datos extraídos exitosamente:")
        print(df.head())
        return df


# Si deseas probarlo localmente:
# scraper = YahooFinanceScraper()
# datos = scraper.extraer_datos()
