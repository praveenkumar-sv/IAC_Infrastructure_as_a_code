from aws_cdk import (
    Stack,
    RemovalPolicy,
    CfnOutput,
)
from constructs import Construct
from aws_cdk import aws_s3 as s3

class CdkDemosStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create S3 bucket with destroy policy
        bucket = s3.Bucket(
            self,
            "MyDemoBucket",
            bucket_name='praveenkuar-cdkbucket24873294732',  # must be globally unique
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY  # ✅ FIXED
        )

        # Output bucket name
        CfnOutput(self, "BucketNameOutput", value=bucket.bucket_name)
