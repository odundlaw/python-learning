import os;
from random import randint
from re import match

class RockPaper():

    def logon(self):
        dir = "new folder"
        parent_directory = os.getcwd()
        path = os.path.join(parent_directory, dir)

        os.mkdir(path)
        os.
        print(f"your current working directory is {dir}")

rockPaper = RockPaper();
rockPaper.logon();