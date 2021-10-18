from PIL import Image
import random
from rich.console import Console
import time
import subprocess
import keyboard

class ShowImage():
    def __init__(self, df):
        self.df = df
        self.size = len(self.df)
        self.is_chosen = [False for i in range(self.size)]
        self.console = Console()

    def reset_chosen(self):
        self.is_chosen = [False for i in range(self.size)]

    def is_complete(self):
        if self.is_chosen.count(False) == 0:
            return True
        else:
            return False

    def pick_random(self):
        choice =  random.randrange(0, self.size)
        while (self.is_chosen[choice] == True):
            choice =  random.randrange(0, self.size)
        self.is_chosen[choice] == True
        return choice

    def show_image(self, filename:str):
        img = Image.open(filename)
        img.show()

    def print_info(self, choice):
        self.console.print("Name: [bold red]" + self.df['Title'][choice])
        self.console.print("Artist: [bold red]" + self.df['Artist'][choice])
        self.console.print("Date: [bold red]" + str(self.df['Date'][choice]))
        if self.df['asterisk'][choice] == 'yes':
            self.console.print("Location: [bold red]" + str(self.df['Location'][choice]))
        else:
            self.console.print("Location: [bold red]" + "N/A")
        self.console.print("-" * 50)

    def show_next(self):
        if self.is_complete():
            return
        choice = self.pick_random()
        self.show_image(self.df['png'][choice])
        self.is_chosen[choice] = True
        return choice

    def show_all(self):
        self.reset_chosen()
        while not self.is_complete():
            choice = self.show_next()
            input1 = input()
            self.print_info(choice)



