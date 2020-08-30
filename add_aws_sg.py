import boto3
import json
from botocore.exceptions import ClientError

##import my module
from get_myip import *


ec2 = boto3.client('ec2')
SecurityGroupID = 'sg-08d8b99f9b6067317'
mask = '/16'
port = 3833
protocol = 'tcp'


def add_to_aws_sg(ip_a_mask, fromport, toport, protocol):
    try:
        response = ec2.describe_security_groups(GroupIds=['sg-08d8b99f9b6067317'])

        #parsedResponse = json.loads(response)
        #print(json.dumps(response['SecurityGroups'], indent=4, sort_keys=True))

        data = ec2.authorize_security_group_ingress(
                GroupId = SecurityGroupID,
                IpPermissions = [
                    {
                        'FromPort':fromport,
                        'ToPort':toport,
                        'IpProtocol':protocol,
                        'IpRanges':[{'CidrIp': ip_a_mask}]
                        },
                    ]
                )
        
        print('Ingress Successfully Set %s' % data)

    except ClientError as e:
        print(e)

def main():
    ip = getmyip()
    ip_a_mask = ip+mask

    add_to_aws_sg(ip_a_mask, port, port, protocol)


if __name__ == "__main__":
    main()


