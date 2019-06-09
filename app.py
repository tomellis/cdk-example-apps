#!/usr/bin/env python3

from aws_cdk import cdk

from hello_cdk.hello_cdk_stack import HelloCdkStack


app = cdk.App()
HelloCdkStack(app, "HelloCdkStack")

app.run()
