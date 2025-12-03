

## CONFIGURE THE AWS CLI
Before you begin, ensure that you have the AWS CLI installed and configured with the necessary permissions to create S3 buckets.
You can configure the AWS CLI by running:
```
aws configure
```
NEED THE ACESS AND SECRATE KEY
for acees the AWS CLI

## CREATE THE S3 BUCKET USING CLOUDFORMATION
To create an S3 bucket using CloudFormation, follow these steps:
1. Create a file named `s3bucket.yml` and add the following CloudFormation template

## connect to AWS CLI

using the commands 
## aws create-stack --stack-name "stack_NAEME" --template-body file://file_name.yml

stack_NAME=what ever give name

## aws delete-stack --stack-name "stack_NAME"
Monitor the stack creation process using:
``` 
aws cloudformation describe-stacks --stack-name my-s3-bucket-stack
```


## CREATING THE VPC AND EC2 ASSIGNING THE PORT NUMBERS 22 AND 80 TO EC2 INSTANCE 

## CREATE THE VPC_EC2.YML FILE
CREATE THE VPC_EC2.YML FILE

aws ec2 create-key-pair --key-name mykey --query "KeyMaterial" --output text > mykey.pem




aws cloudformation create-stack --stack-name my-s3-bucket-stack --template-body file://s3bucket.yml
chmod 400 mykey.pem

## CREATE THE STACK
aws cloudformation create-stack  --stack-name vpc-ec2-stack  --template-body file://vpc-ec2.yaml  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM

## DELETE THE STACK
aws cloudformation delete-stack --stack-name vpc-ec2-stack
 
 ## Monitor the stack creation process using:
 
aws cloudformation describe-stacks --stack-name vpc-ec2-stack