from Db import Db

class User():
    def __init__(self):
        pass

    def createUser(self ,email ,surname ,firstname,password):
        # Permet la création d'un utilisateur
        queries = ("""
            INSERT INTO user(email ,surname, firstname ,password ,state)
            VALUES
            (%s,%s,%s,%s,offline)
            """)
        params = (email ,surname ,firstname)
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
        # Modifie la colonne 'state' de l'utilisateur pour le rendre hors-ligne
        # if button_disconnection = True
            queries = ("""
            UPDATE user
            SET state = offline
            WHERE id = %s
            """)
            params = (id)
            database.executeQuery(queries, params)
    



database = DB("ilyes-chabab.students-laplateforme.io" ,"ilyes-chabab" ,"Nitrate13140" ,"ilyes-chabab_myDiscord")
user = User()
# user.createUser("oleoleg@dongz.com","cricri" ,"ovor")
# user.deleteUser(3)
# user.updateUser("boing" ,"ding" ,2)
user.readUser()
