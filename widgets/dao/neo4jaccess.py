from . import neoconnect
from neo4jrestclient import client

db = neoconnect.NeoConnect()
def get_connection():
    connection = db.getConnection()
    return connection

def get_all_nodes():
    q = "MATCH(n) return(n)"
    connection = db.getConnection()
    results = connection.query(q,returns=(client.Node, str, client.Node))
    return results
# Create some nodes with labels
def create_one_node(**node):
    pass

def create_widget(**widget):
    print(widget)
    
def widget_process(selector,process,nodeid,attribute):
    #query = 'MATCH(n:JovianNodeDefinition{ name:'+selector+'}) return (n)';
    connection = db.getConnection()
    
#user = db.labels.create("User")
#u1 = db.nodes.create(name="Marco")
#user.add(u1)
#u2 = db.nodes.create(name="Daniela")
#user.add(u2)

#beer = db.labels.create("Beer")
#b1 = db.nodes.create(name="Punk IPA")
#b2 = db.nodes.create(name="Hoegaarden Rosee")
## You can associate a label with many nodes in one go
#beer.add(b1, b2)