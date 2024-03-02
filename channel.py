import mysql.connector
from db import Db

class Channel:
    def __init__(self):
        self.db=Db('ilyes-chabab.students-laplateforme.io','ilyes-chabab','Nitrate13140','ilyes-chabab_myDiscord')
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
        queries=('UPDATE channel SET name = %s WHERE id = %s')
        params=(new_name_channel,id)
        self.db.executeQuery(queries,params)
        print(f"le channel avec l'id {id} a été modifié en {new_name_channel}")

    def deleteChannel(self,id):
        queries=('DELETE FROM channel WHERE id = %s')
        params= (id,)
        self.db.executeQuery(queries,params)
        print(f"le channel avec l'{id} a été supprimé")  
    
    def getNameChannel(self,id_channel):
        queries = (f'select name from channel where id = {id_channel}')
        return self.db.fetch(queries)
    
    def getNameChannelWithName(self,name):
        queries = ('select id from channel where name = %s')
        params=(name,)
        return self.db.fetch(queries,params)
    
    def countAllChannel(self,id_user):
        query=("SELECT COUNT(*) FROM right_channel where id_user=%s")
        params=(id_user,)
        return self.db.fetch(query,params)[0][0]
    
    def numberChannelForUser(self,id_user):
        queries=('select id_channel from right_channel where id_user=%s')
        params=(id_user,)
        return self.db.fetch(queries,params)

channel=Channel()
print(channel.getNameChannelWithName('canal2')[::-1][0][0])


