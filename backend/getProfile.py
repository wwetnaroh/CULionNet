#the function is used to add user and courselist to the DB userProfile
#the column of threadList will be handled by post thread lambda
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
    
def get_full_Courses():
    courses = []
    dynamo_db_client = get_db()
    table=dynamo_db_client.Table('course_list')
    
    responses = table.scan()['Items']
    #print(responses)
    for response in responses:
        courses.append(response['course'])
    return courses
      
def get_info(userName):
    userName = userName
    dynamo_db_client = get_db()
    table=dynamo_db_client.Table('userProfile')
    response=table.get_item(Key={'userName': userName})['Item']
    return response
    
def get_profile(userName):
    dynamo_db_client = get_db()
    table=dynamo_db_client.Table('userProfile')
    profile = get_info(userName)
    print(profile)
    if not profile:
        return {
        'statusCode': 400,
        'body': json.dumps('You have not created a profile yet, please create one.')
    }
    cur_courseList = get_full_Courses()#拿到全局的课
    return {
        'statusCode': 200,
        'userName': userName,
        'headline': profile['headline'],
        'major': profile['major'], 
        'linkedin': profile['linkedin'], 
        'github': profile['github'], 
        'courselist': profile['course_list'],
        'thread_list': profile['thread_list'],
        'full_courses': cur_courseList,
        'img':profile['img'],
        'email':profile['email']
    }

        
def lambda_handler(event, context):
    #need to get user name, courselist and operation to implement the logics
    print('***************event***************')
    print('event is', event)
    userName = event['username']
    return get_profile(userName)