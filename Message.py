import time
from db import Db

class Message:

    def __init__(self):
        self.db=Db('ilyes-chabab.students-laplateforme.io','ilyes-chabab','Nitrate13140','ilyes-chabab_myDiscord')

    def createMessage(self,message, id_user_emeteur,id_channel):
        query=('insert into message (message,id_user_emeteur,id_channel,heure) values (%s,%s,%s,%s)')
        params=(message , id_user_emeteur,id_channel,time.strftime('%H:%M:%S', time.localtime()))
        self.db.executeQuery(query , params)
    
    def readMessage(self):
        query=('select * from message ')
        return self.db.fetch(query)
    
    def updateMessage(self,message,id_message):
        query=('UPDATE message SET message = %s WHERE id = %s  ')
        params=(message ,id_message)
        self.db.executeQuery(query , params)
    
    def deleteMessage(self,id):
        queries=('DELETE FROM message WHERE id = %s')
        params= (id,)
        self.db.executeQuery(queries,params)
        
    def getMessage(self,id_user_emeteur,id_channel):
        query=('select message from message where id_user_emeteur=%s and id=%s ')
        params=(id_user_emeteur,id_channel)
        return self.db.fetch(query , params)
    
    def getHeure(self,message, id_user_emeteur,id_channel):
        query=('select heure from message where message=%s and id_user_emeteur=%s and id_channel=%s')
        params=(message, id_user_emeteur,id_channel)
        return self.db.fetch(query,params)

message1=Message()
message1.createMessage("test3",1,1)
print(message1.getHeure("test3",1,1))
print(message1.readMessage())
