from time import sleep


class Scraping:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def access_url(self):
        self.driver.get(self.url)

    def download(self):
        sleep(5)
        self.driver.find_element_by_class_name('btn-close').click()
        self.driver.find_element_by_class_name('find').click()
        sleep(3)
        self.driver.find_element_by_class_name('btn-download').click()
        sleep(3)
