# Build a dictionary containing the specified movie collection
movieDict = {"Munich": [2005, "Steven Spielberg"],
             "The Prestige": [2006, "Christopher Nolan"],
             "The Departed": [2006, "Martin Scorsese"],
             "Into the Wild": [2007, "Sean Penn"],
             "The Dark Knight": [2008, "Christopher Nolan"],
             "Mary and Max": [2009, "Adam Elliot"],
             "The King\'s Speech": [2010, "Tom Hooper"],
             "The Artist": [2011, "Michel Hazanavicius"],
             "The Help": [2011, "Tate Taylor"],
             "Argo": [2012, "Ben Affleck"],
             "12 Years a Slave": [2013, "Steve McQueen"],
             "Birdman": [2014, "Alejandro G. Inarritu"],
             "Spotlight": [2015, "Tom McCarthy"],
             "The BFG": [2016, "Steven Spielberg"]}

# Prompt the user for a year
# Displaying the title(s) and directors(s) from that year
promptForYear = True
while promptForYear:
    yearChoice = int(input('Enter a year between 2005 and 2016:\n'))
    if yearChoice < 2005 or yearChoice > 2016:
        print('N/A')
    else:
        for key, value in movieDict.items():
            if value[0] == yearChoice:
                print(key + ", " + str(value[1]))
        promptForYear = False

# Display menu
# Carry out the desired option: Display movies by year,
# display movies by director, display movies by movie title, or quit
menu = 'MENU' \
       '\nSort by:' \
       '\ny - Year' \
       '\nd - Director' \
       '\nt - Movie title' \
       '\nq - Quit\n'
promptUser = True
first_time = True
while promptUser:
    if first_time == True:
        print()
        first_time = False
    print(menu)
    userChoice = input('Choose an option:\n')
    if userChoice == 'q':
        promptUser = False
    elif userChoice == 'y':
        year_sorted = {}
        for key, value in sorted(movieDict.items(), key=lambda item: (item[1], item[0])):
            year = value[0]
            title = key
            director = value[1]
            if year not in year_sorted:
                year_sorted[year] = [[title, director]]
            else:
                year_sorted[year].append([title, director])
        for year in sorted(year_sorted):
            print(year, end=':\n')
            movies = year_sorted[year]
            if year != 2006:
                for movie in sorted(movies, key=lambda x: x[0]):
                    print('\t' + movie[0] + ', ' + movie[1])
                print()
            else:
                yr = year_sorted[2006]
                print('\t' + yr[0][0] + ', ' + yr[0][1])
                print('\t' + yr[1][0] + ', ' + yr[1][1])
                print()
    elif userChoice == 'd':
        director_sorted = {}
        for key, value in sorted(movieDict.items(), key=lambda item: (item[1][1])):
            year = value[0]
            title = key
            director = value[1]
            if director not in director_sorted:
                director_sorted[director] = [[title, year]]
            else:
                director_sorted[director].append([title, year])
        for director in sorted(director_sorted):
            print(director, end=':\n')
            movies = director_sorted[director]
            if director != 'Christopher Nolan':
                for movie in sorted(movies, key=lambda x: x[0]):
                    print('\t' + movie[0] + ', ' + str(movie[1]))
                print()
            else:
                nolan = director_sorted['Christopher Nolan']
                print('\t' + nolan[0][0] + ', ' + str(nolan[0][1]))
                print('\t' + nolan[1][0] + ', ' + str(nolan[1][1]))
                print()
    elif userChoice == 't':
        for key, value in sorted(movieDict.items(), key=lambda item: (item[0], item[1])):
            print(key, end=':\n')
            print('\t' + str(value[1]) + ', ' + str(value[0]) + '\n')
    else:
        print("Invalid input")
