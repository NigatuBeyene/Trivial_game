from colorama import Fore
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
            print(Fore.LIGHTCYAN_EX, "You got ", Fore.RESET, Fore.LIGHTYELLOW_EX, score, "/", "5", "correct", Fore.RESET)


class Science(History):

    def scienceQuestion_sql(self):
        science = 'select Question, A, B, C, D, Answer from Science'
        self.cursor.execute(science)
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
            print(Fore.LIGHTCYAN_EX, "You got ", Fore.RESET, Fore.LIGHTYELLOW_EX, score, "/", "5", "correct",
                  Fore.RESET)

class Music(Science):


    def musicQuestion_sql(self):
        music = 'select Question, A, B, C, D, Answer from Music'
        self.cursor.execute(music)
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
                print(Fore.LIGHTCYAN_EX, "You got ", Fore.RESET, Fore.LIGHTYELLOW_EX, score, "/", "5", "correct",
                  Fore.RESET)
            