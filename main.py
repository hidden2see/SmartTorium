from scripts.region_endpoint import NewEndPoint
from getpass import getuser
from time import sleep
import os

def Main():
    print(f'''
Hello {getuser()}, welcome to SmarTorium!
Do not install this script from anywhere except the main GitHub project

Options:
1. Change endpoint region
    ''')

    option = input('''Enter the option you wanna select
''')

    try:
        option_num = int(option) 
    except ValueError:
        UserDidntEnterAValidOption()

    ClearLine()
    match option_num:
        case 1:
            RegionChange()
        case _:
            UserDidntEnterAValidOption()

        

def UserDidntEnterAValidOption():
    print("You didn't enter a number valid number, try again")
    sleep(5)
    ClearLine()
    Main()

def ClearLine():
    os.system('cls' if os.name == 'nt' else 'clear')

def OperationCompleted():
    print("\n\nOperation completed successfully")
    print("You will be redericted to the main menu in 5 seconds")
    sleep(5)
    Main()

def RegionChange():
    ClearLine()
    EndPoint = NewEndPoint()
    EndPoint.FindTorrcPath()
    EndPoint.RefreshTorrc()
    EndPoint.RequestContry()
    EndPoint.AddTheContry()
    OperationCompleted()

Main()