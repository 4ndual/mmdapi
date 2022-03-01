# Welcome to my Python project "my movie database api(MMDAPI)" !

__Build using Serverless, lambda, Dynamodb, api-gateway, CDK, boto3__

## Test

__Check status:__

GET https://l4qgjh8uuj.execute-api.us-east-1.amazonaws.com/mymovieapi 

__Get a movie by id:__

GET https://l4qgjh8uuj.execute-api.us-east-1.amazonaws.com/mymovieapi/movie?imdbid=tt0482571 

_Other ids: tt0109830, tt5727208_

__Get all movies:__

GET https://l4qgjh8uuj.execute-api.us-east-1.amazonaws.com/mymovieapi/movies 

__Create a movien in db:__

POST https://l4qgjh8uuj.execute-api.us-east-1.amazonaws.com/mymovieapi/movie 

```
{ 
"Genres": "Biography, Crime, Drama", 
"Year": "1990", 
"gsi1": "all", 
"Date Rated": "2020-05-04", 
"Type": "movie", 
"URL": "https://www.imdb.com/title/tt0099685/", 
"Title": "Goodfellas", 
"Num Votes": "1100652", 
"Release Date": "1990-09-09", 
"IMDb Rating": "8.7", 
"Runtime (mins)": "146", 
"imdbid": "tt0099685", 
"Directors": "Martin Scorsese", 
"Rating": 10
 }
 ```

_required: imdbid, gsi1, Directors, Rating,  IMDb Rating, Year_

__Update a movie by id__

PATCH  https://l4qgjh8uuj.execute-api.us-east-1.amazonaws.com/mymovieapi/movie

 ```
{
    "imdbid": "tt0099685",
    "updateKey":"Title",
    "updateValues":"The Goodfellas"
}
 ```

__Delete a movie by id__
DELETE https://l4qgjh8uuj.execute-api.us-east-1.amazonaws.com/mymovieapi/movie
 ```
{"imdbid": "tt0099685" }
 ```

# Install

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

to run locally with SAM (requires Docker):

```
$ sam local start-api
```

to deploy to aws(requires credentials):

```
$ cdk deploy
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
