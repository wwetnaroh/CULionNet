import boto3
#from configs import ACCESS_KEY, ACCESS_ID
#from constants import SUPPORTED_CUISINES, DYNAMO_DB_TABLE_NAME
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

def set_mid(plan,t):
    if len(plan)<5:
        plan+='*'*(5-len(plan))
    id=plan[:5]+str(t)+str(int(time.time()))
    return id
    
def lambda_handler(event, context):
    
    # database='calendar'
    print(event)
    user=event['user']
    date=event['date']
    time=event['time']
    plan=event['description']
    
   
   
    dynamo_db_client = get_db()
    table=dynamo_db_client.Table('calendar')
    response=table.scan()
    meeting=response['Items']
    print(meeting)
    
   
    table2=dynamo_db_client.Table('meeting')
    
    
 
    a=set_mid(plan,time)
    mid=[a]
    try:
        response=table.get_item(Key={'user':user})
        # response=table.get_item(Key={'user':user})
        old_meetingid=response['Item']['meeting_id']
        print(old_meetingid)
        
        new_meetingid=old_meetingid+mid
        table.update_item(
        Key={'user': user},
        UpdateExpression="SET meeting_id = :val1",
        ExpressionAttributeValues={':val1': new_meetingid})
    except:
        print('new user!')
        table.put_item(
        Item={
            'user': user,
            'meeting_id':mid
        })
    print(len(mid))
   
    table2.put_item(
        Item={
            'meeting_id':a,
            'date':date,
            'time':time,
            'plan':plan
        })
        
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
