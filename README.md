GET https://l4qgjh8uuj.execute-api.us-east-1.amazonaws.com/mymovieapi 

check status

GET https://l4qgjh8uuj.execute-api.us-east-1.amazonaws.com/mymovieapi/movie?imdbid=tt0482571 

get a movie by id (otros ids: tt0109830
tt5727208
tt1392214
tt11126994)

GET https://l4qgjh8uuj.execute-api.us-east-1.amazonaws.com/mymovieapi/movies GET all movies


POST https://l4qgjh8uuj.execute-api.us-east-1.amazonaws.com/mymovieapi/movie
content-type: application/json

{
  "imdbid":"tes",
  "movie":"tes"
}

PATCH  https://l4qgjh8uuj.execute-api.us-east-1.amazonaws.com/mymovieapi/movie


{
    "imdbid": "tes",
    "updateKey":"movie",
    "updateValues":"test"
}

update a existing movie by id

DELETE https://l4qgjh8uuj.execute-api.us-east-1.amazonaws.com/mymovieapi/movie

{
    "imdbid": "tes"
}

delete a existing movie by id
