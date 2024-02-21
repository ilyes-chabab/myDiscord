from db import DB

class User():
    def __init__(self):
        pass

    def createUser(self ,email ,surname ,firstname ,password):
        queries = ("""
            INSERT INTO user(email ,surname, firstname, password)
            VALUES
            (%s,%s,%s,%s)
            """)
        params = (email ,surname ,firstname ,password)
        database.executeQuery(queries ,params)

    def readUser(self):
        queries = ("SELECT * FROM user")
        showdata = database.fetch(queries)
        print (showdata)
    
    def updateUser(self ,email ,surname ,firstname ,id ,id_colonne):
        queries = ("""
            UPDATE user
            SET email = %s ,surname = %s ,firstname = %s
            WHERE id = %s
            """)
        params = (email,surname,firstname,id)
        database.executeQuery(queries, params)
    
    def updatePassword(self ,password):
        queries = ("""
            UPDATE user
            SET password = %s
            WHERE id = %s
            """)
        params = (password)
        database.executeQuery(queries, params)

    
    def deleteUser(self ,id):
        queries = ("""
            DELETE FROM user
            WHERE id = (%s)
            """)
        params = [id]
        database.executeQuery(queries,params)


database = DB("localhost" ,"root" ,"root" ,"myDiscord")
user = User()
user.createUser("dingdong@boing.com","ab" ,"ayop" ,"ronda1")
# user.deleteUser(3)
# user.updateUser("boing" ,"ding" ,2)
user.readUser()
