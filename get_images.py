import pandas as pd
import urllib.request
from PIL import Image
from tqdm import tqdm

class GetImages():
    def __init__(self, df):
        self.df = df

    def get_image_name(self, name: str):
        pngname = name.replace(' ', '')
        return 'data/pngs/' + pngname + '.png'

    def get_image(self, url: str, filename: str):
        urllib.request.urlretrieve(url, filename)

    def show_image(self, filename:str):
        img = Image.open(filename)
        img.show()

    def get_all_images(self):
        length = len(self.df)
        filename_col = []
        for i in tqdm(range(length)):
            filename = self.get_image_name(self.df['Title'][i])
            # print(filename)
            filename_col.append(filename)
            self.get_image(self.df['URL'][i], filename)
        self.df['png'] = filename_col
        return self.df




