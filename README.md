# Trivial_game
### What is Trivial game?


>A trivia game or competition is one where the competitors are asked questions 
about interesting but unimportant facts in many subjects. a pub trivia game. 
Collins English Dictionary.
___________________________________________________



### HOW TO PLAY:

>>Generally, most trivia games are for a set number of rounds, including 
open-ended and 
multiple-choice questions with a maximum number of points that teams can earn on all the questions.
Teams switch answer sheets after each round to score one another. Teams with the highest number of points win.
_________________________________________________

# Trivia_game code using OOP: 

>from colorama import Fore
from connect import Connection


class History(Connection):
    def __init__(self):
        super().__init__()

    def historyQuestion_sql(self):
        history = 'select Question, A, B, C, D, Answer from History'
        self.cursor.execute(history)
        score = 0
        for choice in self.cursor:
            print(Fore.LIGHTGREEN_EX, choice[0], Fore.RESET)
            print(Fore.LIGHTBLUE_EX, choice[1], Fore.RESET)
            print(Fore.LIGHTBLUE_EX, choice[2], Fore.RESET)
            print(Fore.LIGHTBLUE_EX, choice[3], Fore.RESET)
            print(Fore.LIGHTBLUE_EX, choice[4], Fore.RESET)
            answer = input("Multiple question, Choose the corrct answer: ")
            if answer == choice[5]:
                score += 1
            print(Fore.LIGHTCYAN_EX, "You got ", Fore.RESET,  Fore.LIGHTYELLOW_EX, score, "/", "5", "correct", Fore.RESET)


class Science(History):

    def scienceQuestion_sql(self):
        science = 'select Question, A, B, C, D, Answer from Science'
        self.cursor.execute(science)
        score = 0
        for choice in self.cursor:
            print(Fore.LIGHTMAGENTA_EX, choice[0], Fore.RESET)
            print(Fore.LIGHTBLUE_EX, choice[1], Fore.RESET)
            print(Fore.LIGHTBLUE_EX, choice[2], Fore.RESET)
            print(Fore.LIGHTBLUE_EX, choice[3], Fore.RESET)
            print(Fore.LIGHTBLUE_EX, choice[4], Fore.RESET)
            answer = input("choice one of them: ")
            if answer == choice[5]:
                score += 1
            print(Fore.LIGHTCYAN_EX, "You got", Fore.RESET, Fore.LIGHTYELLOW_EX, score, "/", "5", "correct", Fore.RESET)


class Music(Science):

    def musicQuestion_sql(self):
        science = 'select Question, A, B, C, D, Answer from Music'
        self.cursor.execute(science)
        score = 0
        for choice in self.cursor:
            print(Fore.LIGHTCYAN_EX, choice[0], Fore.RESET)
            print(Fore.LIGHTBLUE_EX, choice[1], Fore.RESET)
            print(Fore.LIGHTBLUE_EX, choice[2], Fore.RESET)
            print(Fore.LIGHTBLUE_EX, choice[3], Fore.RESET)
            print(Fore.LIGHTBLUE_EX, choice[4], Fore.RESET)

            answer = input("choice one of them: ")

            if answer == choice[5]:
                score += 1
            print("you got ", str(score), "/", "5", "correct")


import pyodbc


def data():
    connect = pyodbc.connect('Driver={SQL Server};'
                             'Server=NIGATU\MSSQLSERVER01;'
                             'Database=Game;'
                             'Trusted_Connection=yes;')

    cursor = connect.cursor()

    PersonID = input("Please enter your ID: ")
    Full_name = input("Write your Full_name: ")
    Grade = input("Enter your score: ")
    cursor.execute("INSERT INTO Game_table (PersonID, Full_name, Grade)"
                   "VALUES(?,?,?)", (PersonID, Full_name, Grade))
    connect.commit()

    cursor.commit()
    cursor.close()
    connect.close()



import pyodbc


class Connection:

    def __init__(self):
        connectSql = pyodbc.connect('Driver={SQL Server};'
                                    'Server=NIGATU\MSSQLSERVER01;'
                                    'Database=Game;'
                                    'Trusted_Connection=yes;')

        self.cursor = connectSql.cursor()



from colorama import Fore
from oopClasses import History
from oopClasses import Science
from oopClasses import Music
from insertTodataBase import data


class Result(Science):
    while True:
        try:
            print(Fore.LIGHTMAGENTA_EX, "\n\n WELLOCOME TO TRIVIAL GAME\n", Fore.RESET)
            choice = [Fore.LIGHTGREEN_EX, "History", Fore.RESET,
                      Fore.LIGHTYELLOW_EX, "Science", Fore.RESET,
                      Fore.LIGHTRED_EX, "Music", Fore.RESET, ]
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
            try:
                count = input("Do you want to continue? ")
                if count == "no" or count == "n":
                    data()
                    break
            except:
                break

        except ValueError:
            print("please select the correct value!!")


Result()

REFERENCE: Google, YouTube

TECHNOLOGY: Pycharm, Github

AUTHOR INFO: https://github.com/NigatuBeyene/Trivial_game

Linkedin = https://www.linkedin.com/in/nigatu-beyene-404158249