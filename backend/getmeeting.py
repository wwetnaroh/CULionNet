import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print(event)
    # user='Alice'
    # date='2022-4-25-1656'
    # print(event)
    user=event['user']
    date=event['date']
    
    db=boto3.resource('dynamodb')
    table=db.Table('calendar')
    table2=db.Table('meeting')
    
    response=table.get_item(Key={'user':user})
    print('response: ', response)
    meeting=response['Item']
    mid=meeting['meeting_id']
    plan=[]
    # time=[]
    for i in mid:
        meets=table2.get_item(Key={'meeting_id':i})['Item']
        if meets['date']==date:
            plan.append(meets['time']+' '+meets['plan'])
            # time.append(meets['time'])
    
    
    return {
        'statusCode': 200,
        # 'user':user,
        'plan': plan
        # 'time':time
    }

