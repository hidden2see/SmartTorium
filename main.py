'''
SmarTorium
Copyright (C) 2026 Hidden2See

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
'''

from scripts.region_endpoint import NewEndPoint
from getpass import getuser
from time import sleep
import os

def main():
    print(f'''
Hello {getuser()}, welcome to SmarTorium!
Do not install this script from anywhere except the main GitHub project
Data encrypton: Enabled
Password Provided: False

Options:
1. Change endpoint region
    ''')

    option = input('''Enter the option you wanna select
''')

    try:
        option_num = int(option) 
    except ValueError:
        userDidntEnterAValidOption()

    clearLine()
    match option_num:
        case 1:
            regionChange()
        case _:
            userDidntEnterAValidOption()

        

def userDidntEnterAValidOption():
    print("You didn't enter a number valid number, try again")
    sleep(5)
    clearLine()
    main()

def clearLine():
    os.system('cls' if os.name == 'nt' else 'clear')

def operationCompleted():
    print("\n\nOperation completed successfully")
    print("You will be redericted to the main menu in 5 seconds")
    sleep(5)
    main()

def regionChange():
    clearLine()
    EndPoint = NewEndPoint()
    EndPoint.findTorrcPath()
    EndPoint.refreshTorrc()
    EndPoint.requestContry()
    EndPoint.addTheContry()
    operationCompleted()

main()