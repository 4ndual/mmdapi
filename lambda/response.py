from email.quoprimime import body_check
import json
import logging
from custom_encoder import CustomEnconder
logger=logging.getLogger()
logger.setLevel(logging.INFO)

def buildResponse(statusCode,body=None):
    logger.info(body)
    print(body)
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


"""

class Response:
    
    def __init__(self, handler, event):
        self.handler=handler
        self.event=event
        self.httpMethod=event["httpMethod"].lower()
        self.path=event["path"].replace("/","")
        self.response = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body':{"Message": f"Hello World"}
        }

    def result(self):
        
        #if pathis"/" return default body and status else:
        if self.path != "":
            
            #1 get  path in Path class ex: Path.Movie 
            #2 call buildResponse with the path ex: buildResponse(Path.Movie)
            self.buildResponse(self.handler.get(self.path,"keyerror"))
            
        logger.info(self.response)
        self.response["body"] =json.dumps(self.response["body"], cls=CustomEnconder)

        return self.response
            
    def buildResponse(self,pathObj):
        
        #path.httpMethod(event) ex: Movie.get(event)
        result=getattr(pathObj, self.httpMethod, self.respondError)(self.event)
        logger.info(pathObj)
        self.response["statusCode"]=result[0]
        self.response["body"] =result[1]

    def respondError(self,event=None):
        self.response["statusCode"]=404
        self.response["body"] ={"Error": f"the path or method you are using is not valid {self.path}, {self.httpMethod}"}
        
    
"""