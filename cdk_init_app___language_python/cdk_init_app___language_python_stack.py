from constructs import Construct # type: ignore
from aws_cdk import ( # type: ignore
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_s3 as s3,
    aws_lambda as lambda_,
    aws_apigateway as apigw
)



class CdkInitAppLanguagePythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:

        super().__init__(scope, construct_id, **kwargs)
        

        # Create lambda function.
        fn=lambda_.Function(self, "MyLambda",
                code=lambda_.Code.from_asset("lambda"),
                handler="handler.main",
                runtime=lambda_.Runtime.PYTHON_3_8
        )

        api = apigw.LambdaRestApi(self, "cdk-firstsample",
            handler=fn,
            proxy=False
        )
        
        api.root.add_method("GET")
        
        movies = api.root.add_resource("movies")
        movies.add_method("GET") # GET /movies
        movies.add_method("POST") # POST /movies

        movie = api.root.add_resource("movie")
        movie.add_method("GET") # GET /movies/{movie}
        movie.add_method("POST") # GET /movies/{movie}
        movie.add_method("PATCH") # GET /movies/{movie}
        movie.add_method("DELETE") # GET /movies/{movie}
        
        tvSeries = api.root.add_resource("tvSeries")
        tvSeries.add_method("GET") # GET /tvSeries
        tvSeries.add_method("POST") # POST /tvSeries

        tvSerie = api.root.add_resource("tvSerie")
        tvSerie.add_method("GET") # GET /tvSeries/{tvSerie}
        tvSerie.add_method("POST") # GET /tvSeries/{tvSerie}
        tvSerie.add_method("PATCH") # GET /tvSeries/{tvSerie}
        tvSerie.add_method("DELETE") # GET /tvSeries/{tvSerie}

        # the default integration for methods is "handler", but one can
        # customize this behavior per method or even a sub path.
       
        #
                #queue = sqs.Queue(
                #    self, "CdkInitSampleAppLanguagePythonQueue",
        #    visibility_timeout=Duration.seconds(300),
        #)
#
        #topic = sns.Topic(
        #    self, "CdkInitSampleAppLanguagePythonTopic"
        #)
#
        #topic.add_subscription(subs.SqsSubscription(queue))
#