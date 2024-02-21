import mysql.connector

class DB:
    def __init__(self ,host ,user ,password ,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    
    def connect(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )
        self.cursor = self.connection.cursor()
    
    
    def disconnect(self):
        self.connection.close()
    
    def executeQuery(self ,query ,params=None):
        self.connect()
        self.cursor.execute(query ,params or ())
        self.connection.commit()
        self.disconnect()
    
    def fetch(self ,query ,params=None):
        self.connect()
        self.cursor.execute(query ,params or ())
        result = self.cursor.fetchall()
        self.disconnect()
        return result
    
    def checkStock(self):
        queries = ("""
            SELECT quantity FROM product
                   """)
        self.connect()
        self.cursor.execute(queries)
        result = self.cursor.fetchall()
        quantity = 0
        for quantité in result:
            if quantity == quantité[0]:
                print("Produit en rupture de stock")
            else: 
                print("Produit en stock") 

    def checkProduit(self):
        queries = "select * from product"
        self.connect()
        select = self.cursor.execute(queries)
        return select