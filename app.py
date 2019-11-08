import requests
import datetime
import boto3
import time
print("Hello Let's Start Monitoring")
print("---   OO   ---")
print("---   OO   ---")
SIT={'ec2_id':'<instance-id>',
    'ec2_name':'<ec2-tag-name>'}

UAT={'ec2_id':'instance-id',
    'ec2_name':'ec2-tag-name'}

ec2-instances=[SIT,UAT]

client = boto3.client('cloudwatch', region_name='<region>', aws_access_key_id='<key-id>', aws_secret_access_key='<access-key>')
token = '<line-notify-auth-token>'
def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

while True:
    for ec2 in  ec2-instances:
        now = datetime.datetime.utcnow()
        timediff = datetime.timedelta(minutes=1)

        response = client.get_metric_statistics(
           Namespace='AWS/EC2',
           MetricName='CPUUtilization',
           Dimensions=[
               {
                   'Name': 'InstanceId',
                   'Value': ec2['ec2_id']  
               },
           ],
           StartTime=now-timediff,
           EndTime=now,
           Period=60,
           Statistics =['SampleCount','Average', 'Sum']
        )
        #print("Alert Name =" ,response3['Label'] )
        try : 
            average=str(response['Datapoints'][0]['Average'])

            #print(response3['Label'] ,"is" ,response3['Datapoints'][0]['Average'])

            alert=str("InstanceName " +  ec2['ec2_name'] + " " + response['Label'] + " is " + average + " So Hot!!!")

            #print(b)
            # 修改為你要傳送的訊息內容
            alert

            cpu=float(response['Datapoints'][0]['Average'])

            if (cpu > 80):
                print(alert)
                lineNotifyMessage(token, alert)
        except :
            pass
    time.sleep(30)
