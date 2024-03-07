from Db import Db

class User():
    def __init__(self):
        pass

    def createUser(email ,surname ,firstname,password):
        # Permet la création d'un utilisateur
        queries = ("""
            INSERT INTO user(email ,surname, firstname ,password ,state)
            VALUES
            (%s,%s,%s,%s,'offline')
            """)
        params = (email ,surname ,firstname, password)
        db.executeQuery(queries ,params)

    def readUser(self):
        # Permet l'affichage du contenu de la table user dans le terminal
        queries = ("SELECT * FROM user")
        showdata = db.fetch(queries)
        print (showdata)
    
    def updateUser(self ,email ,surname ,firstname ,id ,id_colonne):
        # Permet de modifier les informations d'un utilisateur
        queries = ("""
            UPDATE user
            SET email = %s ,surname = %s ,firstname = %s
            WHERE id = %s
            """)
        params = (email,surname,firstname,id,id_colonne)
        db.executeQuery(queries, params)
    
    def updatePassword(self ,password):
        # Permet de modifier le mot de passe d'un utilisateur
        queries = ("""
            UPDATE user
            SET password = %s
            WHERE id = %s
            """)
        params = (password)
        db.executeQuery(queries, params)

    
    def deleteUser(self ,id):
        # Permet de supprimer un utilisateur
        queries = ("""
            DELETE FROM user
            WHERE id = (%s)
            """)
        params = [id]
        db.executeQuery(queries,params)
        
    def Connection(self):
        # Modifie la colonne 'state' de l'utilisateur pour le rendre hors-ligne
        # Appel lorsqu'on appuie sur le boutton Connection
        queries = ("""
            UPDATE user
            SET state = online
            WHERE id = %s
            """)
        params = (id)
        db.executeQuery(queries, params)
        
    
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
            db.executeQuery(queries, params)

    def checkForAccount(username):
        queries = ("""
                    SELECT email FROM user
                   """)
        checkUser = db.fetch(queries)
        for user in checkUser:
            if username == user[0]:
                return True
    
    def checkForPassword(username):
        queries = ("""
                SELECT password FROM user
                WHERE email = %s
                """)
        params = [username]
        checkPassword = db.fetch(queries, params)[0][0]
        return checkPassword
    
    def checkForConnection(self):
        # Permet de renvoyer True si l'utilisateur est connecté
        queries = ("""
                    SELECT state FROM user
                   """)
        checkUser = db.fetch(queries)
        for user in checkUser:
            if "online" == user[0]:
                print("l'user est connecté")
                return True
            else:
                print("l'user est déconnecté")

# methode qui sert a return l'id de l'user afin de l'inserer dans des channel et pour que ses message lui soit associés
                   
    def get_user_id(email): 
        query = ("""
                 select id from user
                 where email = (%s)
                 """)
        params = [email]
        return db.fetch(query,params)[0][0]

    


db = Db("ilyes-chabab.students-laplateforme.io" ,"ilyes-chabab" ,"Nitrate13140" ,"ilyes-chabab_myDiscord")
user = User()
# user.createUser("oleoleg@dongz.com","cricri" ,"ovor" ,"ippon123")
# print(user.get_user_id('oleoleg@dongz.com'))
user.deleteUser(11)
# user.updateUser("boing" ,"ding" ,2)
# print (user.checkForAccount('dingdong@boing.com'))
# user.checkForConnection()
# print (user.checkForPassword('dingdong@boing.com'))
# print(user.readUser())