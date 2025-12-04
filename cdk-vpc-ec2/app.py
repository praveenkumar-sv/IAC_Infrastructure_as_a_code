#!/usr/bin/env python3
import aws_cdk as cdk
from cdk_vpc_ec2.cdk_vpc_ec2_stack import CdkVpcEc2Stack

app = cdk.App()

CdkVpcEc2Stack(app, "CdkVpcEc2Stack",
               env=cdk.Environment(
                   account="039612884217",
                   region="ap-south-1"
               ))

app.synth()
