#empyty spot will be 0, players piece will be 1, computer piece will be 2





#function to calculate how good the board position is:
def value(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    board = [[a3, b3, c3],
             [a2, b2, c2],
             [a1, b1, c1]]
    value = 0
    for i in range(0, 2):
        for j in range(0, 2):
            if (board[i][j] == 1 & board[i][j+1] == 1):
                value = value - 2
            if (board[i][j] == 1 & board[i][j-1] == 1):
                value = value - 2
            if (board[i][j] == 1 & board[i+1][j] == 1):
                value = value - 2
            if (board[i][j] == 1 & board[i-1][j] == 1):
                value = value - 2
            if (board[i][j] == 1 & board[i+1][j+1] == 1):
                value = value - 2
            if (board[i][j] == 1 & board[i+1][j-1] == 1):
                value = value - 2
            if (board[i][j] == 1 & board[i-1][j+1] == 1):
                value = value - 2
            if (board[i][j] == 1 & board[i-1][j-1] == 1):
                value = value - 2
            if (board[i][j] == 2 & board[i][j+1] == 2):
                value = value + 1
            if (board[i][j] == 2 & board[i][j-1] == 2):
                value = value + 1
            if (board[i][j] == 2 & board[i+1][j] == 2):
                value = value + 1
            if (board[i][j] == 2 & board[i-1][j] == 2):
                value = value + 1
            if (board[i][j] == 2 & board[i+1][j+1] == 2):
                value = value + 1
            if (board[i][j] == 2 & board[i+1][j-1] == 2):
                value = value + 1
            if (board[i][j] == 2 & board[i-1][j+1] == 2):
                value = value + 1
            if (board[i][j] == 2 & board[i-1][j-1] == 2):
                value = value + 1
    return value





#function to determine best position:
def bestposition(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    pos_list = []
    move_list = []
    if (a1 == 0):
        pos_list.append(value(2, a2, a3, b1, b2, b3, c1, c2, c3))
        move_list.append('a1')
    if (a2 == 0):
        pos_list.append(value(a1, 2, a3, b1, b2, b3, c1, c2, c3))
        move_list.append('a2')
    if (a3 == 0):
        pos_list.append(value(a1, a2, 2, b1, b2, b3, c1, c2, c3))
        move_list.append('a3')
    if (b1 == 0):
        pos_list.append(value(a1, a2, a3, 2, b2, b3, c1, c2, c3))
        move_list.append('b1')
    if (b2 == 0):
        pos_list.append(value(a1, a2, a3, b1, 2, b3, c1, c2, c3))
        move_list.append('b2')
    if (b3 == 0):
        pos_list.append(value(a1, a2, a3, b1, b2, 2, c1, c2, c3))
        move_list.append('b3')
    if (c1 == 0):
        pos_list.append(value(a1, a2, a3, b1, b2, b3, 2, c2, c3))
        move_list.append('c1')
    if (c2 == 0):
        pos_list.append(value(a1, a2, a3, b1, b2, b3, c1, 2, c3))
        move_list.append('c2')
    if (c3 == 0):
        pos_list.append(value(a1, a2, a3, b1, b2, b3, c1, c2, 2))
        move_list.append('c3')
    temp = pos_list.index(max(pos_list))
    return move_list[temp]





#function to check if there is a necessary move:
def check(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    if ((a1 == 1) & (a2 == 1) & (a3 == 0)):
        return 'a3'
    elif ((b1 == 1) & (b2 == 1) & (b3 == 0)):
        return 'b3'
    elif ((c1 == 1) & (c2 == 1) & (c3 == 0)):
        return 'c3'
    elif ((a3 == 1) & (a2 == 1) & (a1 == 0)):
        return 'a1'
    elif ((b3 == 1) & (b2 == 1) & (b1 == 0)):
        return 'b1'
    elif ((c3 == 1) & (c2 == 1) & (c1 == 0)):
        return 'c1'
    elif ((a1 == 1) & (b1 == 1) & (c1 == 0)):
        return 'c1'
    elif ((a2 == 1) & (b2 == 1) & (c1 == 0)):
        return 'c1'
    elif ((a3 == 1) & (b3 == 1) & (c3 == 0)):
        return 'c3'
    elif ((b1 == 1) & (c1 == 1) & (a1 == 0)):
        return 'a1'
    elif ((b2 == 1) & (c2 == 1) & (a2 == 0)):
        return 'a2'
    elif ((b3 == 1) & (c3 == 1) & (a3 == 0)):
        return 'a3'
    elif ((a1 == 1) & (b2 == 1) & (c3 == 0)):
        return 'c3'
    elif ((a3 == 1) & (b2 == 1) & (c1 == 0)):
        return 'c1'  
    elif ((a2 == 2) & (a2 == 2) & (a3 == 0)):
        return 'a3'
    elif ((b1 == 2) & (b2 == 2) & (b3 == 0)):
        return 'b3'
    elif ((c1 == 2) & (c2 == 2) & (c3 == 0)):
        return 'c3'
    elif ((a3 == 2) & (a2 == 2) & (a1 == 0)):
        return 'a1'
    elif ((b3 == 2) & (b2 == 2) & (b1 == 0)):
        return 'b1'
    elif ((c3 == 2) & (c2 == 2) & (c1 == 0)):
        return 'c1'
    elif ((a1 == 2) & (b1 == 2) & (c1 == 0)):
        return 'c1'
    elif ((a2 == 2) & (b2 == 2) & (c1 == 0)):
        return 'c1'
    elif ((a3 == 2) & (b3 == 2) & (c3 == 0)):
        return 'c3'
    elif ((b1 == 2) & (c1 == 2) & (a1 == 0)):
        return 'a1'
    elif ((b2 == 2) & (c2 == 2) & (a2 == 0)):
        return 'a2'
    elif ((b3 == 2) & (c3 == 2) & (a3 == 0)):
        return 'a3'
    elif ((a1 == 2) & (b2 == 2) & (c3 == 0)):
        return 'c3'
    elif ((a3 == 2) & (b2 == 2) & (c1 == 0)):
        return 'c1'
    else:
        return '0'





    
#function for checking who wins   if finish is 0 then it hans't finished, if it's 1, player wins, and if it's 2, computer wins
def finishgame(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    finish = 0
    if ((a1 == 1) & (a2 == 1) & (a3 == 1)) or ((b1 == 1) & (b2 == 1) & (b3 == 1)) or ((c1 == 1) & (c2 == 1) & (c3 == 1)) or ((a3 == 1) & (b3 == 1) & (c3 == 1)) or ((a2 == 1) & (b2 == 1) & (c2 == 1)) or ((a1 == 1) & (b1 == 1) & (c1 == 1)) or ((a3 == 1) & (b2 == 1) & (c1 == 1)) or ((a1 == 1) & (b2 == 1) & (c3 == 1)):
        finish = finish + 1
    if ((a1 == 2) & (a2 == 2) & (a3 == 2)) or ((b1 == 2) & (b2 == 2) & (b3 == 2)) or ((c1 == 2) & (c2 == 2) & (c3 == 2)) or ((a3 == 2) & (b3 == 2) & (c3 == 2)) or ((a2 == 2) & (b2 == 2) & (c2 == 2)) or ((a1 == 2) & (b1 == 2) & (c1 == 2)) or ((a3 == 2) & (b2 == 2) & (c1 == 2)) or ((a1 == 2) & (b2 == 2) & (c3 == 2)):
        finish = finish + 2
    return finish








#gameplay:
turn = input("Do you want to go first?(Y,N)")
if (turn == 'Y'):
    #player's first move
    move_1 = input("Where do you want to put your first piece?")
    if (move_1 == 'a1'):
        a1 = 1
    if (move_1 == 'a2'):
        a2 = 1
    if (move_1 == 'a3'):
        a3 = 1
    if (move_1 == 'b1'):
        b1 = 1
    if (move_1 == 'b2'):
        b2 = 1
    if (move_1 == 'b3'):
        b3 = 1
    if (move_1 == 'c1'):
        c1 = 1
    if (move_1 == 'c2'):
        c2 = 1
    if (move_1 == 'c3'):
        c3 = 1
    if (move_1 != 'a1'):
        a1 = 0
    if (move_1 != 'a2'):
        a2 = 0
    if (move_1 != 'a3'):
        a3 = 0
    if (move_1 != 'b1'):
        b1 = 0
    if (move_1 != 'b2'):
        b2 = 0
    if (move_1 != 'b3'):
        b3 = 0
    if (move_1 != 'c1'):
        c1 = 0
    if (move_1 != 'c2'):
        c2 = 0
    if (move_1 != 'c3'):
        c3 = 0




    #computer's first move:
    if (move_1 != 'b2'):
        b2 = 2
        print ("My turn! Thinking...")
        print ("b2")
    else:
        temp_1 = bestposition(a1, a2, a3, b1, b2, b3, c1, c2, c3)
        if (temp_1 == 'a1'):
            a1 = 2
        if (temp_1 == 'a2'):
            a2 = 2
        if (temp_1 == 'a3'):
            a3 = 2
        if (temp_1 == 'b1'):
            b1 = 2
        if (temp_1 == 'b2'):
            b2 = 2
        if (temp_1 == 'b3'):
            b3 = 2
        if (temp_1 == 'c1'):
            c1 = 2
        if (temp_1 == 'c2'):
            c2 = 2
        if (temp_1 == 'c3'):
            c3 = 2
        print ("My turn! Thinking..")
        print (temp_1)





    #player's second move:
    move_2 = input("Where do you want to put your second piece?")
    if (move_2 == 'a1'):
        a1 = 1
    if (move_2 == 'a2'):
        a2 = 1
    if (move_2 == 'a3'):
        a3 = 1
    if (move_2 == 'b1'):
        b1 = 1
    if (move_2 == 'b2'):
        b2 = 1
    if (move_2 == 'b3'):
        b3 = 1
    if (move_2 == 'c1'):
        c1 = 1
    if (move_2 == 'c2'):
        c2 = 1
    if (move_2 == 'c3'):
        c3 = 1








    #computer's second move:
    temp_2 = check(a1, a2, a3, b1, b2, b3, c1, c2, c3)
    temp_3 = bestposition(a1, a2, a3, b1, b2, b3, c1, c2, c3)
    if (temp_2 == 0):
        print ("My turn! Thinking...")
        print (temp_3)
        if (temp_3 == 'a1'):
            a1 = 2
        if (temp_3 == 'a2'):
            a2 = 2
        if (temp_3 == 'a2'):
            a3 = 2
        if (temp_3 == 'b1'):
            b1 = 2
        if (temp_3 == 'b2'):
            b2 = 2
        if (temp_3 == 'b3'):
            b3 = 2
        if (temp_3 == 'c1'):
            c1 = 2
        if (temp_3 == 'c2'):
            c2 = 2
        if (temp_3 == 'c3'):
            c3 = 2
    else:
        print ("My turn! Thinking...")
        print (temp_2)
        if (temp_2 == 'a1'):
            a1 = 2
        if (temp_2 == 'a2'):
            a2 = 2
        if (temp_2 == 'a3'):
            a3 = 2
        if (temp_2 == 'b1'):
            b1 = 2
        if (temp_2 == 'b2'):
            b2 = 2
        if (temp_2 == 'b3'):
            b3 = 2
        if (temp_2 == 'c1'):
            c1 = 2
        if (temp_2 == 'c2'):
            c2 = 2
        if (temp_2 == 'c3'):
            c3 = 2





    #player's third move: 
    move_3 = input("Where do you want to put your third piece?")
    if (move_3 == 'a1'):
        a1 = 1
    if (move_3 == 'a2'):
        a2 = 1
    if (move_3 == 'a3'):
        a3 = 1
    if (move_3 == 'b1'):
        b1 = 1
    if (move_3 == 'b2'):
        b2 = 1
    if (move_3 == 'b3'):
        b3 = 1
    if (move_3 == 'c1'):
        c1 = 1
    if (move_3 == 'c2'):
        c2 = 1
    if (move_3 == 'c3'):
        c3 = 1








    #computer's third move:
    temp_4 = finishgame(a1, a2, a3, b1, b2, b3, c1, c2, c3)
    temp_5 = check(a1, a2, a3, b1, b2, b3, c1, c2, c3)
    temp_6 = bestposition(a1, a2, a3, b1, b2, b3, c1, c2, c3)
    if (temp_4 == 1):
        print ("Game over! You won")
    elif (temp_4 == 2):
        print ("Game over! I won")
    else:
        if (temp_5 == 0):
            print("My turn! Thinking...")
            print (temp_6)
            if (temp_6 == 'a1'):
                a1 = 2
            if (temp_6 == 'a2'):
                a2 = 2
            if (temp_6 == 'a2'):
                a3 = 2
            if (temp_6 == 'b1'):
                b1 = 2
            if (temp_6 == 'b2'):
                b2 = 2
            if (temp_6 == 'b3'):
                b3 = 2
            if (temp_6 == 'c1'):
                c1 = 2
            if (temp_6 == 'c2'):
                c2 = 2
            if (temp_6 == 'c3'):
                c3 = 2
        else:
            print ("My turn! Thinking...")
            print (temp_5)
            if (temp_5 == 'a1'):
                a1 = 2
            if (temp_5 == 'a2'):
                a2 = 2
            if (temp_5 == 'a3'):
                a3 = 2
            if (temp_5 == 'b1'):
                b1 = 2
            if (temp_5 == 'b2'):
                b2 = 2
            if (temp_5 == 'b3'):
                b3 = 2
            if (temp_5 == 'c1'):
                c1 = 2
            if (temp_5 == 'c2'):
                c2 = 2
            if (temp_5 == 'c3'):
                c3 = 2








    #player's fourth move:
    move_4 = input("Where do you want to put your fourth piece?")
    if (move_4 == 'a1'):
        a1 = 1
    if (move_4 == 'a2'):
        a2 = 1
    if (move_4 == 'a3'):
        a3 = 1
    if (move_4 == 'b1'):
        b1 = 1
    if (move_4 == 'b2'):
        b2 = 1
    if (move_4 == 'b3'):
        b3 = 1
    if (move_4 == 'c1'):
        c1 = 1
    if (move_4 == 'c2'):
        c2 = 1
    if (move_4 == 'c3'):
        c3 = 1







    #computer's fourth move:
    temp_7 = finishgame(a1, a2, a3, b1, b2, b3, c1, c2, c3)
    temp_8 = check(a1, a2, a3, b1, b2, b3, c1, c2, c3)
    temp_9 = bestposition(a1, a2, a3, b1, b2, b3, c1, c2, c3)
    if (temp_7 == 1):
        print ("Game over! You won")
    elif (temp_7 == 2):
        print ("Game over! I won")
    else:
        if (temp_8 == 0):
            print ("My turn! Thinking...")
            print (temp_9)
            if (temp_9 == 'a1'):
                a1 = 2
            if (temp_9 == 'a2'):
                a2 = 2
            if (temp_9 == 'a3'):
                a3 = 2
            if (temp_9 == 'b1'):
                b1 = 2
            if (temp_9 == 'b2'):
                b2 = 2
            if (temp_9 == 'b3'):
                b3 = 2
            if (temp_9 == 'c1'):
                c1 = 2
            if (temp_9 == 'c2'):
                c2 = 2
            if (temp_9 == 'c3'):
                c3 = 2
        else:
            print ("My turn! Thinking...")
            print (temp_8)
            if (temp_8 == 'a1'):
                a1 = 2
            if (temp_8 == 'a2'):
                a2 = 2
            if (temp_8 == 'a3'):
                a3 = 2
            if (temp_8 == 'b1'):
                b1 = 2
            if (temp_8 == 'b2'):
                b2 = 2
            if (temp_8 == 'b3'):
                b3 = 2
            if (temp_8 == 'c1'):
                c1 = 2
            if (temp_8 == 'c2'):
                c2 = 2
            if (temp_8 == 'c3'):
                c3 = 2







    #player's fifth move:
    move_5 = input("Where do you want to put your fifth piece?")
    if (move_5 == 'a1'):
        a1 = 1
    if (move_5 == 'a2'):
        a2 = 1
    if (move_5 == 'a3'):
        a3 = 1
    if (move_5 == 'b1'):
        b1 = 1
    if (move_5 == 'b2'):
        b2 = 1
    if (move_5 == 'b3'):
        b3 = 1
    if (move_5 == 'c1'):
        c1 = 1
    if (move_5 == 'c2'):
        c2 = 1
    if (move_5 == 'c3'):
        c3 = 1







    #computer's fifth move:
    temp_10 = finishgame(a1, a2, a3, b1, b2, b3, c1, c2, c3)
    temp_11 = check(a1, a2, a3, b1, b2, b3, c1, c2, c3)
    temp_12 = bestposition(a1, a2, a3, b1, b2, b3, c1, c2, c3)
    if (temp_10 == 1):
        print ("Game over! You won")
    elif (temp_10 == 2):
        print ("Game over! I won")
    else:
        if (temp_11 == 0):
            print ("My turn! Thinking...")
            print (temp_12)
            if (temp_12 == 'a1'):
                a1 = 2
            if (temp_12 == 'a2'):
                a2 = 2
            if (temp_12 == 'a3'):
                a3 = 2
            if (temp_12 == 'b1'):
                b1 = 2
            if (temp_12 == 'b2'):
                b2 = 2
            if (temp_12 == 'b3'):
                b3 = 2
            if (temp_12 == 'c1'):
                c1 = 2
            if (temp_12 == 'c2'):
                c2 = 2
            if (temp_12 == 'c3'):
                c3 = 2
        else:
            print ("My turn! Thinking...")
            print (temp_11)
            if (temp_11 == 'a1'):
                a1 = 2
            if (temp_11 == 'a2'):
                a2 = 2
            if (temp_11 == 'a3'):
                a3 = 2
            if (temp_11 == 'b1'):
                b1 = 2
            if (temp_11 == 'b2'):
                b2 = 2
            if (temp_11 == 'b3'):
                b3 = 2
            if (temp_11 == 'c1'):
                c1 = 2
            if (temp_11 == 'c2'):
                c2 = 2
            if (temp_11 == 'c3'):
                c3 = 2







    


















            
    
