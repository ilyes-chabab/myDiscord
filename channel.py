import mysql.connector
from db import Db

class Channel:
    def __init__(self):
        self.db=Db('localhost','root','root','discord')
        self.db.connect()

    def read(self):
        self.db.cursor.execute('select * from channel')
        result=self.db.cursor.fetchall()
        print(result)
channel=Channel()
channel.read()