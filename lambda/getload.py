#from __future__ import print_function

import json
import logging
import formatload 



def getload(event,validpaths):
    path=event["path"]
    
    
    if path in validpaths:
        
        
        method=event["httpMethod"] 
        
        #health path
        if path == "/" and method=="GET":
            return {"Operation":"ping"}
        
        else:
            print(event["body"])
            body=json.loads(event["body"]) if event["body"] else None
            
            #if path is plural    
            if path[-1]=="s":
                
                #returns a dictionary based on the method/operation, ex:  {operation:"create",{"Key":compositekey}} 
                return formatload.many[method](body)
            
            else:

                #get imdbid for compistekey, i'm trying to find a better way to do this
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",path)
                imdbid=getid(event,body)
                
                compositekey={'pk': "rated", 'sk':"{}#{}".format(path.replace("/",""),imdbid)}
                print(compositekey)

                #returns a dictionary based on the method/operation, ex:  {operation:"create",{"Key":compositekey}} 
                return formatload.one[method](compositekey,body,path)
            
    return {"Error": "invalid path"}
        
def getid(event,body):
    
    if event["httpMethod"]=="GET":
        return event["queryStringParameters"]["imdbid"]
    
    return body.get("imdbid")
        
    