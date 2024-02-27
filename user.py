from Db import Db

class User():
    def __init__(self):
        pass

    def createUser(self ,email ,surname ,firstname,password):
        # Permet la création d'un utilisateur
        queries = ("""
            INSERT INTO user(email ,surname, firstname ,password ,state)
            VALUES
            (%s,%s,%s,%s,'offline')
            """)
        params = (email ,surname ,firstname, password)
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
        
    def Connection(self):
        # Modifie la colonne 'state' de l'utilisateur pour le rendre hors-ligne
        # Appel lorsqu'on appuie sur le boutton Connection
        queries = ("""
            UPDATE user
            SET state = online
            WHERE id = %s
            """)
        params = (id)
        database.executeQuery(queries, params)
        
    
    def Disconnection(self ,id):
        # Modifie la colonne 'state' de l'utilisateur pour le rendre hors-ligne
        # Appel lorsqu'on appuie sur le boutton Connection
        # if button_disconnection = True
            queries = ("""
            UPDATE user
            SET state = offline
            WHERE id = %s
            """)
            params = (id)
            database.executeQuery(queries, params)

    def checkForAccount(self ,email):
        queries = ("""
                    SELECT email FROM user
                   """)
        checkUser = database.fetch(queries)
        for user in checkUser:
            if email == user[0]:
                print("Déja créer")
                return True
    
    def checkForConnection(self):
        # Permet de renvoyer True si l'utilisateur est connecté
        queries = ("""
                    SELECT state FROM user
                   """)
        checkUser = database.fetch(queries)
        for user in checkUser:
            if "online" == user[0]:
                print("l'user est connecté")
                return True
            else:
                print("l'user est déconnecté")
    
    def get_user_id(self,email_user): 
        query = ("""
                 select id from user
                 where email=%s
                 """)
        param=(email_user,)
        return database.fetch(query,param)[0][0]
# methode qui sert a return l'id de l'user afin de l'inserer dans des channel et pour que ses message lui soit associés
    


database = Db("ilyes-chabab.students-laplateforme.io" ,"ilyes-chabab" ,"Nitrate13140" ,"ilyes-chabab_myDiscord")
user = User()
# user.createUser("oleoleg@dongz.com","cricri" ,"ovor" ,"ippon123")
print(user.get_user_id('oleoleg@dongz.com'))
# user.deleteUser(3)
# user.updateUser("boing" ,"ding" ,2)
# user.checkForAccount('dingdong@boing.com')
# user.checkForConnection()
# user.readUser()
