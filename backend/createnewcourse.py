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
    

def lambda_handler(event, context):
    # TODO implement
    # print(event)
    
    # course='COMS4111'
    # # code='COMS6998'
    # official_document='1'#url
    # department_website='2'#url
    # other_course='3'#url
    
    # user='Jerry'
    # comment='very good'
    # gpa='4.0'
    # workload='3.8'
    # assessment_type='report'
    # semester='2021fall'
    
    course=event['courseForm']['courseName']
    code=event['courseForm']['code']
    department=event['courseForm']['department']
    courseWebsite=event['courseForm']['courseWebsite']
    deptWebsite=event['courseForm']['deptWebsite']
    exam=event['courseForm']['exam']
    assignment=event['courseForm']['assignment']
    report=event['courseForm']['report']
    project=event['courseForm']['project']
    GPA=event['courseForm']['GPA']
    workload=event['courseForm']['workload']
    comments=event['courseForm']['comment']
    semester = event['courseForm']['semester']
    # year = event['courseForm']['year']
   
    
    id_list=[]
    dynamo_db_client = get_db()
    table=dynamo_db_client.Table('course_list')
    table.put_item(
    Item={
        'course':course,
        'code':code,
        'department':department,
        'courseWebsite':courseWebsite,
        'deptWebsite': deptWebsite,
        'exam':exam,
        'assignment':assignment,
        'report':report,
        'project':project,
        'GPA':GPA,
        'workload':workload,
        'comments':[],
        'semester':semester
    })
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }