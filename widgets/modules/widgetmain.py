
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
print(sys.path)

import dao.neo4jaccess
from importlib import import_module

def get_all_nodes():
    results=dao.neo4jaccess.get_all_nodes()
    for r in results:
        print("(%s))" % (r[0]))
    
    return results   
    
def create(name,appliesTo,process):
    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'widget'+name+'wid.py'))
    
    widgetfile = open(filename,"w")
    widgetfile.write('import dao \n')
    widgetfile.write('from dao import neo4jaccess\n\n')
    widgetfile.write('db = dao.neo4jaccess.get_connection()\n')
    widgetfile.write('def widget_process(nodeid):\n')
    widgetfile.write('    ')
    widgetfile.write(process)
    widgetfile.close()
    
def widget_process(widget,nodeid,modulename):
    widgetfilename = os.path.abspath(os.path.join(os.path.dirname(__file__), widget))
    code = open(widgetfilename,"r")
    print(code.read())
    exec(code.read())
    widgetmodule = import_module(modulename)
    getattr(widgetmodule,"widget_process")(nodeid)
    return None
    #dao.neo4jaccess.widget_process('Mechanical Part','set n.revision = n.revision++',nodeid,attribute)