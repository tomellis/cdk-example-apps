from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    cdk,
)

class HelloCdkStack(cdk.Stack):

    def __init__(self, app: cdk.App, id: str, **kwargs) -> None:
        super().__init__(app, id)

#        bucket = s3.Bucket(self,
#        "MyFirstBucketwithCDK",
#        versioned=True,
#        encryption=s3.BucketEncryption.KmsManaged,)

        # Build the VPC
        vpc = ec2.Vpc(
            self, "MyVpc",
            max_a_zs=3
        )

        # Define ECS cluster constructr
        cluster = ecs.Cluster(
            self, 'FargateCluster',
            vpc=vpc
        )

        fargate_service = ecs_patterns.LoadBalancedFargateService(
            self, "FargateService",
            cluster=cluster,
            image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")
        )

        cdk.CfnOutput(
            self, "LoadBalancerDNS",
            value=fargate_service.load_balancer.load_balancer_dns_name
        )
