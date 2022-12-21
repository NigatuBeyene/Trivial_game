import pyodbc


def dataBase():
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

# data()
