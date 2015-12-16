# Exercise: Using your first API

# API documentation: http://bechdeltest.com/api/v1/doc

# Goal 1:
#   Ask the user for the movie title they want to check
#   Display all of the details about the movie returned by the API
#
#   Things to keep in mind:
#       How will your program behave when multiple movies are returned?
#       How will your program behave when no movies are returned?
#       How will your program behave with works like "the" in the title?

# Goal 2:
#   Check to see if the user input is a movie title or an ImdbID and use the proper endpoint.
    
# Goal 3:
#   Integrate this with the Open Movie Database API: http://www.omdbapi.com/
#   Display all of the details from both APIs when searching for a movie.
#   Note that you may need to prefix your ImdbIDs with 'tt' to get the search to work.

# Copy these URLs into your browser
# To visualize as a CSV, copy the JSON into http://konklone.io/json

# Sample Bechdel test API returns: http://bechdeltest.com/api/v1/getMovieByImdbId?imdbid=0367631
# JSON: 
    # {
    #   "visible": "1",
    #   "date": "2009-12-05 05:13:37",
    #   "submitterid": "270",
    #   "rating": "3",
    #   "dubious": "0",
    #   "imdbid": "0367631",
    #   "id": "551",
    #   "title": "D.E.B.S.",
    #   "year": "2004"
    # }
# JSON to CSV link: http://konklone.io/json/?id=11488879

# Sample Open Movie Database API returns: http://www.omdbapi.com/?i=tt0367631&t=
# JSON:
    # {
    #   "Title": "D.E.B.S.",
    #   "Year": "2004",
    #   "Rated": "PG-13",
    #   "Released": "25 Mar 2005",
    #   "Runtime": "91 min",
    #   "Genre": "Action, Comedy, Romance",
    #   "Director": "Angela Robinson",
    #   "Writer": "Angela Robinson",
    #   "Actors": "Sara Foster, Jordana Brewster, Meagan Good, Devon Aoki",
    #   "Plot": "Plaid-skirted schoolgirls are groomed by a secret government agency to become the newest members of the elite national-defense group, D.E.B.S.",
    #   "Language": "English",
    #   "Country": "USA",
    #   "Awards": "1 win & 2 nominations.",
    #   "Poster": "http://ia.media-imdb.com/images/M/MV5BMjA0OTU5ODgyOF5BMl5BanBnXkFtZTcwODczNDgyMQ@@._V1_SX300.jpg",
    #   "Metascore": "42",
    #   "imdbRating": "5.2",
    #   "imdbVotes": "10,563",
    #   "imdbID": "tt0367631",
    #   "Type": "movie",
    #   "Response": "True"
    # }
# JSON to CSV link: http://konklone.io/json/?id=11488839

import requests

title=raw_input("Enter an IMDB ID or a movie title to search.")
def proper(x):
    x=x.title()
    return x

if title.isdigit():#search by IMBD ID
    print "\n\tInformation from Bechdel Test:"#bechdel API
    url="http://bechdeltest.com/api/v1/getMovieByImdbId?imdbid={}".format(title)
    response=requests.get(url)
    movies=response.json()
    if movies.get("status") == "404":
        print '\nNo movie found with IMDB ID {} on Bechdel. Try another title.'.format(proper(title))
    else:
        print "\n"
        for key, value in movies.items():
            print key, value

    print "\n\tInformation from OMDB:"#OMDB API
    url_2="http://www.omdbapi.com/?i=tt{}&t=".format(title)
    response=requests.get(url_2)
    movies=response.json()
    if movies.get("Response") == "False":
        print '\nNo movie found with IMBD ID {} on OMDB. Try another title.'.format(proper(title))
    else:
        print "\n"
        for key, value in movies.items():
            print key, value
else: #search by title
    #reformatting title for url
    title=title.upper()
    if title.startswith("THE "):
        title=title.replace("THE ","",1)
    title_for_search=title.replace(" ","+").replace("'","&#39;")

    url= "http://bechdeltest.com/api/v1/getMoviesByTitle?title={0}".format(title_for_search)
    response=requests.get(url)
    movies=response.json()
    if movies== []:#if no movie found
        print '\nNo movie found with title "{}". Try another title.'.format(proper(title))
    elif len(movies)>1:#if multiple movies returned
        print '\nThere are {0} movies with the title "{1}".'.format(len(movies),proper(title))
    else:#if one movie returned
        print '\nThere is 1 movie with the title "{}".'.format(proper(title))
    if movies!=[]:
        print "\n\tInformation from Bechdel Test:"#Bechdel API
        for movie in movies:
            print "\n"
            for key, value in movie.items():
                print key, value
        print "\n\tInformation from OMDB:"#OMDB API
        for movie in movies:
            for key, value in movie.items():
                while key=="imdbid":
                    IMDB= value
                    url_2="http://www.omdbapi.com/?i=tt{}&t=".format(IMDB)
                    response=requests.get(url_2)
                    movies=response.json()
                    if movies== []:
                        print 'No movie found with IMDB ID "{}". Try another title.'.format(IMDB)
                    else:
                        print "\n"
                        for key, value in movies.items():
                            print key, value
