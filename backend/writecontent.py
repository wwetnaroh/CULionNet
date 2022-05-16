import boto3
import json
import time

def get_db():
    """
    get db client
    :return:
    """
    db = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id=ACCESS_ID,
                        aws_secret_access_key=ACCESS_KEY)
    return db
    
    
def load_data_into_dynamo_db(row, database):
    table = db.Table(database)
    #print("Loading into Dynamodb:{}".format(row))
    count = 0
    for i in row:
        response=table.put_item(Item=i)

def lambda_handler(event, context):
    # TODO implement
    print(event)
    
    database=event['db']
    id=event['id']
    new_comment=event['new_content']
    replier=event['replier']
    t=event['time']
   
    dynamo_db_client = get_db()
    table=dynamo_db_client.Table(database)
    
    response=table.get_item(Key={'id':id})
    thread=response['Item']
    main_content=thread['content']['main']
    topic=thread['topic']
    # comments=[]
    comments=thread['content']['comments']
    tag=replier+','+t#str(len(comments)+1)
    print(tag)
    comments[tag]=new_comment
    new_content={'main': main_content, 
            # 'topic':topic,
            # 'id':id,
            'comments':comments}
    print(new_content)
    table.update_item(
    Key={'id': id},
    UpdateExpression="SET content = :val1",
    ExpressionAttributeValues={':val1': new_content})
    
    print(thread)
    
    table2 = dynamo_db_client.Table('userProfile')
    response2=table2.get_item(Key={'userName':replier})['Item']
    print('response2', response2)
    dict={}
    dict['id']=id
    dict['topic']=topic
    thread_list = response2['thread_list']
    # thread_list.append(id)
    thread_list.append(dict)
    print('thread_list', thread_list)
    table2.update_item(
    Key={'userName':replier},
    UpdateExpression="SET thread_list = :val1",
    ExpressionAttributeValues={':val1': thread_list})
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
