import aws_cdk as core
import aws_cdk.assertions as assertions

from simple_bucket.simple_bucket_stack import SimpleBucketStack

# example tests. To run these tests, uncomment this file along with the example
# resource in simple_bucket/simple_bucket_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SimpleBucketStack(app, "simple-bucket")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
