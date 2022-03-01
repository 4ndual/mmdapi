import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_init_app___language_python.cdk_init_app___language_python_stack import CdkInitAppLanguagePythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_init_app___language_python/cdk_init_app___language_python_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkInitAppLanguagePythonStack(app, "cdk-init-app---language-python")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
