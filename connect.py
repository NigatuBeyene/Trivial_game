import pyodbc


class Connection:

    def __init__(self):
        connectSql = pyodbc.connect('Driver={SQL Server};'
                                    'Server=NIGATU\MSSQLSERVER01;'
                                    'Database=Game;'
                                    'Trusted_Connection=yes;')

        self.cursor = connectSql.cursor()