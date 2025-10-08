import boto3
from pprint import pprint

client = boto3.client('ec2', region_name='ap-south-1')

res = client.run_instances(
    ImageId='ami-0f9708d1cd2cfee41',
    InstanceType='t3.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='ec2_boto3',
    TagSpecifications=[
        {
            'ResourceType':'instance',
            'Tags':[
                {
                    'Key':'Name',
                    'Value':'Boto3Instance'
                }
            ]
        }
    ],
    BlockDeviceMappings=[
    {
        'DeviceName':'/dev/xvda',
        'Ebs':{
            'DeleteOnTermination':True,
            'VolumeSize':20
        }
    }
]
)

pprint(res)

pprint('Instance description: ',client.describe_instances())
