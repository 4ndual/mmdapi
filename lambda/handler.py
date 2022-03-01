#from __future__ import print_function #WTF IS THIS
from operate import operator
from response import buildResponse
from getload import getload




def main(event, context):
    '''
        - operation: create, read, update, delete  one or many
        - payload: a parameter to pass to the operation being performed
        - load: a dictionary with the payload and the operation {operation:"",payload:""}
    '''
    #print("Received event: " + json.dumps(event, indent=2))
    load=getload(event,["/movie","/serie","/movies","/series","/"])
    response=buildResponse(200,operator(load,"showlists"))
    return response
    

    
#finish build response
#build yaml
#debug
#improve

