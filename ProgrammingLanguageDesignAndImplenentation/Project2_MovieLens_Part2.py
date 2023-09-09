#
# File: objecttier.py
#
# Builds Movie-related objects from data retrieved through
# the data tier.
#
# Original author:
#   Prof. Joe Hummel
#   U. of Illinois, Chicago
#   CS 341, Spring 2022
#   Project #02
#
import datatier


##################################################################
#
# Movie:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Year: string
#
class Movie:

    def __init__(self, m_id, title, r_year):
        self._Movie_ID = m_id
        self._Title = title
        self._Release_Year = r_year

    @property
    def Movie_ID(self):
        return self._Movie_ID

    @property
    def Title(self):
        return self._Title

    @property
    def Release_Year(self):
        return self._Release_Year


##################################################################
#
# MovieRating:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Year: string
#   Num_Reviews: int
#   Avg_Rating: float
#
class MovieRating:

    def __init__(self, m_id, title, r_year, n_rev, avg_rat):
        self._Movie_ID = m_id
        self._Title = title
        self._Release_Year = r_year
        self._Num_Reviews = n_rev
        self._Avg_Rating = avg_rat

    @property
    def Movie_ID(self):
        return self._Movie_ID

    @property
    def Title(self):
        return self._Title

    @property
    def Release_Year(self):
        return self._Release_Year

    @property
    def Num_Reviews(self):
        return self._Num_Reviews

    @property
    def Avg_Rating(self):
        return self._Avg_Rating


##################################################################
#
# MovieDetails:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Date: string, date only (no time)
#   Runtime: int (minutes)
#   Original_Language: string
#   Budget: int (USD)
#   Revenue: int (USD)
#   Num_Reviews: int
#   Avg_Rating: float
#   Tagline: string
#   Genres: list of string
#   Production_Companies: list of string
#
class MovieDetails:

    def __init__(self, m_id, title, r_date, runt, o_lang, budget, revenue,
                 n_rev, avg_rat, tag):
        self._Movie_ID = m_id
        self._Title = title
        self._Release_Date = r_date
        self._Runtime = runt
        self._Original_Language = o_lang
        self._Budget = budget
        self._Revenue = revenue
        self._Num_Reviews = n_rev
        self._Avg_Rating = avg_rat
        self._Tagline = tag
        self._Genres = []
        self._Production_Companies = []

    @property
    def Movie_ID(self):
        return self._Movie_ID

    @property
    def Title(self):
        return self._Title

    @property
    def Release_Date(self):
        return self._Release_Date

    @property
    def Runtime(self):
        return self._Runtime

    @property
    def Original_Language(self):
        return self._Original_Language

    @property
    def Budget(self):
        return self._Budget

    @property
    def Revenue(self):
        return self._Revenue

    @property
    def Num_Reviews(self):
        return self._Num_Reviews

    @property
    def Avg_Rating(self):
        return self._Avg_Rating

    @property
    def Tagline(self):
        return self._Tagline

    @property
    def Genres(self):
        return self._Genres

    @property
    def Production_Companies(self):
        return self._Production_Companies


##################################################################
#
# num_movies:
#
# Returns: # of movies in the database; if an error returns -1
#
def num_movies(dbConn):
    try:
        sql = "SELECT COUNT(Title) from Movies;"
        row = datatier.select_one_row(dbConn, sql)  # only need 1 row
        return row[0]
    except:
        return -1


##################################################################
#
# num_reviews:
#
# Returns: # of reviews in the database; if an error returns -1
#
def num_reviews(dbConn):
    try:
        sql = "SELECT COUNT(Rating) from Ratings;"
        row = datatier.select_one_row(dbConn, sql)  # only need 1 row
        return row[0]
    except:
        return -1


##################################################################
#
# get_movies:
#
# gets and returns all movies whose name are "like"
# the pattern. Patterns are based on SQL, which allow
# the _ and % wildcards. Pass "%" to get all stations.
#
# Returns: list of movies in ascending order by name;
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_movies(dbConn, pattern):
    listMovies = []
    sql = """SELECT Movie_ID, Title, strftime('%Y', Release_Date) from Movies
             where Title like ? order by Title asc;"""
    rows = datatier.select_n_rows(dbConn, sql, [pattern])  # will have multiple rows
    for r in rows:
        mov = Movie(r[0], r[1], r[2])  # create Movie object with necessary values
        listMovies.append(mov)  # append the movies into list
    return listMovies


##################################################################
#
# get_movie_details:
#
# gets and returns details about the given movie; you pass
# the movie id, function returns a MovieDetails object. Returns
# None if no movie was found with this id.
#
# Returns: if the search was successful, a MovieDetails obj
#          is returned. If the search did not find a matching
#          movie, None is returned; note that None is also
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_movie_details(dbConn, movie_id):
  try:
    sql = """SELECT Movie_ID, Title, strftime('%Y-%m-%d', Release_Date) as Date, 
             Runtime, Original_Language, Budget, Revenue from Movies where Movie_ID = ?;"""
    sql2 = "SELECT Tagline from Movie_Taglines where Movie_ID = ?;"
    sql3 = "SELECT Count(Rating), avg(Rating) from Ratings where Movie_ID = ?;"
    sql4 = """SELECT Genre_Name from Genres 
              join Movie_Genres on Genres.Genre_ID = Movie_Genres.Genre_ID
              where Movie_Genres.Movie_ID = ? order by Genre_Name asc;"""
    sql5 = """SELECT Company_Name from Companies
              join Movie_Production_Companies on Companies.Company_ID = Movie_Production_Companies.Company_ID
              where Movie_Production_Companies.Movie_ID = ? order by Company_Name asc;"""

    row1 = datatier.select_one_row(dbConn, sql, [movie_id])  # only 1 row
    if row1 is None or row1 == (): 
        return None

    row2 = datatier.select_one_row(dbConn, sql2, [movie_id])  # only 1 row
    t = ""
    if row2 is None or row2 == () or row2[0] == "":   # check if tagline is empty
        t = ""
    elif row2[0] != "":  # if tagline is not empty, proceed
        t = row2[0]
    tag_line = t

    row3 = datatier.select_one_row(dbConn, sql3, [movie_id])  # only 1 row
    toople = tuple()
    if row3 is None or row3 == () or row3[0] == 0:  # check if num reviews is 0
        toople = (0, 0.0)
    elif row3[0] > 0:  # if num reviews more than 0, we can have an average
        toople = row3
    num_rev = toople[0]  # set the values
    av_rating = toople[1]

    # make a MovieDetails object containing everything so far
    tempList = MovieDetails(row1[0], row1[1], row1[2], row1[3], row1[4],
                            row1[5], row1[6], num_rev, av_rating, tag_line)

    row4 = datatier.select_n_rows(dbConn, sql4, [movie_id])  # multiple rows
    if row4 is None:
        return None
    for r in row4:
        g = r[0]
        tempList._Genres.append(g)  # append the genres 1 by 1 to the list

    row5 = datatier.select_n_rows(dbConn, sql5, [movie_id])  #multiple rows
    if row5 is None:
        return None
    for r in row5:
        h = r[0]
        tempList._Production_Companies.append(h)  # append the companies 1 by 1
    return tempList
  except:
    return None


##################################################################
#
# get_top_N_movies:
#
# gets and returns the top N movies based on their average
# rating, where each movie has at least the specified # of
# reviews. Example: pass (10, 100) to get the top 10 movies
# with at least 100 reviews.
#
# Returns: returns a list of 0 or more MovieRating objects;
#          the list could be empty if the min # of reviews
#          is too high. An empty list is also returned if
#          an internal error occurs (in which case an error
#          msg is already output).
#
def get_top_N_movies(dbConn, N, min_num_reviews):
    sql = """SELECT Movies.Movie_ID, Title, strftime('%Y', Release_Date), count(Rating), avg(Rating) from Movies
             join Ratings on Movies.Movie_ID = Ratings.Movie_ID
             group by Movies.Movie_ID 
             having count(Rating) >= ?
             order by avg(Rating) desc limit ?;"""

    row = datatier.select_n_rows(dbConn, sql, [min_num_reviews, N])  # multiple rows
    listNMovies = []  # will contain movies
    for r in row:
        mov = MovieRating(r[0], r[1], r[2], r[3], r[4])  # make MovieRating object with needed values
        listNMovies.append(mov)  # append the objects to the list
    return listNMovies


##################################################################
#
# add_review:
#
# Inserts the given review --- a rating value 0..10 --- into
# the database for the given movie. It is considered an error
# if the movie does not exist (see below), and the review is
# not inserted.
#
# Returns: 1 if the review was successfully added, returns
#          0 if not (e.g. if the movie does not exist, or if
#          an internal error occurred).
#
def add_review(dbConn, movie_id, rating):
    sql = "SELECT * from Movies where Movie_ID like ?"
    row = datatier.select_one_row(dbConn, sql, [movie_id])  # get the movie
    if row == ():  # if movie doesn't exist
        return 0
    sql2 = "INSERT INTO Ratings(Movie_ID, Rating) VALUES(?, ?);"
    insert = datatier.perform_action(dbConn, sql2, [movie_id, rating]) # execute
    if insert == -1:  # if perform_action returns error
        return 0
    return 1  # success


##################################################################
#
# set_tagline:
#
# Sets the tagline --- summary --- for the given movie. If
# the movie already has a tagline, it will be replaced by
# this new value. Passing a tagline of "" effectively
# deletes the existing tagline. It is considered an error
# if the movie does not exist (see below), and the tagline
# is not set.
#
# Returns: 1 if the tagline was successfully set, returns
#          0 if not (e.g. if the movie does not exist, or if
#          an internal error occurred).
#
def set_tagline(dbConn, movie_id, tagline):
    sql = "SELECT * from Movies where Movies.Movie_ID = ?;"
    row = datatier.select_one_row(dbConn, sql, [movie_id])  # get the movie
    if row == ():  # if movie doesn't exist
        return 0
    #sql2 = """Update Movie_Taglines
    #          set Tagline = ?
    #          where Movie_ID = ?;"""
    sql2 = "INSERT INTO Movie_Taglines(Movie_ID, Tagline) VALUES(?, ?);"
    set = datatier.perform_action(dbConn, sql2, [movie_id, tagline])  # execute
    if set == -1:  # if perform_action returns error
        return 0
    return 1  # success