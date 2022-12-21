import pyodbc
from colorama import Fore
from insertTodataBase import dataBase


class History():

    def historyQuestion_sql(self):

        connectSql = pyodbc.connect('Driver={SQL Server};'
                                    'Server=NIGATU\MSSQLSERVER01;'
                                    'Database=Game;'
                                    'Trusted_Connection=yes;')
        history = 'select Question, A, B, C, D, Answer from History'
        cursor = connectSql.cursor()
        cursor.execute(history)
        score = 0
        for choice in cursor:
            print(choice[0])
            print(choice[1])
            print(choice[2])
            print(choice[3])
            print(choice[4])

            answer = input("choice one of them: ")

            if answer == choice[5]:
                score += 1
            print("you got ", str(score), "/", "5", "correct")


class Science(History):

    def scienceQuestion_sql(self):

        connectSql = pyodbc.connect('Driver={SQL Server};'
                                    'Server=NIGATU\MSSQLSERVER01;'
                                    'Database=Game;'
                                    'Trusted_Connection=yes;')

        science = 'select Question, A, B, C, D, Answer from Science'
        cursor = connectSql.cursor()
        cursor.execute(science)
        score = 0
        for choice in cursor:
            print(choice[0])
            print(choice[1])
            print(choice[2])
            print(choice[3])
            print(choice[4])

            answer = input("choice one of them: ")

            if answer == choice[5]:
                score += 1
            print("you got ", str(score), "/", "5", "correct")


class Music(Science):

    def musicQuestion_sql(self):

        connectSql = pyodbc.connect('Driver={SQL Server};'
                                    'Server=NIGATU\MSSQLSERVER01;'
                                    'Database=Game;'
                                    'Trusted_Connection=yes;')

        science = 'select Question, A, B, C, D, Answer from Music'
        cursor = connectSql.cursor()
        cursor.execute(science)
        score = 0
        for choice in cursor:
            print(choice[0])
            print(choice[1])
            print(choice[2])
            print(choice[3])
            print(choice[4])

            answer = input("choice one of them: ")

            if answer == choice[5]:
                score += 1
            print("you got ", str(score), "/", "5", "correct")


class Result(Science):
    while True:
        try:
            print(Fore.GREEN, "\n\nWELLOCOME TO TRIVIAL GAME\n", Fore.RESET)
            choice = ["History", "Science", "Music"]
            print("\n", Fore.LIGHTBLUE_EX, *choice, Fore.RESET, sep="   ")
            user = input("Select one of them: ")

            if user == choice[0]:
                h = History()
                h.historyQuestion_sql()

            elif user == choice[1]:
                s = Science()
                s.scienceQuestion_sql()

            elif user == choice[2]:
                m = Music()
                m.musicQuestion_sql()
                # m.run_score()

            try:
                count = input("Do you want to continue? ")
                if count == "no" or count == "n":
                    dataBase()
                    break
            except:
                break

        except ValueError:
            print("please select the correct value!!")


Result()