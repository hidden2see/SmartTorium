from pathlib import Path
import shutil
import pycountry
from time import sleep

class NewEndPoint:
    def __init__(self):
        self.path = ""
        self.region = ""
        self.errors = False

    def findTorrcPath(self):
        initial_paths = list(Path("/").rglob("torrc"))
        file_found = False

        for ipath in initial_paths:
            for search_file in ipath.parent.iterdir():
                if search_file.name == "torrc-defaults":
                    file_found = True
                    self.path = ipath
                    break
            if file_found:
                break

        if not file_found:
            raise KeyError("The program was unable to find the Torrc file, ensure Tor Browser is installed correctly. If Tor Browser is installed contact support.")

    def refreshTorrc(self):
        shutil.copyfile(self.path.with_name("torrc-defaults"), self.path)

    def requestContry(self):
        code = input("Enter the country code you wanna use for your end point connection: ")
        cleaned_code = code.strip().upper()

        if pycountry.countries.get(alpha_2=cleaned_code):
            self.region = cleaned_code
        elif pycountry.countries.get(alpha_3=cleaned_code):
            country = pycountry.countries.get(alpha_3=cleaned_code)
            self.region = country.alpha_2.upper()
        else:
            print("Please enter a valid country code")
            sleep(5)
            self.RequestContry()

    def addTheContry(self):
        with open(self.path, "a") as file:
            file.write(f'''
                ExitNodes {{{self.region}}}
                StrictNodes 1
            ''')