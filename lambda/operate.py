from __future__ import print_function
import boto3 #type:ignore
import logging


logger=logging.getLogger()
logger.setLevel(logging.INFO)


print('Loading function')



def operator(load,table):
    '''Provide an load that contains the following keys:
      - operation: one of the operations in the operations dict below
      - table: required for operations that interact with DynamoDB
      - payload: a parameter to pass to the operation being performed
    '''
    
    
    if "Error" in load:
        print("Error",load)
        return load
        
    operation = load['Operation']
    

    if table:
        dynamo = boto3.resource('dynamodb').Table(table)

    operations = {
        'create': lambda x: dynamo.put_item(**x),
        'read': lambda x: dynamo.get_item(**x),
        'update': lambda x: dynamo.update_item(**x),
        'delete': lambda x: dynamo.delete_item(**x),
        'readmany': lambda x: dynamo.query(**x),
        'createmany':lambda x:map(dynamo.put_item(**x),x), #improve using batchwrite with 25
        "updatemany":lambda x: x,#implement
        'deletemany':lambda x: x,#implement
        'echo': lambda x: x,
        'ping': lambda x: 'pong'
    }

    if operation in operations:
        return operations[operation](load.get('payload'))
    else:
        raise ValueError('Unrecognized operation "{}"'.format(operation))
    
