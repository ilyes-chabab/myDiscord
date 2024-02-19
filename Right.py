from Channel import Channel

class Right(Channel):
    def __init__(self):
        super().__init__()
    
    def createCreator(self,id_channel,id_user):
        queries=('insert into `right` (id_channel , id_user , `right`) values (%s,%s,%s)')
        params = (id_channel,id_user,1)
        self.db.executeQuery(queries,params)
        print("créateur ajouté en tant qu'admin")

    def readRight(self):
        query=('select * from `right`')
        return self.db.fetch(query)
    
right=Right()
print(right.readRight())
