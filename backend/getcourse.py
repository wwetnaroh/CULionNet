import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    db=boto3.resource('dynamodb')
    table=db.Table('course_list')
    course=table.scan()['Items']
    course_list=[]
    for i in range(len(course)):
        dict={}
        dict['name']=course[i]['course']
        dict['code']=course[i]['code']
        course_list.append(dict)
    print(dict)
    print(course_list)
    return {
        'statusCode': 200,
        'course_list':course_list
    }
