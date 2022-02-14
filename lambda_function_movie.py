import boto3
import json
import logging
from custom_encoder import CustomEnconder

logger=logging.getLogger()
logger.setLevel(logging.INFO)
dynamodbTableName="RATED"
dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table(dynamodbTableName)

getMethod="GET"
postMethod="POST"
deleteMethod="DELETE"
patchMethod="PATCH"
health="/"
movie="/movie"
movies="/movies"

def lambda_handler(event,context):
    logger.info(event)
    httpMethod=event["httpMethod"]
    path=event["path"]

    if httpMethod==getMethod and path==health:
        
        response=buildResponse(200)
    
    
    elif httpMethod== getMethod and path==movie:

        response=getmovie(event["queryStringParameters"]["imdbid"])

    elif httpMethod== postMethod and path==movie:

        response=savemovie(json.loads(event["body"]))
    
    
    elif httpMethod== getMethod and path==movies:

        response=getmovies()

    elif httpMethod== postMethod and path==movies:

        response=savemovies(json.loads(event["body"]))
    
    
    elif httpMethod== patchMethod and path==movie:

        requestBody=json.loads(event["body"])
        response=modifymovie(requestBody["imdbid"],requestBody["updateKey"],requestBody["updateValues"])
    
    
    elif httpMethod== deleteMethod and path==movie:

        requestBody=json.loads(event["body"])
        response=deletemovie(requestBody["imdbid"])

    else:
        response=buildResponse(404,"not Found")

    return response
    
def buildResponse(statusCode,body=None):
    response={
        'statusCode': statusCode,
        'headers':{
            'Content-Type':'application/json',
            'Access-Control-Allow-Origin':'*'
        }
    }
    
    if body is not None:
        response["body"]=json.dumps(body, cls=CustomEnconder)
    
    return response

def getmovie(imdbid):
    try: 
        body=table.get_item(
            Key={"imdbid":imdbid}
        )
        if "Item" in body:
            return buildResponse(200,body["Item"])
        
        else:
            return buildResponse(404,{"Message":f"imdbid {imdbid} not found"})
    except:
        logger.exception("your exception here")

def savemovie(requestBody):
    try:
        table.put_item(Item=requestBody)
        body={
            'Operation':"SAVE",
            'Message':"SUCCESS",
            'Item':requestBody
        }
        return buildResponse(200,body)
    except:
        logger.exception("your exception here")
        

def getmovies():

    try:
        response=table.scan()
        result=response["Items"]
        
        while "lastEvalutatedKey" in response:
            response=table.scan(ExclusiveStartKey=response["lastEvalutatedKey"])
            result.extend(response["Items"])
        body={
            "movies":response
        }
        return buildResponse(200,body)
    except:
        logger.exception("your exception here")
    

def savemovies(requestBody):
    try:
        requestBody=json.loads(json.dumps(requestBody))
        
        for item in requestBody:
            table.put_item(Item=item)
        body={
            'Operation':"SAVE",
            'Message':"SUCCESS",
            'Item':"a lot of items"
        }
        return buildResponse(200,body)
    except:
        logger.exception("your exception here")


def modifymovie(imdbid,updateKey,updateValues):
        try:
     
            response=table.update_item(

                Key={"imdbid":imdbid},
                UpdateExpression="set %s = :value" % updateKey,
                ExpressionAttributeValues={":value":updateValues},
                ReturnValues="UPDATED_NEW")

            body={
                'Operation':"UPDATE",
                'Message':"SUCCESS",
                'UpdatedAttributes':response
            }
            return buildResponse(200,body)
        except:
            logger.exception("your exception here")


def deletemovie(imdbid):
    try:
     
        response=table.delete_item(Key={"imdbid":imdbid},ReturnValues="ALL_OLD")
            

        body={
                'Operation':"DELETE",
                'Message':"SUCCESS",
                'DeletedItem':response
            }
        return buildResponse(200,body)

    except:
        logger.exception("your exception here")