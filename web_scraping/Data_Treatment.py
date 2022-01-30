import shutil
import os
from datetime import datetime

class DataTreatment:
    def __init__(self):
        self.download_path = "C:/Users/andre/Downloads/statusinvest-busca-avancada.csv"
        self.src_path = "C:/Users/andre/Documents/GitHub/indicadores_financeiros/repo/"

    def move(self):
        print(self.src_path)
        print('[DataTreatment] Moving the File...')
        shutil.move(self.download_path, self.src_path)
        print('[DataTreatment] File Moved Successful!')

    def rename_stock_file(self):
        print('[DataTreatment] Renaming the File...')
        os.rename(self.src_path + "/statusinvest-busca-avancada.csv", self.src_path + str(datetime.now().date()) + "-stocks.csv")
        print('[DataTreatment] File Rename Successful!')

    def rename_fii_file(self):
        print('[DataTreatment] Renaming the File...')
        os.rename(self.src_path + "/statusinvest-busca-avancada.csv", self.src_path + str(datetime.now().date()) + "-fii.csv")
        print('[DataTreatment] File Rename Successful!')