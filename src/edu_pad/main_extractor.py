from src.edu_pad.dataweb import YahooFinanceScraper
import pandas as pd



def main_1():
    scraper = YahooFinanceScraper()
    df = scraper.extraer_datos()
    df.to_csv("src/edu_pad/static/csv/data_extractor.csv", index=False)




if __name__ == "__main__":
    main_1()