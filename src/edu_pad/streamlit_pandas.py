import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit.components.v1 import html


def cargar_datos(ruta: str, columnas_interes: list) -> pd.DataFrame:
    """Carga los datos desde un archivo CSV y selecciona columnas específicas."""
    try:
        datos = pd.read_csv(ruta)
        return datos[columnas_interes]
    except FileNotFoundError:
        st.error(f"Archivo no encontrado: {ruta}")
        return pd.DataFrame()
    except KeyError as e:
        st.error(f"Columnas no encontradas: {e}")
        return pd.DataFrame()


def mostrar_perfil(dataframe: pd.DataFrame, titulo: str):
    """Genera y muestra el reporte de perfil en Streamlit."""
    if not dataframe.empty:
        reporte = ProfileReport(dataframe, title=titulo, explorative=True)
        html(reporte.to_html(), height=700, scrolling=True)
    else:
        st.warning("No se pudo generar el reporte por falta de datos válidos.")


def main():
    st.title("Explorador de Indicadores Financieros - SOL")
    
    ruta_archivo = "src/edu_pad/static/csv/data_extractor.csv"
    columnas = ["fecha", "abrir", "max", "min", "cerrar", "cierre_ajustado", "volumen"]
    
    df_filtrado = cargar_datos(ruta_archivo, columnas)
    mostrar_perfil(df_filtrado, "Análisis de Indicador SOL")


if __name__ == "__main__":
    main()
