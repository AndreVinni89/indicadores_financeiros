from time import sleep
from selenium import webdriver

class Scraping:
    def __init__(self, url):
        print('[Scrap] Initializing...')
        self.driver = webdriver.Chrome()
        self.url = url
        print('[Scrap] Initialized!')

    def run(self):
        print('[Scrap] Accessing the URL...')
        self.access_url()
        print('[Scrap] URL access successful!')

        print('[Scrap] Downnloading...')
        self.download()
        print('[Scrap] Downloaded Successful!')


    def access_url(self):
        self.driver.get(self.url)

    def download(self):
        sleep(5)
        self.driver.find_element_by_class_name('btn-close').click()
        self.driver.find_element_by_class_name('find').click()
        sleep(3)
        self.driver.find_element_by_class_name('btn-download').click()
        sleep(4)
        self.driver.close()
