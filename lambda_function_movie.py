import json
import logging
from response import Response
from paths import routes

logger=logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    
    logger.info(event)
    
    response=Response(routes,event).result()
    
    return response

