import mysql.connector
from db import Db

class Channel:
    def __init__(self):
        self.db=Db('ilyes-chabab.students-laplateforme.io','ilyes-chabab','Nitrate13140','ilyes-chabab_myDiscord')
        # self.db=Db('localhost','root','root','discord')
        self.db.connect()

    def createChannel(self,nameChannel):
        queries = (" insert into channel (name) values (%s) ")
        params = (nameChannel,)
        self.db.executeQuery(queries ,params)
        print(f"{nameChannel} crée")
     
    def readchannel(self):
        queries = ('select * from channel')
        return self.db.fetch(queries)
    
    def updateChannel(self,id,new_name_channel):
        queries=('UPDATE channel SET nom = %s WHERE id = %s')
        params=(new_name_channel,id)
        self.db.executeQuery(queries,params)
        print(f"le channel avec l'id {id} a été modifié en {new_name_channel}")

    def deleteChannel(self,id):
        queries=('DELETE FROM channel WHERE id = %s')
        params= (id,)
        self.db.executeQuery(queries,params)
        print(f"le channel avec l'{id} a été supprimé")  
    
    def getNameChannel(self,id_channel):
        queries = (f'select nom from channel where id = {id_channel}')
        return self.db.fetch(queries)


channel=Channel()
channel.deleteChannel(2)
print(channel.readchannel())
print(channel.getNameChannel(1))


