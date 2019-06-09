from aws_cdk import (
    aws_s3 as s3,
    cdk
)

class HelloCdkStack(cdk.Stack):

    def __init__(self, app: cdk.App, id: str, **kwargs) -> None:
        super().__init__(app, id)

        bucket = s3.Bucket(self,
        "MyFirstBucketwithCDK",
        versioned=True,
        encryption=s3.BucketEncryption.KmsManaged,)
