from neo4jrestclient.client import GraphDatabase
class NeoConnect:
    
    def __init__(self):
        print ("Init of Neoconnect")
        self.db = GraphDatabase("http://localhost:7474", username="neo4j", password="neo")
        if self.db is not None:
            print ("Connected Sucessfully!")
             
    def getConnection(self):
        return self.db
   