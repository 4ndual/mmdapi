GET https://l4qgjh8uuj.execute-api.us-east-1.amazonaws.com/mymovieapi 

check status

GET https://l4qgjh8uuj.execute-api.us-east-1.amazonaws.com/mymovieapi/movie?imdbid=tt0482571 

get a movie or serie by id  movie?imdbid=tt0482571  (other ids: tt0109830,
tt5727208)

GET https://l4qgjh8uuj.execute-api.us-east-1.amazonaws.com/mymovieapi/movies GET all movies


POST https://l4qgjh8uuj.execute-api.us-east-1.amazonaws.com/mymovieapi/movie
content-type: application/json

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
"sk": "movie#tt0099685", 
"Runtime (mins)": "146", 
"imdbid": "tt0099685", 
"pk": "rated", 
"Directors": "Martin Scorsese", 
"Rating": 10
 }

#required: pk, sk, gsi1, Directors, Rating,  IMDb Rating, Year

PATCH  https://l4qgjh8uuj.execute-api.us-east-1.amazonaws.com/mymovieapi/movie


{
    "pk": "rated",
    "sk": "movie#tt0099685"
    "updateKey":"Title",
    "updateValues":"The Goodfellas"
}

update a existing movie by id

DELETE https://l4qgjh8uuj.execute-api.us-east-1.amazonaws.com/mymovieapi/movie

{
    "pk": "rated"
    "sk: "movie#tt0099685"
}

delete a existing movie by id
