import json
from boto3.dynamodb.conditions import Key #type:ignore


##################################################################################
## PAYLOAD FOR OPERATIONS WHERE ONLY ONE ITEM IS EDITED OR OBTAINED IN A REQUEST##
##################################################################################

def create(compositekey,body,path):
    
    payload={"Item":{**body,**compositekey,"type":path.replace("/","")}}
    
    return {"Operation":"create","payload": payload}

def read(compositekey,*_):
  
    return {"Operation":"read","payload":{"Key":compositekey}}
    
def update(compositekey,body,_):
    
    payload={
                "Key":compositekey,
                "UpdateExpression":"set %s = :value" % body["updateKey"],
                "ExpressionAttributeValues":{":value": body["updateValues"]},
                "ReturnValues":"UPDATED_NEW"
            }

    return {"Operation":"update","payload":payload}

def delete(compositekey,*_):
    return {"Operation":"delete","payload":{"Key" :compositekey, "ReturnValues":"ALL_OLD"}}


##################################################################################
## PAYLOAD FOR OPERATIONS WHERE MANY ITEMS ARE EDITED OR OBTAINED IN ONE REQUEST##
##################################################################################

def readmany(_):
    
    #should receive path 
    payload={"KeyConditionExpression":Key('pk').eq("rated") & Key("sk").begins_with("movie")}
    
    return {"Operation":"readmany","payload":payload}

def createmany(body):
    
    #bad use of json? solve this
    payload={**json.loads(json.dumps(body))}

    return {"Operation":"createmany","payload": payload}
    
def updatemany(_):
    pass

def deletemany(_):
    pass


######################################
## MAP HTTP METHODS WITH OPERATIONS ##
######################################

#
one={
    "POST":create,
    "GET":read,
    "DELETE":delete,
    "PATCH":update
}

many={
    "POST":createmany,
    "GET":readmany,
    "DELETE":deletemany,
    "PATCH":updatemany
}


#XD if it were up to me I would reduce all this code to a dictionary with lambdas
