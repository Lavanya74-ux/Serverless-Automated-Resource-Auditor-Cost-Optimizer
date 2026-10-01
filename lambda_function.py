import boto3

def lambda_handler(event, context):
    # Initialize the EC2 client
    ec2 = boto3.client('ec2', region_name='us-east-1')
    
    # Search for all running EC2 instances that have 'Dev' in their name
    custom_filter = [
        {'Name': 'instance-state-name', 'Values': ['running']},
        {'Name': 'tag:Name', 'Values': ['*Dev*']}
    ]
    
    # Get the list of instances matching our filter
    response = ec2.describe_instances(Filters=custom_filter)
    
    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
            
    # If we find running Dev instances, stop them automatically
    if len(instance_ids) > 0:
        print(f"Auditor Alert: Found idle Dev instances: {instance_ids}. Stopping them now to save costs...")
        ec2.stop_instances(InstanceIds=instance_ids)
        return {
            'statusCode': 200,
            'body': f"Successfully stopped idle cost-incurring instances: {instance_ids}"
        }
    else:
        print("Auditor Alert: No running Dev instances found. Cloud costs are optimized!")
        return {
            'statusCode': 200,
            'body': "No running instances found."
        }
