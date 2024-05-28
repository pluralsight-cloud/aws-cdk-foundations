#!/usr/bin/env python3
import os

import aws_cdk as cdk

from simple_bucket.simple_bucket_stack import SimpleBucketStack


app = cdk.App()
SimpleBucketStack(app, "SimpleBucketStack")

app.synth()