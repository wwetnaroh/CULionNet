# the function is used to add user and courselist to the DB userProfile
# the column of threadList will be handled by post thread lambda
import boto3
# from configs import ACCESS_KEY, ACCESS_ID
# from constants import SUPPORTED_CUISINES, DYNAMO_DB_TABLE_NAME
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


def get_courseList(userName):  # 拿到一个人的可
    userName = userName
    dynamo_db_client = get_db()
    table = dynamo_db_client.Table('userProfile')
    response = table.get_item(Key={'userName': userName})['Item']
    course_list=[]
    course_list = response['course_list']
    return course_list


def create_user(userName, major, headline, linkedin, github, courseList,img, editImg, email):
    print('in create_user')
    dynamo_db_client = get_db()
    table = dynamo_db_client.Table('userProfile')
    try:
        response = table.get_item(Key={'userName': userName})['Item']
        print('response is: ', response)
        course_list = response['course_list']
        for course in courseList:
            print(course)
            course_list.append(course)
        course_list = list(set(course_list))
        print('course_list:', course_list)
        print("editImg is", editImg)
        if editImg:
            table.update_item(
                Key={'userName': userName},
                UpdateExpression="SET course_list = :val1, github = :val2, linkedin = :val3, headline = :val4, major = :val5, img = :val6",
                ExpressionAttributeValues={':val1': course_list, ':val2': github, ':val3': linkedin, ':val4': headline,
                                           ':val5': major, ":val6":img
                                         })

        else:
            table.update_item(
                Key={'userName': userName},
                UpdateExpression="SET course_list = :val1, github = :val2, linkedin = :val3, headline = :val4, major = :val5",
                ExpressionAttributeValues={':val1': course_list, ':val2': github, ':val3': linkedin, ':val4': headline,
                                           ':val5': major
                                           })

    except:
        course_list = courseList
        thread_list = []
        dynamo_db_client = get_db()
        table = dynamo_db_client.Table('userProfile')

     
        if editImg:
            table.put_item(
                Item={
                    'userName': userName,
                    'major': major,
                    'headline': headline,
                    'linkedin': linkedin,
                    'github': github,
                    'course_list': course_list,
                    'thread_list': thread_list,
                    'img':img,
                    'email':email
                })
        else:
            table.put_item(
                Item={
                    'userName': userName,
                    'major': major,
                    'headline': headline,
                    'linkedin': linkedin,
                    'github': github,
                    'course_list': course_list,
                    'thread_list': thread_list,
                    'email':email
                })
    
def add_course(userName, courselist):
    dynamo_db_client = get_db()
    table = dynamo_db_client.Table('userProfile')
    course_list = get_courseList(userName)
    for course in courselist:
        course_list.append(course)
    # course_list = list(set(course_list))
    table.update_item(
        Key={'userName': userName},
        UpdateExpression="SET course_list = :val1",
        ExpressionAttributeValues={':val1': course_list})


def del_course(userName, courselist):
    dynamo_db_client = get_db()
    table = dynamo_db_client.Table('userProfile')
    course_list = get_courseList(userName)
    for course in courselist:
        course_list.remove(course)
    table.update_item(
        Key={'userName': userName},
        UpdateExpression="SET course_list = :val1",
        ExpressionAttributeValues={':val1': course_list})


def lambda_handler(event, context):
    # need to get user name, courselist and operation to implement the logics
    print('event is', event)

  

    userName = event['user']
    major = event['major']
    linkedin = event['linkedin']
    github = event['github']
    courselist = event['courselist']
    operation = event['operation']
    headline = event['headline']
    img = event['img']
    editImg = event['editImg']
    email=event['email']
    if operation == '':
        create_user(userName, major, headline, linkedin, github, courselist, img, editImg, email)
    elif operation == 'add':
        add_course(userName, courselist)
    elif operation == 'delete':
        del_course(userName, courselist)

    elif operation == 'edit':
        create_user(userName, major, headline, linkedin, github, courselist, img, editImg,email)



    return {
        'statusCode': 200,
        'body': json.dumps('Hello lambda.')
    }
