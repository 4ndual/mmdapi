import json
import logging
import boto3
from boto3.dynamodb.conditions import Key

logger=logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("showlists")


body = {
            'Operation': "",
            'Message': "SUCCESS",
            'Item': ""
        }   

class Movie:
    
    def get(event):
        
        try:
            imdbid = event["queryStringParameters"]["imdbid"]
            
            body = table.get_item(
                Key={'pk': "rated", 'sk': "movie#"+imdbid}
            )
            
            return [200, body["Item"]]
        
        except:
            
            logger.exception("Error gettings items from table")
            return [404, {"Message": f'imdbid not found'}]
        
        
    
    def post( event):
        body["Operation"] = "SAVE"
        try:
            
            requestBody = json.loads(event["body"])
            requestBody["pk"]="rated"
            requestBody["sk"]="movie#"+requestBody["imdbid"]
            requestBody["type"]="movie"
            
            table.put_item(Item=requestBody)
            
            body['Message']= "SUCCESS"
            body["Item"] = requestBody
            
            return [200, body]
        
        except:
            logger.exception("your exception here")
            body["Message"] = "FAIL"
            return [404, body]
    
    def patch( event):
        body["Operation"] = "UPDATE"
        try:
            requestBody = json.loads(event["body"])
            
            response = table.update_item(
                Key={'pk': "rated", 'sk': "movie#"+requestBody["imdbid"]},
                UpdateExpression="set %s = :value" % requestBody["updateKey"],
                ExpressionAttributeValues={":value": requestBody["updateValues"]},
                ReturnValues="UPDATED_NEW"
            )
            
            body['Message']= "SUCCESS"
            body["Item"] = response
            
            return [200, body]
        
        except:
            logger.exception("your exception here")
            body["Message"] = "FAIL"
            return [404, body]
    
    def delete( event):
        
        body["Operation"] = "DELETE"
        
        try:
            requestBody = json.loads(event["body"])
            sk ="movie#"+requestBody["imdbid"]
            response = table.delete_item(
                Key={'pk': "rated", 'sk': sk}, ReturnValues="ALL_OLD")
            body["Item"] = response
            body['Message']= "SUCCESS"
            return [200, body]
        except:
            logger.exception("your exception here")
            body["Message"] = "FAIL"
            return [404, body]
            
class Movies:

    def post(event):
        try:
            requestBody=json.loads(event["body"])
            requestBody = json.loads(json.dumps(requestBody))
            for item in requestBody:
                table.put_item(Item=item)
            
            return [200, body]
        except:
            logger.exception("your exception here")
            return [404, body]
            
    def get(event):

        try:
            response=table.query(
            KeyConditionExpression=Key('pk').eq("rated") & Key("sk").begins_with("movie")
        )

            result=response["Items"]

            while "lastEvalutatedKey" in response:
                response=table.scan(ExclusiveStartKey=response["lastEvalutatedKey"])
                result.extend(response["Items"])
            body={
                "movies":response
            }
            return [200, body]
            
        except:
            logger.exception("your exception here")
            return [404, body]
            
            
routes={"movie": Movie,"movies":Movies}
    