import json
import boto3
# def get_db():
#     """
#     get db client
#     :return:
#     """

#     db = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id=ACCESS_ID,
#                         aws_secret_access_key=ACCESS_KEY)
#     return db
def lambda_handler(event, context):
    # TODO implement
    print(event)
    
    # database='Job_hunting'
    # id='hello world2022-4-30-1651353975963'
    
    database=event['db']
    id=event['id']
    
    db=boto3.resource('dynamodb')
    table=db.Table(database)
   
    response=table.get_item(Key={'id':id})
    print('response is:', response)
    thread=response['Item']
    
    
    
    
    postUser=thread['content']['main']['user']
    
    table2 = db.Table('userProfile')
    response2 = table2.get_item(Key = {'userName':postUser})
    postUserImg = response2['Item']['img']
    
    postTime=thread['create_time']
    main_content=thread['content']['main']['content']
    title=thread['thread name']
    comments=[]
    
    content1=thread['content']['comments']
    
    
    
    for i in content1.keys():
        a=i.split(',')
        print(a)
        dict={}
        dict['username']=a[0],
        dict['time']=a[1],
        print(a[0])
        print(a[1])
        dict['comment']=content1[i]
        # dict['topic']=content1[i]
        # comment=content[i]
        # print(comment)
        response3 = table2.get_item(Key={'userName': a[0]})['Item']
        dict['img'] = response3['img']
        comments.append(dict)
    print(main_content)
    
    
    
    
    return {
        'statusCode': 200,
        'postUser':postUser,
        'postTime':postTime,
        'postUserImg':postUserImg,
        'title':title,
        'content':main_content,
        'comments':comments
    }

