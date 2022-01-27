from selenium import webdriver

from Data_Treatment import DataTreatment
from Scraping import Scraping



class System_Core:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://statusinvest.com.br/acoes/busca-avancada'


    def run(self):
        """SCRAPING"""
        print('[Scrap] Initializing...')
        scrap = Scraping(self.driver, self.url)
        print('[Scrap] Initialized!')

        print('[Scrap] Accessing the URL...')
        scrap.access_url()
        print('[Scrap] URL access successful!')

        print('[Scrap] Downnloading...')
        scrap.download()
        print('[Scrap] Downloaded Successful!')

        """DATA TREATMENT"""
        dt = DataTreatment()
        dt.move()

