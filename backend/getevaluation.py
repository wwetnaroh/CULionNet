import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print(event)
    # database = event['course']
    # database='course_list'
    # course='COMS6998'
    
    code=event['course']
    
    db=boto3.resource('dynamodb')
    table=db.Table('course_list')
   
    course_content=table.get_item(Key={'code':code})['Item']
    print(course_content)
    course=course_content['course']
    department=course_content['department']
    courseWebsite=course_content['courseWebsite']
    deptWebsite=course_content['deptWebsite']
    exam=course_content['exam']
    assignment=course_content['assignment']
    report=course_content['report']
    project=course_content['project']
    GPA=course_content['GPA']
    workload=course_content['workload']
    semester = course_content['semester']
    comments=course_content['comments']
        
    
    return {
        'statusCode': 200,
        'course':course,
        'department':department,
        'courseWebsite':courseWebsite,
        'deptWebsite':deptWebsite,
        'exam':exam,
        'assignment':assignment,
        'report':report,
        'project':project,
        'GPA':GPA,
        'workload':workload,
        'semester':semester,
        'comments':comments
    }

