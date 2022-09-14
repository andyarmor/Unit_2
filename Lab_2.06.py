'''
#################
Lab 2.06
#################
1. In your Notebook
-------------------
Predict what will be printed then type the program in your console to confirm
Example 1
    a = 0
    while a < 10:
        print(a)

prediction:
actual:

Example 2
    a = 0
    while a < 10:
        a = a + 1
        print(a)

prediction:
actual:

2. In your Notebook
-------------------
Create a set of test cases for the following sample code and predict the behavior
    a = input("Would you like to quit: ")
    while a != "y" and a != "n" :
        a = input("Would you like to quit: ")

test cases: 'y', 'n', 'q', 'cat'

3. Implement the Tic Tac Toe game using a while loop
----------------------------------------------------
Allow users to keep playing (max 9 times).

Use variables to decide whose turn it is, and greet them as Xs or Os.

User picks a location on the board according to the number:
        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9


Depending on the position user gave, update the corresponding position of the board to reflect that.

Print the updated board out.

You will not need to determine the winner at this point.
(Copy and paste your previous tic-tac-toe version and modify the code to implement the above)
'''




board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
turns = 0 
player = 1
player_symbol = ""
valid_choice = False

#print first row
print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
print('----------')

#second row
print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
print('----------')

#third row
print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
print('----------')

#f allows you to add strings and values

while turns < 9:
    player_choice = int(input(f"Choose a number to place your {player_symbol}"))

    #move conditional 
    if player_choice ==1 and board [0][0] ==1:
        board[0][0] = player_symbol
        valid_choice =True
    elif player_choice == 2 and board [0][1] ==2:
        board[0][1] = player_symbol
        valid_choice =True
    elif player_choice == 3 and board [0][2] ==3:
        board[0][2] = player_symbol
        valid_choice =True
    elif player_choice == 4 and board [1][0] ==4:
        board[1][0] = player_symbol
        valid_choice =True
    elif player_choice == 5 and board [1][1] ==5:
        board[1][1] = player_symbol
        valid_choice =True
    elif player_choice == 6 and board [1][2] ==6:
        board[1][2] = player_symbol
        valid_choice =True
    elif player_choice == 7 and board [2][0] ==7:
        board[2][0] = player_symbol
        valid_choice =True
    elif player_choice == 8 and board [2][1] ==8:
        board[2][1] = player_symbol
        valid_choice =True
    elif player_choice == 9 and board [2][2] ==9:
        board[2][2] = player_symbol
        valid_choice =True
    else:
        print("invalid")
        
#print first row of board
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print('----------')

#second row
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print('----------')

#third row
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
    print('----------')

    #Switch players
    if valid_choice == True:
        turns +=1
        if player ==1:
            player =2
            player_symbol = 'O'
        else:
            player =1
            player_symbol = 'X'
    valid_choice = False

print("No more turns, GAME OVER!")
    










