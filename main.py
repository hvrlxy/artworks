import pandas as pd
from get_images import *
from read_xlxs import *
from show_images import *

artworks_df = ReadXLSX('data/artworks.xlsx').df
img = GetImages(artworks_df)
artworks_df = img.get_all_images()

quiz = ShowImage(artworks_df)
quiz.show_all()




