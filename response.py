import json
from custom_encoder import CustomEnconder

class Response:
    
    def __init__(self, handler, event):
        self.handler=handler
        self.event=event
        self.httpMethod=event["httpMethod"].lower()
        self.path=event["path"].replace("/","").capitalize()
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
            
            #1 get  key in path dictionary: path["movie"] 
            #2 call buildResponse with the path ex: buildResponse(path["movie"])
            self.buildResponse(self.handler.get(self.path,"Error"))

        return self.response
            
    def buildResponse(self,pathObj):
        
        #path.httpMethod(event) ex: Movie.get(event)
        result=getattr(pathObj, self.httpMethod, self.respondError)(self.event)
        
        self.response["statusCode"]=result[0]
        self.response["body"] = json.dumps(result[1], cls=CustomEnconder)

    def respondError(self,event):
        self.response["statusCode"]=404
        self.response["body"] ={"Error": f"the path or method you are using is not valid {self.path}, {self.httpMethod}"}
        

    

    