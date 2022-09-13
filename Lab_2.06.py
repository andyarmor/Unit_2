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
# P1 first turn 
#making board
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print 1st row of board
print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
print('----------')

#second row
print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
print('----------')

#third row
print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
print('----------')

#f allows you to add strings and values

#player chooses a location
cell_selected = int(input("User 1: Choose a location on the board: "))

#replace number in the board with an X
if cell_selected ==1:
    board[0][0] ='X'
elif cell_selected ==2:
    board[0][1] = 'X'
elif cell_selected ==3:
    board[0][2] = 'X'
elif cell_selected ==4:
    board[1][0] = 'X'
elif cell_selected ==5:
    board[1][1] = 'X'
elif cell_selected ==6:
    board[1][2] = 'X'
elif cell_selected ==7:
    board[2][0] = 'X'
elif cell_selected ==8:
    board[2][1] = 'X'
elif cell_selected ==9:
    board[2][2] = 'X'



#print 1st row of board
print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
print('----------')

#second row
print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
print('----------')

#third row
print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
print('----------')

#P2 First Turn

cell_selected = int(input("User 2: Choose a location on the board: "))

#replace number in the board with an X
if cell_selected ==1:
    board[0][0] ='O'
elif cell_selected ==2:
    board[0][1] = 'O'
elif cell_selected ==3:
    board[0][2] = 'O'
elif cell_selected ==4:
    board[1][0] = 'O'
elif cell_selected ==5:
    board[1][1] = 'O'
elif cell_selected ==6:
    board[1][2] = 'O'
elif cell_selected ==7:
    board[2][0] = 'O'
elif cell_selected ==8:
    board[2][1] = 'O'
elif cell_selected ==9:
    board[2][2] = 'O'


#print 1st row of board
print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
print('----------')

#second row
print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
print('----------')

#third row
print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
print('----------')


