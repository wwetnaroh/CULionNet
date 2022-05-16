import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print(event)
    # database=event[]
    database = event['topic_name']
    # createtime=event['t']
    # title=event['title']
    
    db=boto3.resource('dynamodb')
    table=db.Table(database)
    response=table.scan()
    thread=response['Items']
    print(thread)
    # content=thread[0]['content']
    #print(content)
    # thread_name=[]
    # id=[]
    concept=[]
    
    for i in range(len(thread)):
        dict={}
        dict['thread_name']=thread[i]['thread name']
        dict['id']=thread[i]['id']
        dict['topic']=thread[i]['topic']
        concept.append(dict)
        # thread_name.append(thread[i]['thread name'])
        # id.append(thread[i]['id'])
        
        print(thread[i]['thread name'])
    
    return {
        'statusCode': 200,
        # 'thread_name': thread_name,
        'dict': concept
    }
