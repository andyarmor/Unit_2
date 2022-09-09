'''
############################
Lab 2.05 - Tic-Tac-Toe
############################
In your Notebook
1. Predict what will be printed. Then run the program and confirm
Example 1
---------
a = ['a', 'b', 'c', 'd', 'e']
print(a[0:3])
print(a[1:4])

Prediction: a b c     bcd
Actual: abc    bcd 

Example 2
---------
a = ['a', 'b', 'c', 'd', 'e']
print(a[1:len(a) - 3])

Prediction: idk
Actual: b

Example 3
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a.remove('b')
print(a)
print(b)

Prediction: acde then idk
Actual:acde then none

Example 4
---------
a = ['a', 'b', 'c', 'd', 'e']
a[0] = 'haha'
b = a.pop()
print(a)
print(b)

Prediction: haha b c d then just e
Actual: haha b c d then just e

Example 5
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a + ['abc']
print(a)
print(b)

Prediction: abcde then abcde abc
Actual: abcde then abcde abc

Example 6
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a.append('f')
print(a)
print(b)

Prediction: abcdef then idk
Actual: abcdef then none
2. In script mode (Type your program below the multi-line comment)
We are going to start implementing Tic-Tac-Toe using a single list.
1. The user picks a location on the board according to the number:
    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9
2. Depending on the position that the user inputs, update the position of the board to an "X" to reflect
that.
    Example:
        1 | 2 | 3
        ---------
        4 | 5 | X
        ---------
        7 | 8 | 9
3. Print the updated board out, but don't worry about making it look pretty.
4. Only need to implement one turn of the game
'''
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
cell_selected = int(input("Choose a location on the board: "))

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








