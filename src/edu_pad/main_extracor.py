from edu_pad.dataweb import DataWeb
import pandas as pd



def main_1():
    dataweb = DataWeb()
    df = dataweb.obtener_datos() 
    df = dataweb.convertir_numericos(df) # capa 2 
    df.to_csv("src/edu_pad/static/csv/data_extractor.csv", index=False)



if __name__ == "__main__":
    main_1()