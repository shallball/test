#coding:gbk
import sqlite3
class DataOutput(object):
    def __init__(self):
        self.cx = sqlite3.connect("Movie.db")
        self.create_table('Movie')

    def create_table(self,table_name):

        values = '''
        id integer primary key autoincrement,
        Name varchar(20) NOT NULL,
        Directors varchar(40) NOT NULL,
        Stars varchar(40) NOT NULL,
        Category varchar(20) NOT NULL,
        Year varchar(10) NOT NULL,
        Rate varchar(10) NOT NULL,
        Runtime varchar(20) NOT NULL,
        Ticket varchar(40) NOT NULL
       
        '''
        self.cx.execute('CREATE TABLE IF NOT EXISTS  %s( %s ) '%(table_name,values))




    def output_db(self,table_name,data):
        value=[v for v in data.values()]
        self.cx.execute("INSERT INTO %s (Name,Directors,"
                        "Stars,Category,Year,Rate,Runtime,Ticket"
                        ") VALUES (?,?,?,?,?,?,?,?) "
                        ""%table_name,value)
        self.cx.commit()
    def close_db(self):
        self.cx.close()
