#
# Name:  Harshnandan Dasika
# NetID: hdasik2
# UIN:   652855943
# Description: This project has us making various SQL queries to get intended
#              data values to print out for the user or display in the form of
#              various plots. It  inputs commands from the user and outputs 
#              data from the CTA2 L daily ridership database.
#

import sqlite3
import matplotlib.pyplot as plt


##################################################################
#
# print_stats
#
# Given a connection to the CTA database, executes various
# SQL queries to retrieve and output basic stats.
#
def print_stats(dbConn):
  dbCursor = dbConn.cursor()
  dbCursor2 = dbConn.cursor()
  dbCursor3 = dbConn.cursor()
  dbCursor4 = dbConn.cursor()
  dbCursor4_2 = dbConn.cursor()
  dbCursor5 = dbConn.cursor()
  dbCursor6 = dbConn.cursor()
  dbCursor7 = dbConn.cursor()
  dbCursor8 = dbConn.cursor()

  print("General stats:")

  dbCursor.execute("SELECT count(*) From Stations;")
  row = dbCursor.fetchone()
  print("  # of stations:", f"{row[0]:,}")

  dbCursor2.execute("SELECT count(*) From Stops;")
  row2 = dbCursor2.fetchone()
  print("  # of stops:", f"{row2[0]:,}")

  dbCursor3.execute("SELECT count(*) From Ridership;")
  row3 = dbCursor3.fetchone()
  print("  # of ride entries:", f"{row3[0]:,}")

  dbCursor4.execute("""SELECT strftime('%Y-%m-%d', Ride_Date) as Date from 
                       Ridership group by Date order by Date asc limit 1;""")
  dbCursor4_2.execute("""SELECT strftime('%Y-%m-%d', Ride_Date) as Date from 
                         Ridership group by Date order by Date desc limit 1;""")
  row4 = dbCursor4.fetchone()
  row4_2 = dbCursor4_2.fetchone()
  print("  date range:", f"{row4[0]:}", "-", f"{row4_2[0]}")

  dbCursor5.execute("SELECT sum(Num_Riders) from Ridership;")
  row5 = dbCursor5.fetchone()
  print("  Total ridership:", f"{row5[0]:,}")

  dbCursor6.execute("""SELECT sum(Num_Riders) from Ridership where 
                    Type_of_Day = 'W';""")
  row6 = dbCursor6.fetchone()
  percentage = 100 * row6[0] / row5[0]
  print("  Weekday ridership:", f"{row6[0]:,}", f"({percentage:.2f}%)")

  dbCursor7.execute("""SELECT sum(Num_Riders) from Ridership where 
                    Type_of_Day = 'A';""")
  row7 = dbCursor7.fetchone()
  percentage2 = 100 * row7[0] / row5[0]
  print("  Saturday ridership:", f"{row7[0]:,}", f"({percentage2:.2f}%)")

  dbCursor8.execute("""SELECT sum(Num_Riders) from Ridership where 
                    Type_of_Day = 'U';""")
  row8 = dbCursor8.fetchone()
  percentage3 = 100 * row8[0] / row5[0]
  print("  Sunday/holiday ridership:", f"{row8[0]:,}", f"({percentage3:.2f}%)")


#################################################################################
#
# command1
#
# Inputs a partial station name from the user, searches database
# for matching station names, and outputs those stations.
#
def command1(dbConn):
    print()
    name = input("Enter partial station name (wildcards _ and %): ")
    sql = """SELECT Station_ID, Station_Name from Stations where 
             Station_Name like ? Order By Station_Name;"""

    dbCursor = dbConn.cursor()
    dbCursor.execute(sql, [name])
    rows = dbCursor.fetchall()  # fetch all relevant station names

    if len(rows) == 0:  # if none found
      print("**No stations found...")
      print()
    else:  # if any found
      for row in rows:
        print(row[0], ":", row[1])  # printing in proper format
      print()

    
#################################################################################
#
# command2
#
# Outputs the ridership at each station, in ascending order by station name
#
def command2(dbConn):
    print("** ridership all stations **")
    sql = "SELECT sum(Num_Riders) from Ridership;" # for total ridership
    sql2 = """SELECT Station_Name, sum(Num_Riders) from Ridership join Stations
              on Ridership.Station_ID = Stations.Station_ID 
              group by Ridership.Station_ID order by Station_Name asc;"""

    dbCursor = dbConn.cursor()
    dbCursor.execute(sql)
    rowTRidership = dbCursor.fetchone()  # gets the total ridership
  
    dbCursor2 = dbConn.cursor()
    dbCursor2.execute(sql2)
    rowPerc = dbCursor2.fetchall()  # fetches the individual riderships

    for row in rowPerc:
      num = row[1]
      percentage = 100 * num / rowTRidership[0]  # calculating percentage
      print(row[0], ":", f"{row[1]:,}", f"({percentage:.2f}%)")
    print()

    
#################################################################################
#
# command3
#
# Outputs top-10 busiest stations in terms of ridership, in desc. order by ridership
#
def command3(dbConn):
    print("** top-10 stations **")
    sql = "SELECT sum(Num_Riders) from Ridership;" # for total ridership
    sql2 = """SELECT Stations.Station_Name, sum(Num_Riders) from Ridership join
              Stations on Ridership.Station_ID = Stations.Station_ID 
              group by Station_Name order by sum(Num_Riders) desc limit 10;"""

    dbCursor = dbConn.cursor()
    dbCursor.execute(sql)
    rowTRidership = dbCursor.fetchone()  # gets the total ridership
  
    dbCursor2 = dbConn.cursor()
    dbCursor2.execute(sql2)
    rowPerc = dbCursor2.fetchall()  # gets all 10 biggest stations i.t.o ridership

    for row in rowPerc:
      num = row[1]
      percentage = 100 * num / rowTRidership[0]  # calculating percentage
      print(row[0], ":", f"{row[1]:,}", f"({percentage:.2f}%)")
    print()


#################################################################################
#
# command4
#
# Outputs least-10 busiest stations in terms of ridership, in asc. order by ridership
#
def command4(dbConn):
    print("** least-10 stations **")
    sql = "SELECT sum(Num_Riders) from Ridership;" # for total ridership
    sql2 = """SELECT Stations.Station_Name, sum(Num_Riders) from Ridership join
              Stations on Ridership.Station_ID = Stations.Station_ID 
              group by Station_Name order by sum(Num_Riders) asc limit 10;"""

    dbCursor = dbConn.cursor()
    dbCursor.execute(sql)
    rowTRidership = dbCursor.fetchone()  # gets the total ridership
  
    dbCursor2 = dbConn.cursor()
    dbCursor2.execute(sql2)
    rowPerc = dbCursor2.fetchall()  # gets all 10 smallest stations i.t.o ridership

    for row in rowPerc:
      num = row[1]
      percentage = 100 * num / rowTRidership[0]  # calculating percentage
      print(row[0], ":", f"{row[1]:,}", f"({percentage:.2f}%)")
    print()


#################################################################################
#
# command5
#
# Inputs a line color from the user and outputs all stop names that are part 
# of that line, in ascending order. The stop’s direction is also output, along 
# with whether the station is handicap-accessible or not
#
def command5(dbConn):
    print()
    usr_inp = input("Enter a line color (e.g. Red or Yellow): ")  # user input
    sql = """SELECT Stop_Name, Direction, ADA from Stops join StopDetails on 
             Stops.Stop_ID = StopDetails.Stop_ID join Lines on 
             StopDetails.Line_ID = Lines.Line_ID where Color like ? 
             Order By Stop_Name asc"""

    dbCursor = dbConn.cursor()
    dbCursor.execute(sql, [usr_inp])
    row = dbCursor.fetchall()  # all stop names associated with that line

    if len(row) == 0:  # if none found
      print("**No such line...")
      print()
    else:
      for x in row:
        ada = x[2]
        if (ada == 1):  # check for accessibility
          str1 = "(accessible? yes)"
          print(x[0], ": direction = ", x[1], str1)
        else:
          str2 = "(accessible? no)"
          print(x[0], ": direction = ", x[1], str2)                
      print()


#################################################################################
#
# command6
#
# Outputs total ridership by month, in ascending order by month. After the 
# output, the user is given the option to plot the data
#
def command6(dbConn):
    print("** ridership by month **")
    sql = """SELECT strftime('%m', Ride_Date) as Month, sum(Num_Riders) 
             from Ridership group by Month order by Month asc;"""

    dbCursor = dbConn.cursor()
    dbCursor.execute(sql)
    row = dbCursor.fetchall()   # all ridership sorted by month

    for r in row:
        print(r[0], ":", f"{r[1]:,}")  # print out details of each row
    print()
    
    usr_inp = input("Plot? (y/n) ")
    print()
    if (usr_inp == "y"):
        x = [] # create 2 empty vectors/lists
        y = []
        for r in row: # append each (x, y) coordinate that you want to plot
            x.append(r[0])
            y.append(r[1])
            plt.xlabel("month")
            plt.ylabel("number of riders (x * 10^8)")
            plt.title("monthly ridership")
            plt.plot(x, y)
            plt.show()
        print()
    else:
        return


#################################################################################
#
# command7
#
# Outputs total ridership by month, in ascending order by year. After the 
# output, the user is given the option to plot the data
#
def command7(dbConn):
    print("** ridership by year **")
    sql = """SELECT strftime('%Y', Ride_Date) as Year, sum(Num_Riders) 
             from Ridership group by Year order by Year asc;"""
    
    dbCursor = dbConn.cursor()
    dbCursor.execute(sql)
    row = dbCursor.fetchall()   # all ridership sorted by year
    
    for r in row:
        print(r[0], ":", f"{r[1]:,}")  # print out details of each row
    print()
    
    usr_inp = input("Plot? (y/n) ")
    print()
    if (usr_inp == "y"):
        x = [] # create 2 empty vectors/lists
        y = []
        for r in row: # append each (x, y) coordinate that you want to plot
            x.append(r[0][2:4])
            y.append(r[1])
            plt.xlabel("year")
            plt.ylabel("number of riders (x * 10^8)")
            plt.title("yearly ridership")
            plt.plot(x, y)
            plt.show()
        print()
    else:
        return


#################################################################################
#
# command8
#
# Inputs a year and the names of two stations (full or partial names), and then 
# outputs the daily ridership at each station for that year
#
def command8(dbConn):
    print()
    yr_inp = input("Year to compare against? ")  # user year input
    print()
    
    st1_inp = input("Enter station 1 (wildcards _ and %): ")  # first station
    sql = "SELECT Station_ID, Station_Name from Stations where Station_Name like ?"
    sql2 = """SELECT strftime('%Y-%m-%d', Ride_Date), sum(Num_Riders) from 
              Ridership join Stations on Ridership.Station_ID = Stations.Station_ID 
              where Station_Name like ? group by Ride_Date order by Ride_Date asc"""
    
    dbCursor = dbConn.cursor()
    dbCursor.execute(sql, [st1_inp])
    row1 = dbCursor.fetchall()  # associated station ID and name
    dbCursor2 = dbConn.cursor()
    dbCursor2.execute(sql2, [st1_inp])
    row2 = dbCursor2.fetchall()   # all ridership info at station1 during year

    if(len(row1) > 1):
        print("**Multiple stations found...")
        return
    elif(len(row1) < 1):
        print("**No station found...")
        return
    else:
        print()
        st2_inp = input("Enter station 2 (wildcards _ and %): ")
    dbCursor3 = dbConn.cursor()
    dbCursor3.execute(sql, [st2_inp])
    row3 = dbCursor3.fetchall()  # associated station ID and name
    dbCursor4 = dbConn.cursor()
    dbCursor4.execute(sql2, [st2_inp])
    row4 = dbCursor4.fetchall()  # all ridership info at station2 during year
    if(len(row3) > 1):
        print("**Multiple stations found...")
        return
    elif(len(row3) < 1):
        print("**No station found...")
        return
    else:
        print("Station 1:", row1[0][0], row1[0][1])  # month and ridership
        st1_rows = []
        for r in row2:
            if(yr_inp in r[0]):
                st1_rows.append(r)
        st1_output = st1_rows[0:5] + st1_rows[-5:]  # first 5, last 5
        for x in st1_output:
            print(f"{x[0]} {x[1]}")
        print("Station 2:", row3[0][0], row3[0][1])  # month and ridership
        st2_rows = []
        for r in row4:
            if(yr_inp in r[0]):
                st2_rows.append(r)
        st2_output = st2_rows[0:5] + st2_rows[-5:]  # first five, last five
        for x in st2_output:
            print(f"{x[0]} {x[1]}")
        print()
        plot_inp = input("Plot? (y/n)")
        print()
        if(plot_inp == "y"):
            day1 = 0
            day2 = 0
            x = [] # create 2 empty vectors/lists
            y = []
            for r in st1_rows: # append each (x, y) coordinate that you want to plot
                x.append(day1)
                y.append(r[1])
                day1 += 1
            x2 = []
            y2 = []
            for r in st2_rows: # append each (x, y) coordinate that you want to plot
                x2.append(day2)
                y2.append(r[1])
                day2 += 1
            plt.xlabel("day")
            plt.ylabel("number of riders")
            plt.title("riders each day of " + yr_inp)
            plt.plot(x, y, "#156aa8", label= row1[0][1])
            plt.plot(x2, y2, "#dc732e", label = row3[0][1])
            plt.legend()
            plt.show()
        else:
            return
    print()
    

#################################################################################
#
# command9
#
# Inputs a line color from the user and output all station names that are 
# part of that line, in ascending order
#
def command9(dbConn):
    print()
    color = input("Enter a line color (e.g. Red or Yellow): ")
    sql = """SELECT DISTINCT Station_Name, Latitude, Longitude from Stops 
             join Stations on Stops.Station_ID = Stations.Station_ID 
             join StopDetails on Stops.Stop_ID = StopDetails.Stop_ID 
             join Lines on StopDetails.Line_ID = Lines.Line_ID where Color like ? 
             Order By Station_Name asc"""
    dbCursor = dbConn.cursor()
    dbCursor.execute(sql, [color])
    row = dbCursor.fetchall()  # all associated stops for that line
  
    if(len(row) < 1):
        print("**No such line...")  
        return
    else:
        for r in row:
            latLong = (r[1], r[2])
            print(r[0], ":", latLong)
        print()

        plot_inp = input("Plot? (y/n) ")
        print()
        if(plot_inp == "y"):
            #
            # populate x and y lists with (x, y) coordinates --- note that longitude
            # are the X values and latitude are the Y values
            #
            x = []
            y = []
            for r in row: # append each (x, y) coordinate that you want to plot
                x.append(r[2])
                y.append(r[1])

            image = plt.imread("chicago.png")
            xydims = [-87.9277, -87.5569, 41.7012, 42.0868] # area covered by the map:
            plt.imshow(image, extent=xydims)

            plt.title(color + " line")
            #
            # color is the value input by user, we can use that to plot the
            # figure *except* we need to map Purple-Express to Purple:
            #
            if (color.lower() == "purple-express"):
                color="Purple" # color="#800080"

            plt.plot(x, y, "o", c=color)
            #
            # annotate each (x, y) coordinate with its station name: #
            for r in row:
                plt.annotate(r[0], (r[2], r[1]))

            plt.xlim([-87.9277, -87.5569])
            plt.ylim([41.7012, 42.0868])

        plt.show()

##################################################################
#
# user input loop
#
def user_input_loop(user_input):
    # go to the correct command based on input
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
    elif (user_input == "6"):
      command6(dbConn)
    elif (user_input == "7"):
      command7(dbConn)
    elif (user_input == "8"):
      command8(dbConn)
    elif (user_input == "9"):
      command9(dbConn)
    else:
      print("**Error, unknown command, try again...", end = '\n\n')


##################################################################
#
# main
#
print('** Welcome to CTA L analysis app **')
print()

dbConn = sqlite3.connect('CTA2_L_daily_ridership.db')

print_stats(dbConn)
print()
user_input = input("Please enter a command (1-9, x to exit): ")
while(user_input != "x"):
    user_input_loop(user_input)
    user_input = input("Please enter a command (1-9, x to exit): ")

#
# done
#
