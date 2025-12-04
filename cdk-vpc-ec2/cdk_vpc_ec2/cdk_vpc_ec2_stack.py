from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct

class CdkVpcEc2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # 1️⃣ Create VPC
        vpc = ec2.Vpc(
            self,
            "MyDemoVPC",
            max_azs=2,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="publicSubnet",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                )
            ]
        )

        # 2️⃣ Create Security Group
        sg = ec2.SecurityGroup(
            self,
            "EC2SecurityGroup",
            vpc=vpc,
            description="Allow SSH (22) and HTTP (80)",
            allow_all_outbound=True
        )

        # Allow SSH
        sg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(22),
            "Allow SSH"
        )

        # Allow HTTP
        sg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            "Allow HTTP"
        )

        # 3️⃣ Create EC2 Instance
        instance = ec2.Instance(
            self,
            "MyDemoEC2",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux2023(),
            vpc=vpc,
            security_group=sg,
            key_name="my-keypair",  # Change to your actual key pair
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            )
        )

        # Output instance public IP
        from aws_cdk import CfnOutput
        CfnOutput(self, "EC2PublicIP",
                  value=instance.instance_public_ip)