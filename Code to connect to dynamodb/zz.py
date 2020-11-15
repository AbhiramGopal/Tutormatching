import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('tutormatch')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
# table.delete_item(
#             Key={
#                     'name': 'abhiram'
                   
#                 }
# #             )
# table.put_item(
#    Item={
#         'name': 'abhiram',
#         'password':'abhiram'
        
#     }
# )
response = table.get_item(Key={'name': 'sad'})
# item = response['Item']
print(response)
# {'ResponseMetadata': {'RequestId': '9HFMQALSTTQ5Q1Q5869LNU7IFFVV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'Server', 'date': 'Sat, 14 Nov 2020 16:41:21 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '2', 'connection': 'keep-alive', 'x-amzn-requestid': '9HFMQALSTTQ5Q1Q5869LNU7IFFVV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '2745614147'}, 'RetryAttempts': 0}}
print(response['ResponseMetadata']['HTTPHeaders']['content-length'])