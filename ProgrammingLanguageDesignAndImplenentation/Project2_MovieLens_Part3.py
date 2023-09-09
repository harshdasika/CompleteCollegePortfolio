import sqlite3
import objecttier

#################################################################################
#
# command1
#
# Takes movie name as input, and then outputs ID + Title + Release Year
#
def command1(dbConn):
  mName = input("\nEnter movie name (wildcards _ and % supported): ")  # input
  print()
  listMovs = objecttier.get_movies(dbConn, mName)  # get the movies
  print("# of movies found:", len(listMovs))  
  if len(listMovs) == 0:  # if no movies
    return None
  numMovs = len(listMovs)
  print()
  
  if numMovs > 100:
    print("There are too many movies to display, please narrow your search and try again...")
    return None
  else:
    #print()
    for m in listMovs:
      print(m.Movie_ID, ":", m.Title, "(" + m.Release_Year + ")")   # print the results
  print()


#################################################################################
#
# command2
#
# Takes movie ID as input, and then outputs all the movie details
#
def command2(dbConn):
  print()
  mID = input("Enter movie id: ")  # input
  print()
  mDeets = objecttier.get_movie_details(dbConn, mID)  # get details object

  if mDeets is None:   # if no such movie exists
    print("No such movie...")
    print()
    return None
  else:   # print out all the details
    print(mDeets.Movie_ID, ":", mDeets.Title)
    print("  Release date:", mDeets.Release_Date)
    print("  Runtime:", mDeets.Runtime, "(mins)")
    print("  Orig language:", mDeets.Original_Language)
    print("  Budget:", "$" + f"{mDeets.Budget:,}", "(USD)")
    print("  Revenue:", "$" + f"{mDeets.Revenue:,}", "(USD)")
    print("  Num reviews:", mDeets.Num_Reviews)
    print("  Avg rating:", f"{mDeets.Avg_Rating:.2f}", "(0..10)")
    
    if mDeets.Genres == []:  # in the case of an empty list
      print("  Genres: ")
    else:
      print("  Genres:", end = " ")
      for g in mDeets.Genres:
        print(g, end = ", ")  # print each genre in 1 line
      print()
      
    if mDeets.Production_Companies == []:  # in the case of an empty list
      print("  Production companies: ")
    else:
      print("  Production companies:", end = " ")
      for pc in mDeets.Production_Companies:
        print(pc, end = ", ")  # print each PC in 1 line
      print()
      
    if mDeets.Tagline == "":
      print("  Tagline: ")   # in the case of no tagline
    else:
      print("  Tagline:", mDeets.Tagline)   # print tagline
      print()

      
#################################################################################
#
# command3
#
# Takes number of movies and minimum reviews as input, outputs the top N movies
#
def command3(dbConn):
  print()
  nMovs = int(input("N? "))  # input
  if nMovs < 1:
    print("Please enter a positive value for N...")  # invalid number for N
    return
  minrevs = int(input("min number of reviews? "))  # input
  if minrevs < 1:
    print("Please enter a positive value for min number of reviews...")  # invalid reviews
    return
  print()
    
  topN = objecttier.get_top_N_movies(dbConn, nMovs, minrevs)   # get topN object
  for x in topN:
    print(x.Movie_ID, ":", x.Title, "("+x.Release_Year+"),", "avg rating =", f"{x.Avg_Rating:.2f}", "("+str(x.Num_Reviews)+" reviews)")  # print results
  print()
      

    
#################################################################################
#
# command4
#
# takes ID and rating as input, then inserts the review
#
def command4(dbConn):
  print()
  rating = int(input("Enter rating (0..10): "))  # input
  if rating < 0 or rating > 10:  # ratings conditions
    print("Invalid rating...")
    return
  mID = int(input("Enter movie id: "))  # input
  func_return = objecttier.add_review(dbConn, mID, rating)  # insert
  if func_return == 0:  # if function returns 0, no movie
    print("\nNo such movie...")
    return
  elif func_return == 1:   # if function returns 1, returns 1 after insert
    print("\nReview successfully inserted")
  print()


#################################################################################
#
# command5
#
# takes ID and tagline as inputs and inserts/updates tagline
#
def command5(dbConn):
  print()
  tag = input("tagline? ")  # input
  mID = int(input("movie id? "))  # input
  func_return = objecttier.set_tagline(dbConn, mID, tag)  # insert/update
  if func_return == 0:  # if function returns 0, no movie
    print("\nNo such movie...")
    return
  elif func_return == 1:  # if function returns 1, insert/update successful
    print("\nTagline successfully set")
  print()


##################################################################
#
# user input loop
#
def user_input_loop(user_input):
    if (user_input == "1"):
      command1(dbConn)
    elif (user_input == "2"):
      command2(dbConn)
    elif (user_input == "3"):
      command3(dbConn)
    elif (user_input == "4"):
      command4(dbConn)
    elif (user_input == "5"):
      command5(dbConn)

##################################################################
#
# main
#
print('** Welcome to the MovieLens app **')
print()
print("General stats:")
print("  # of movies: 45,431")
print("  # of reviews: 100,004")
print()

dbConn = sqlite3.connect('MovieLens.db')

user_input = input("Please enter a command (1-5, x to exit): ")
print()

while(user_input != "x"):
    user_input_loop(user_input)
    user_input = input("Please enter a command (1-5, x to exit): ")