import pandas as pd

class ReadXLSX():
    def __init__(self, path):
        self.path = path
        self.df = pd.read_excel(self.path)
        self.clean_df()

    def get_columns(self):
        return list(self.df.columns)

    def clean_df(self):
        cols = self.get_columns()
        for col in cols:
            if col.startswith("Unnamed"):
                self.df = self.df.drop(columns=[col])

    def print_df(self, num_rows):
        print(self.df.head(num_rows))

# obj = ReadXLSX('data/artworks.xlsx')


