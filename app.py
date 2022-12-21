from colorama import Fore
from oopClasses import History
from oopClasses import Science
from oopClasses import Music
from insertTodataBase import dataBase


import pyfiglet


class Result:
    while True:
        try:
            out = pyfiglet.figlet_format("Nigatu    Beyene")
            print(Fore.LIGHTYELLOW_EX, out, Fore.RESET)

            print(Fore.LIGHTMAGENTA_EX, "\n\n *********** WELLOCOME TO TRIVIAL GAME***********\n", Fore.RESET)
            choice = [Fore.LIGHTGREEN_EX, "1.History", Fore.RESET,
                      Fore.LIGHTYELLOW_EX, "2.Science", Fore.RESET,
                      Fore.LIGHTRED_EX, "3.Music", Fore.RESET, ]
            print("\n", Fore.LIGHTBLUE_EX, *choice, Fore.RESET, sep="   ")
            user = input("Select one of them: ")
            if user == "History":
                h = History()
                h.historyQuestion_sql()
            elif user == "Science":
                s = Science()
                s.scienceQuestion_sql()
            elif user == "Music":
                m = Music()
                m.musicQuestion_sql()

            try:
                count = input("Do you want to continue? ")
                if count == "no" or count == "n":
                    dataBase()
                    break
            except:
                break

        except ValueError:
            print("please select the correct value!!")


# Result()
