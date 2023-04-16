import boto3

# Set your desired user name and initial password for console access
user_name = 'cloud-architect'
initial_password = 'InitialPassword!123'

# Create an IAM client
iam = boto3.client('iam')

# Create a new IAM user
response = iam.create_user(UserName=user_name)
print(f'User {user_name} created.')

# Create access keys for programmatic access
response = iam.create_access_key(UserName=user_name)
access_key_id = response['AccessKey']['AccessKeyId']
secret_access_key = response['AccessKey']['SecretAccessKey']
print(f'Access key ID: {access_key_id}')
print(f'Secret access key: {secret_access_key}')

# Set initial password for console access and require password change
iam.create_login_profile(
    UserName=user_name,
    Password=initial_password,
    PasswordResetRequired=True
)
print(f'Console access enabled with initial password: {initial_password}')
