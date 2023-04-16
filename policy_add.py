import boto3

# Set the user name of the existing user
user_name = 'cloud-architect'

# Create an IAM client
iam = boto3.client('iam')

# Attach the "AdministratorAccess" managed policy to the user
administrator_policy_arn = 'arn:aws:iam::aws:policy/AdministratorAccess'
iam.attach_user_policy(UserName=user_name, PolicyArn=administrator_policy_arn)
print(f'AdministratorAccess policy attached to the user {user_name}.')
