from db import DB

class User():
    def __init__(self):
        pass

    def createUser(self ,email ,surname ,firstname ,password):
        # Permet la création d'un utilisateur
        queries = ("""
            INSERT INTO user(email ,surname, firstname)
            VALUES
            (%s,%s,%s)
            """)
        params = (email ,surname ,firstname)
        database.executeQuery(queries ,params)
    
    def createPassword(self, password):
        queries = ("""
            INSERT INTO user(password)
            VALUES
            (%s)
            """)
        params = (password)
        database.executeQuery(queries ,params)

    def readUser(self):
        # Permet l'affichage du contenu de la table user dans le terminal
        queries = ("SELECT * FROM user")
        showdata = database.fetch(queries)
        print (showdata)
    
    def updateUser(self ,email ,surname ,firstname ,id ,id_colonne):
        # Permet de modifier les informations d'un utilisateur
        queries = ("""
            UPDATE user
            SET email = %s ,surname = %s ,firstname = %s
            WHERE id = %s
            """)
        params = (email,surname,firstname,id,id_colonne)
        database.executeQuery(queries, params)
    
    def updatePassword(self ,password):
        # Permet de modifier le mot de passe d'un utilisateur
        queries = ("""
            UPDATE user
            SET password = %s
            WHERE id = %s
            """)
        params = (password)
        database.executeQuery(queries, params)

    
    def deleteUser(self ,id):
        # Permet de supprimer un utilisateur
        queries = ("""
            DELETE FROM user
            WHERE id = (%s)
            """)
        params = [id]
        database.executeQuery(queries,params)
    
    def checkForConnection(self):
        # Permet de renvoyer True si l'utilisateur est connecté
        pass
        Online = True
    
    def Disconnection(self ,id):
        # Permet de renvoyer True si l'utilisateur appuie sur le boutton True
        # if button_disconnection = True
            queries = ("""
            UPDATE user
            SET state = False
            WHERE id = %s
            """)
            params = (id)
            database.executeQuery(queries, params) 



database = DB("ilyes-chabab.students-laplateforme.io" ,"ilyes-chabab" ,"Nitrate13140" ,"ilyes-chabab_myDiscord")
user = User()
# user.createUser("dingdong@boing.com","ab" ,"ayop" ,"ronda1")
# user.deleteUser(3)
# user.updateUser("boing" ,"ding" ,2)
user.readUser()
