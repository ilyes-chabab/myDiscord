from channel import Channel

class Right(Channel):
    def __init__(self):
        super().__init__()
    
    def createCreator(self,id_channel,id_user):
        queries=('insert into right_channel (id_channel , id_user , right_number ) values (%s,%s,%s)')
        params = (id_channel,id_user,1)#'''1 car il est admin '''
        self.db.executeQuery(queries,params)
        print("créateur ajouté en tant qu'admin")

    def readRight(self):
        query=('select * from right_channel')
        return self.db.fetch(query)
    
    def updateRight(self,new_right,id_channel,id_user):
        queries=('UPDATE right_channel SET `right` = %s WHERE id_channel = %s and id_user= %s')
        params=(new_right,id_channel,id_user)
        self.db.executeQuery(queries,params)
    
    def addUser(self,id_channel,id_user):
        queries=('insert into right_channel (id_channel,id_user,right_number) values (%s,%s,%s)')
        params=(id_channel,id_user,2 ) #2 car il est membre 
        self.db.executeQuery(queries,params)
    
    def deleteUser(self,id_channel,id_user):
        queries=("delete from right_channel where id_channel = %s and id_user = %s")
        params=(id_channel,id_user)
        self.db.fetch(queries,params)
        
        

    
right=Right()
print(right.readRight())
right.addUser(3,2)
