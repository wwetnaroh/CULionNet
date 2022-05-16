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
    
    
def load_data_into_dynamo_db(row, database):
    table = db.Table(database)
    #print("Loading into Dynamodb:{}".format(row))
    count = 0
    for i in row:
        response=table.put_item(Item=i)


def lambda_handler(event, context):
   
    
    # course='COMS6998'
    # # code='COMS6998'
    # user='Jerry'
    # comment='very good'
    # gpa='4.0'
    # workload='3.8'
    # assessment_type='report'
    # semester='2021fall'
    # time=event[]
    dynamo_db_client = get_db()
    table=dynamo_db_client.Table('course_list')
    table2=dynamo_db_client.Table('userProfile')
    # try:
    print(event['form']['code'])
    code=event['form']['code']
    print(event)
    response=table.get_item(Key={'code':code})['Item']
    # thread=response['Item']
    comments=response['comments']
    GPA=response['GPA']
    workload=response['workload']
    semester=response['semester']
    
    GPA.append(event['form']['gpa'])
    workload.append(event['form']['workload'])
    semester.append(event['form']['semester'])
    
    new_comment={}
    new_comment['user']=event['form']['user']
    new_comment['time']=event['form']['time']
    new_comment['grade']=event['form']['grade']
    new_comment['gpa']=event['form']['gpa']
    new_comment['workload']=event['form']['workload']
    new_comment['semester']=event['form']['semester']
    new_comment['comments']=event['form']['comment']
    new_comment['instructor']=event['form']['instructor']
    
    response2 = table2.get_item(Key = {'userName':new_comment['user']})
    new_comment_user_Img = response2['Item']['img']
    new_comment['new_comment_user_Img'] = new_comment_user_Img
    
    comments.append(new_comment)
    table.update_item(
    Key={'code':code},
    UpdateExpression="SET comments = :val1",
    ExpressionAttributeValues={':val1': comments})
    
    table.update_item(
    Key={'code':code},
    UpdateExpression="SET GPA = :val2",
    ExpressionAttributeValues={':val2': GPA})
    
    table.update_item(
    Key={'code':code},
    UpdateExpression="SET workload = :val3",
    ExpressionAttributeValues={':val3': workload})
    
    table.update_item(
    Key={'code':code},
    UpdateExpression="SET semester = :val4",
    ExpressionAttributeValues={':val4': semester})
        
    # except:
    #     print('no such course')
   
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }