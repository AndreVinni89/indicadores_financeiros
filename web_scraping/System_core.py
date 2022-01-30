

from Data_Treatment import DataTreatment
from Scraping import Scraping



class System_Core:
    def __init__(self):
        self.url_stocks = 'https://statusinvest.com.br/acoes/busca-avancada'
        self.url_fiis = 'https://statusinvest.com.br/fundos-imobiliarios/busca-avancada'

    def run(self):
        """SCRAPING STOCKS"""
        scrap_stock = Scraping(self.url_stocks)
        scrap_stock.run()

        """DATA TREATMENT"""
        dt = DataTreatment()
        dt.move()
        dt.rename_stock_file()

        """SCRAPING FIIS"""
        scrap_fii = Scraping(self.url_fiis)
        scrap_fii.run()

        """DATA TREATMENT"""
        dt.move()
        dt.rename_fii_file()
