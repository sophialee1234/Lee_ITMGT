#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    who_from_member_follows = social_graph[from_member]["following"]
    who_to_member_follows = social_graph[to_member]["following"]
    
    if to_member in who_from_member_follows and from_member in who_to_member_follows:
        return("friends")
    elif to_member in who_from_member_follows:
        return("follower")
    elif from_member in who_to_member_follows:
        return("followed by")
    else:
        return("no relationship")


# In[ ]:





# In[ ]:


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # horizontal
    z = []
    for x in range(0,len(board)):
        z.append(board[x])

    # vertical
    z1 = []
    z2 = []
    z3 = []
    z4 = []
    z5 = []
    z6 = []
    for a in range(0,len(board)):
        z1.append(board[a][0])
    for a in range(0,len(board)):
        z2.append(board[a][1])
    for a in range(0,len(board)):
        z3.append(board[a][2])
    z.append(z1)
    z.append(z2)
    z.append(z3)
    if len(board) >= 4:
        for a in range(0,len(board)):
            z4.append(board[a][3])
        z.append(z4)
    if len(board) >= 5:
        for a in range(0,len(board)):
            z5.append(board[a][4])
        z.append(z5)
    if len(board) >= 6:
        for a in range(0,len(board)):
            z6.append(board[a][5])
        z.append(z6)

    # diagonal 1
    otherz = []
    for m in range(0,len(board)):
        otherz.append(board[m][m])
    z.append(otherz)

    # diagonal 2
    lastz = []
    if len(board)%2==1:
        lastz.append(board[int((len(board)-1)/2)][int((len(board)-1)/2)])
        lastz.append(board[len(board)-1][0])
        lastz.append(board[0][len(board)-1])
        if len(board)==5:
            lastz.append(board[1][len(board)-2])
            lastz.append(board[len(board)-2][1]) 
    if len(board)%2==0:
        lastz.append(board[len(board)-1][0])
        lastz.append(board[0][len(board)-1])
        lastz.append(board[len(board)-2][1])
        lastz.append(board[1][len(board)-2])
        if len(board)==6:
            lastz.append(board[2][len(board)-3])
            lastz.append(board[len(board)-3][2])
    z.append(lastz)

    answer = " "
    for a in range(0,len(z)):
        if z[a].count("X")==len(board):
            answer = "X"
        elif z[a].count("O")==len(board):
            answer = "O"

    if answer != "X" and answer != "O":
        return("NO WINNER")
    elif answer == "X":
        return("X")
    elif answer == "O":
        return("O")


# In[ ]:





# In[ ]:


def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    keys = list(route_map.keys())
    values = list(route_map.values())

    for i in range(0,len(route_map)):
        if keys[i][0]==first_stop:
            start_index = int(i)
    for e in range(0,len(route_map)):
        if keys[e][1]==second_stop:
            destination_index = int(e)

    if start_index==destination_index:
        return(route_map[(first_stop,second_stop)]["travel_time_mins"])
    if start_index<destination_index:
        listt = []
        for w in range(start_index,destination_index+1):
            listt.append(values[w]["travel_time_mins"])
        return(sum(listt))
    if start_index>destination_index:
        n = destination_index - start_index
        listtt = []
        for y in range(start_index,len(route_map)):
            listtt.append(values[y]["travel_time_mins"])
        for z in range(0,destination_index+1):
            listtt.append(values[z]["travel_time_mins"])
        return(sum(listtt))


# In[ ]:




