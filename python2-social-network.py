#! /usr/bin/python

# Michael Cullen 2020

# ------------------------------------------------------------------------------
# Example string input. It is used here to test the code below.

example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."


# -----------------------------------------------------------------------------
# create_data_structure(string_input):
#   Parses a block of text (such as the one above) and stores relevant
#   information into a data structure. The data structure used is a dictionary
#   with dictionaries for (hopefully) better scalability.
#
# Arguments:
#   string_input: block of text containing the network information
#       (in the format as specified in the 'example_input' block of text as above)
#
# Return:
#   The newly created network data structure, or if the input is an empty string, will return
#   a network with no users.

def create_data_structure(string_input):
    # the following 5 lines of code change the string into a list (named 'newlist') for processing
    newlist = []
    while string_input != '':
        split_point = string_input.find('.', string_input.find('.') + 1)
        newlist.append(string_input[:split_point + 1])
        string_input = string_input[split_point + 1:]
    # now below the list is processed - user names, friends lists and games played are extracted from
    # this list and added to a new data structure named 'network' - the new data structure is of
    # dictionaries within dictionaries for ease of retrieval of user information and for further analysis
    string_A = ' is connected to '
    string_B = 'likes to play '
    x = 0
    network = {}
    for element in newlist:
        user = newlist[x][:newlist[x].find(string_A)]
        network[user] = {}
        friends_list = newlist[x][newlist[x].find(string_A) + len(string_A) : newlist[x].find('.')].split(', ')
        network[user]['friends'] = friends_list
        games_list = newlist[x][newlist[x].find(string_B) + len(string_B) : -1].split(', ')
        network[user]['games'] = games_list
        x = x + 1
    return network


# ----------------------------------------------------------------------------- #
# Note that the first argument to all procedures below is 'network' This is the #
# data structure created with your create_data_structure procedure,             #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        #
# ----------------------------------------------------------------------------- #


# -----------------------------------------------------------------------------
# get_connections(network, user):
#   Returns a list of all the connections that user has
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.

def get_connections(network, user):
    if user not in network:
        print 'ERROR: User with name ' + "'" + user + "'" + ' not found in the network.'
        return
    elif not network.get(user).get('friends'):
        print 'No connections found for ' + user +'. Returning an empty list:'
        return []
    else:
        return network[user]['friends']


# -----------------------------------------------------------------------------
# get_games_liked(network, user):
#   Returns a list of all the games a user likes
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.

def get_games_liked(network, user):
    if user not in network:
        print 'ERROR: User with name ' + "'" + user + "'" + ' not found in the network. Please try a different name.'
        return
    elif not network.get(user).get('games'):
        print 'No games found for ' + user +'. Returning an empty list:'
        return []
    else:
        print user + ' likes ' + str(len(network[user]['games'])) + ' games: '
        return network[user]['games']


# -----------------------------------------------------------------------------
# add_new_user(network, user, games):
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assumes that the user has no
#   connections to begin with.
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return:
#   The updated network with the new user and game preferences added. The new user
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (does not change
#     the user's game preferences)


def add_new_user(network, user, games):
        if not user:
            print 'No name entered!'
            return network
        if user in network:
            print '*UNCHANGED*'
            print 'Attempt to add new user failed - username already exists.'
            return network
        else:
            network[user] = {}
            network[user]['games'] = games
            network[user]['friends'] = []
            return network


# -----------------------------------------------------------------------------
# add_connection(network, user_A, user_B):
#   Adds a connection from user_A to user_B. Make sure to check that both users
#   exist in network.
#
# Arguments:
#   network: the gamer network data structure
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return:
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.

def add_connection(network, user_A, user_B):
    if user_A not in network:
        print 'ERROR: User with name ' + "'" + user_A + "'" + ' not found in the network. Please try a different name.'
        return False
    elif user_B not in network:
        print 'ERROR: User with name ' + "'" + user_B + "'" + ' not found in the network. Please try a different name.'
        return False
    else:
        if network[user_A].get('friends') == None:
            return 'Network Error'
        connections = get_connections(network, user_A)
        for connection in connections:
            if connection == user_B:
                return 'ERROR: Attempt to add new connection failed - connection already exists. Network unchanged.'
        network[user_A]['friends'] = network[user_A]['friends'] + [user_B]
        print 'Connection Added! ' + user_B + ' is now one of ' + user_A + '\'s connections:'
        print ''
        print user_A + '\'s Connections:', network[user_A]['friends']
        print ''
        print 'Network Updated!'
        print ''
        return network


# -----------------------------------------------------------------------------
# get_secondary_connections(network, user):
#   Finds all the secondary connections (i.e. connections of connections) of a
#   given user.
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.

def get_secondary_connections(network, user):
    if user not in network:
        print 'ERROR: User with name ' + "'" + user + "'" + ' not found in the network.'
        return None
    elif not network.get(user).get('friends'):
        print 'No primary or secondary connections found for ' + user +'.'
        return []
    else:
        newlist = get_connections(network, user)
        temp_list = []
        sec_list = []
        final_list = []
        for connection in newlist:
            temp_list = get_connections(network, connection)
            sec_list = sec_list + temp_list
        for connection in sec_list:
            if connection not in final_list:
                final_list.append(connection)
        return final_list


# -----------------------------------------------------------------------------
# connections_in_common(network, user_A, user_B):
#   Finds the number of people that user_A and user_B have in common.
#
# Arguments:
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return:
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.


def connections_in_common(network, user_A, user_B):
    if user_A not in network:
        print 'ERROR: User with name ' + "'" + user_A + "'" + ' not found in the network. Please try a different name.'
        return False
    elif user_B not in network:
        print 'ERROR: User with name ' + "'" + user_B + "'" + ' not found in the network. Please try a different name.'
        return False
    else:
        list_A = get_connections(network, user_A)
        list_B = get_connections(network, user_B)
        shared_connections = []
        for user in list_B:
            if user in list_A:
                shared_connections.append(user)
        print user_A + ' and ' + user_B + ' have ' + str(len(list_A)) + ' connections in common:'
        return len(shared_connections)


# -----------------------------------------------------------------------------
# path_to_friend(network, user_A, user_B, nodes_visited=None):
#   Finds a connections path from user_A to user_B. It has to be an existing
#   path but is not necessarily the shortest path. Contains a default parameter
#   to keep track of nodes already visited in the search.
#
# Arguments:
#   network: The network created with create_data_structure.
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
#   nodes_visited=None: A default parameter to keep track of nodes already visited
#
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam,
#   who is connected with Zed.

def path_to_friend(network, user_A, user_B, nodes_visited=None):
    if user_A not in network:
        print 'ERROR: User with name ' + "'" + user_A + "'" + ' not found in the network. Please try a different name.'
        return
    elif user_B not in network:
        print 'ERROR: User with name ' + "'" + user_B + "'" + ' not found in the network. Please try a different name.'
        return
    else:
        if not nodes_visited:
            nodes_visited = []
        nodes_visited = nodes_visited + [user_A]
        if user_A == user_B:
            return nodes_visited
        if user_B in get_connections(network, user_A):
            return nodes_visited + [user_B]
        if user_A not in network or user_B not in network:
            return
        for connection in get_connections(network, user_A):
            if connection not in nodes_visited:
                results = path_to_friend(network, connection, user_B, nodes_visited)
                if results != None:
                    return results
        return


# -----------------------------------------------------------------------------
# popularity_of_each_game(network):
#
#   Shows the popularity of games by listing the games stored in the network,
#   along with the number of users that play each game.
#
# Arguments:
#   network: the gamer network data structure
#
# Return:
#   Returns None if the network is an empty dictionary, or if the network is an empty string,
#   otherwise prints one each line the number of users that play a specific game, together with
#   the game itself -thereby showing the popularity of each game in the network.
#   It only returns a series of dashes that form a dividing line for use with the menu() procedure.
#   In the case of an empty data structure, the procedure returns 'None'.
#

def popularity_of_each_game(network):
    if not network:
        return
    new_list = []
    for e in network:
        new_list = new_list + get_games_liked(network, e)
    new_list = dict((i,str(new_list.count(i)) + ' users play ->') for i in new_list)
    popularity_list = None
    print '-------------------------------'  # for use with the menu() procedure
    for item in new_list:
        popularity_list = new_list[item], item
        print popularity_list
    return '-------------------------------'


# -----------------------------------------------------------------------------
# show_all_users(network):
#
#   Displays a single column list with the intention of clearly showing all users in the network.
#   Created so as to more easily display each user - making it easier
#   to select individual users while using the interactive menu.
#
# Arguments:
#   network: the gamer network data structure
#
# Return:
#   Prints each user on a single line. This was designed for use with the menu()
#   procedure below. The reason for creating this list was to permit easy viewing of all current users
#   in order to more comfortably make changes / additions to the network via the menu commands in the menu() procedure.
#   It only returns a series of dashes that form a dividing line for use with the menu() procedure.
#   It also prints the total number of users in the network, expressed as an integer.
#   In the case of an empty data structure, the procedure returns 'None'.
#

def show_all_users(network):
    if not network:
        return
    number_of_users = 0
    for user in network:
        print user
        number_of_users += 1
    print '-------------------------------'
    print '(' + str(number_of_users), 'users in total)'
    return '-------------------------------'


# -----------------------------------------------------------------------------
# popularity_of_each_user(network):
#
#   Shows the popularity of users by listing each user within the network,
#   together with the number of connections each user has.
#
# Arguments:
#   network: the gamer network data structure
#
# Return:
#   Prints each username on a new line, together with an integer representing the number of users
#   connected to that user. It therefore displays a basic form of popularity of each individual user.
#   It only returns a series of dashes that form a dividing line for use with the menu() procedure.
#   In the case of an empty data structure, the procedure returns 'None'.
#

def popularity_of_each_user(network):
    if not network:
        return
    new_list = []
    for user in network:
        new_list = new_list + get_connections(network, e)
        # new_list = new_list + network[e]['friends']
    new_list = dict((i ,str(new_list.count(i))) for i in new_list)
    print '--------------------------------'
    for item in new_list:
        print 'The number of unique users that are friends with', item, 'is:', new_list[item]
    return '-------------------------------'


# -----------------------------------------------------------------------------
# user_with_friends_list(network):
#
#   For convenient viewing, shows a list of all users within the network, together
#   with their associated connections/friends.
#
# Arguments:
#   network: the gamer network data structure
#
# Return:
#   Prints each username on a single line, together with a list of that user's connections / friends.
#   It only returns a series of dashes that form a dividing line for use with the menu() procedure.
#   In the case of an empty data structure, the procedure returns 'None'.
#

def user_with_friends_list(network):
    if not network:
        return
    print '--------------------------------'
    for user in network:
        print user, 'is friends with:', get_connections(network, user)
    return '-------------------------------'



# -----------------------------------------------------------------------------
# user_with_games_list(network):
#
#   For convenient viewing, shows a list of all users within the network, together
#   with their associated games.
#
# Arguments:
#   network: the gamer network data structure
#
# Return:
#   Prints each user on a single line, together with a list of that user's games.
#   It only returns a series of dashes that form a dividing line for use with the menu() procedure.
#   In the case of an empty data structure, the procedure returns 'None'.
#

def user_with_games_list(network):
    if not network:
        return
    print '--------------------------------'
    for user in network:
        print user, 'likes to play:', network[user]['games'] # <-- get_games_liked(network, user) was
    return '-------------------------------'                 # deliberately not used here, since the
                                                             # get_games_liked procedure also returns
                                                             # some string that clashes with the string used
                                                             # in this procedure.




# An Interactive Menu for accessing all functions. 
# -----------------------------------------------------------------------------
# menu():
#
#   Displays a menu with 14 options. The first 12 options access the various procedures
#   that have been defined in this project. Option 13 shows the resources that assisted
#   me in the creation of this project, and option 14 exits the menu.
#   Please uncomment 'menu()' on the last line of code in this file, to enable the menu.
#   I decided to make this menu procedure in order to learn more about working with user
#   input - raw_input(), for instance, and enjoyed making it!
#
# Arguments:
#   No arguments are passed into the procedure.
#
# Return:
#   The menu() procedure returns upon itself, so that after each round of user input, the main
#   menu displays again. Option 14 allows the user to exit the menu.



def menu():
    print """
    PLEASE SELECT FROM ONE OF THE FOLLOWING OPTIONS:

    1.  DISPLAY THE ENTIRE CONTENTS OF THE NETWORK
    2.  SHOW A SIMPLE LIST OF ALL REGISTERED USERS
    3.  DISPLAY THE CONNECTIONS OF A SPECIFIC USER
    4.  SHOW THE GAMES LIST OF A SPECIFIC USER
    5.  ADD A NEW USER TO THE NETWORK
    6.  ADD A NEW CONNECTION TO AN EXISTING USER
    7.  SHOW THE SECONDARY CONNECTIONS OF A USER
    8.  SHOW A LIST OF THE CONNECTIONS IN COMMON BETWEEN TWO UNIQUE USERS
    9.  DISPLAY THE CONNECTION PATHWAY BETWEEN TWO USERS
    10. DISPLAY THE POPULARITY OF EACH GAME IN THE NETWORK
    11. LIST USERS AND THEIR FAVOURITE GAMES
    12. SHOW USERS TOGETHER WITH THEIR PRIMARY CONNECTIONS
    13. LIST OF RESOURCES USED
    14. EXIT THIS MENU
    """
    while True:
        try:
            selection = int(raw_input('>>> '))
        except ValueError:
            print 'That is not a valid entry.'
            print 'Please enter a number between 1 and 14 as listed above:'
        else:
            if 1 <= selection < 15:
                if selection == 1:
                    print '-------------------------------'
                    print 'THE ENTIRE CONTENTS OF THE NETWORK:'
                    print '-------------------------------'
                    print network
                    print '-------------------------------'
                    raw_input("Press ENTER to return to the main menu...")
                    break
                if selection == 2:
                    print '-------------------------------'
                    print 'A SIMPLE LIST OF ALL REGISTERED USERS:'
                    print '-------------------------------'
                    print show_all_users(network)
                    raw_input("Press ENTER to return to the main menu...")
                    break
                if selection == 3:
                    print '-------------------------------'
                    print 'THE CONNECTIONS OF A SPECIFIC USER:'
                    print '-------------------------------'
                    print show_all_users(network)
                    user = raw_input('Type a username from the list above to show current connections: ')
                    print ''
                    print get_connections(network, user)
                    print ''
                    raw_input("Press ENTER to return to the main menu...")
                    break
                if selection == 4:
                    print '-------------------------------'
                    print 'THE GAMES OF A SPECIFIC USER:'
                    print '-------------------------------'
                    print show_all_users(network)
                    user = raw_input('Type a username from the list above to show the games a user likes: ')
                    print ''
                    print get_games_liked(network, user)
                    print ''
                    raw_input("Press ENTER to return to the main menu...")
                    break
                if selection == 5:
                    print '-------------------------------'
                    print 'ADD A NEW USER TO THE NETWORK:'
                    print '-------------------------------'
                    print show_all_users(network)
                    print 'CREATE A NEW USER:'
                    user = raw_input('Please type a new username different from those in the above list: ')
                    print ''
                    games = []
                    while True:
                        next_game = raw_input('Would you like to add a game for ' + user + ' (type yes or no):')
                        if next_game == 'yes':
                            games.append(raw_input('Please type the name of a game you would like to add:'))
                        else:
                            break
                    add_new_user(network, user, games)
                    print ''
                    raw_input("Press ENTER to return to the main menu...")
                    break
                if selection == 6:
                    print '-------------------------------'
                    print 'ADD A NEW CONNECTION TO AN EXISTING USER:'
                    print '-------------------------------'
                    print show_all_users(network)
                    user_A = raw_input('Type a username you would like to add as a connection: ')
                    user_B = raw_input('Type the name of a user you would like to add ' + user_A + ' to: ')
                    print ''
                    print add_connection(network, user_A, user_B)
                    print ''
                    print ''
                    raw_input("Press ENTER to return to the main menu...")
                    break
                if selection == 7:
                    print '-------------------------------'
                    print 'FIND THE SECONDARY CONNECTIONS OF A USER:'
                    print '-------------------------------'
                    print show_all_users(network)
                    user = raw_input('Type a username from the list above to show the secondary connections of the user: ')
                    print ''
                    print 'The secondary connections of ' + user + ' are:', get_secondary_connections(network, user)
                    print ''
                    raw_input("Press ENTER to return to the main menu...")
                    break
                if selection == 8:
                    print '-------------------------------'
                    print 'SHOW A LIST OF CONNECTIONS IN COMMON BETWEEN TWO USERS:'
                    print '-------------------------------'
                    print show_all_users(network)
                    user_A = raw_input('Please type the first username: ')
                    user_B = raw_input('Please type the second username: ')
                    print ''
                    print connections_in_common(network, user_A, user_B)
                    print ''
                    print ''
                    raw_input("Press ENTER to return to the main menu...")
                    break
                if selection == 9:
                    print '-------------------------------'
                    print 'DISPLAY THE CONNECTION PATHWAY BETWEEN TWO USERS:'
                    print '-------------------------------'
                    print show_all_users(network)
                    user_A = raw_input('Please type the first username: ')
                    user_B = raw_input('Please type the second username: ')
                    print ''
                    print path_to_friend(network, user_A, user_B, nodes_visited=[])
                    print ''
                    print ''
                    raw_input("Press ENTER to return to the main menu...")
                    break
                if selection == 10:
                    print '-------------------------------'
                    print 'THE POPULARITY OF EACH GAME IN THE NETWORK:'
                    print popularity_of_each_game(network)
                    print ''
                    raw_input("Press ENTER to return to the main menu...")
                    break
                if selection == 11:
                    print '--------------------------------'
                    print 'LIST USERS AND THEIR FAVOURITE GAMES:'
                    print user_with_games_list(network)
                    print ''
                    raw_input("Press ENTER to return to the main menu...")
                    break
                if selection == 12:
                    print '--------------------------------'
                    print 'SHOW USERS TOGETHER WITH THEIR PRIMARY CONNECTIONS:'
                    print user_with_friends_list(network)
                    print ''
                    raw_input("Press ENTER to return to the main menu...")
                    break
                if selection == 13:
                    print '-------------------------------'
                    print 'RESOURCES USED:'
                    print '-------------------------------'
                    print 'Learn Python The Hard Way'
                    print 'http://learnpythonthehardway.org/'
                    print ''
                    print 'Stack Overflow'
                    print 'http://stackoverflow.com/'
                    print ''
                    print 'Python.Org - Python 2.7.9 Documentation'
                    print 'https://docs.python.org/2/'
                    print ''
                    print '(the eff-bot guide to) The Standard Python Library'
                    print 'http://effbot.org/zone/librarybook-index.htm'
                    print ''
                    print 'Online Python Tutor'
                    print 'http://www.pythontutor.com/'
                    print ''
                    print 'The Hitchhiker\'s Guide to Python!'
                    print 'http://docs.python-guide.org/en/latest/'
                    print ''
                    print 'How To Think Like a Computer Scientist: Interactive Edition'
                    print 'http://interactivepython.org/'
                    print ''
                    print 'Repl.It'
                    print 'http://repl.it/'
                    print ''
                    print 'Python Practice Book'
                    print 'http://anandology.com/python-practice-book/index.html'
                    print ''
                    print 'Open Book Project'
                    print 'http://openbookproject.net/'
                    print ''
                    print 'Tutorials Point'
                    print 'http://www.tutorialspoint.com/python/'
                    print ''
                    print 'Python Course'
                    print 'http://www.python-course.eu/'
                    print ''
                    print 'Dot Net Perls'
                    print 'http://www.dotnetperls.com/python'
                    print ''
                    print 'Dive into Python'
                    print 'http://www.diveintopython.net/'
                    print ''
                    print 'Quora'
                    print 'http://www.quora.com/'
                    print ''
                    print 'InformIT'
                    print 'http://www.informit.com/'
                    print ''
                    print 'Code Review Stack Exchange'
                    print 'http://codereview.stackexchange.com/'
                    print ''
                    print 'Python Central'
                    print 'http://www.pythoncentral.io/'
                    print ''
                    raw_input("Press ENTER to return to the main menu...")
                    print ''
                    break
                if selection == 14:
                    return 'Exiting Menu'
            else:
                print 'Please enter a number between 1 and 14 as listed above:'

    return menu()




# The menu() procedure can be tested with an existing data structure:
# network = create_data_structure(example_input)
# Uncomment the two lines immediately below to test:
# network = {}
# menu()


# Or the menu() procedure can be tested with an empty data structure. New information can
# be added to the structure through the menu.
# Uncomment the two lines immediately below to test:
network = {}
menu()
