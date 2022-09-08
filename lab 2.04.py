'''
###########################
Lab 2.04
###########################
1. In your notebook
For each example below, predict what will be printed. Run the program and write down the output in your notebook.

Example 1
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[0])
    print(a[3])

    prediction:  a d                                          
    actual: a d

Example 2
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 3])

    prediction: idk
    actual: c

Example 3
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 6])

    prediction: idk
    actual: e

Example 4
    a = ['a', 'b', 'c', 'd', 'e']
    a[3] = 'haha'
    print(a)

    prediction: haha
    actual: ['a' , 'b' , 'c' , 'haha' , 'e']

2. Create this game again using lists and indexes
--------------------------------------------------
Declare 10 prizes (prize0, prize1, prize2 at the top of your file), but store them all in a list.

User picks a number.

Print prize associated with the door user picked.

prize0 = "dog"
prize1 = "cat"
prize2 = "balloon"
prize3 = "house"
prize4 = "toy"
prize5 = "car"
prize6 = "horse"
prize7 = "desk"
prize8 = "friend"
prize9 = "shirt"
prize10 = "pants"

prizes = [prize0 , prize1, prize2, prize3, prize4, prize5, prize6, prize7, prize8, prize9, prize10]
user_number = int(input("give me a random number from 0-10: "))
if user_number == 0:
    print(prize0)
elif user_number == 1:
    print(prize1)
elif user_number == 2:
    print(prize2)
elif user_number == 3:
    print(prize3)
elif user_number == 4:
    print(prize4)
elif user_number == 5:
    print(prize5)
elif user_number == 6:
    print(prize6)
elif user_number == 7:
    print(prize7)
elif user_number == 8:
    print(prize8)
elif user_number == 9:
    print(prize9)
elif user_number == 10:
    print(prize10)

3. Create a quiz
--------------------------------------------------
Create a food quiz using lists and indexes.

List of 6 different foods.

Ask the user 8 vague questions to find out what their favorite food is using the list.

Update the score and print their top 2 favorite foods.

Hint: Use a search engine to find the largest number in a python list.

----------------------
​Starter code here​:
----------------------
food = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','baggles']
score = [0,0,0,0,0,0]

print('Please answer each questions with "y" for "yes" and "n" for "no."')
user_input = input('Do you like food with holes? ')
if user_input == 'y':
  score[0] = score[0] + 1
  score[5] = score[5] + 1

##############################
Together in class:
##############################
Research nested lists and work through the following Examples:

Bonus Example 1
a = ['a', 'b', 'c', ['d', 'e']]
print(len(a))
Bonus Example 2
a = ['a', 'b', 'c', ['d', 'e']]
b = a[3]
print(b)
Bonus - In your Notebook
How would you access d from the list a?
print([3][0])
'''
print("We are going to take a food quiz to see if I can guess what food you like!")
food = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','baggles']
score = [0,0,0,0,0,0]

print('Please answer each questions with "y" for "yes" and "n" for "no."')
user_input = input("Do you like food with holes? ")


if user_input == 'y':
  score[0] = score[0] + 1 #add 1 to donut
  score[5] = score[5] + 1 #add 1 to baggles

user_input = input("Do you like fried foods? ")
if user_input == 'y':
    score[0] +=1 #add 1 to donuts
    score[1] +=1  #add 1 to pancakes
    score[2] +=1 # add 1 to bacon
    score[3]#add 1 to waffles 
    score[4] +=1 #add 1 to eggs

user_input = input("Do you like yellow foods? ")
if user_input == 'y': 
    score[4] +=1


user_input = input("Do you like boiled foods? ")
if user_input == 'y':
    score[4] +=1
    score[5] +=1

user_input = input("Do you like foods with squares in them? ")
if user_input == 'y':
    score[3] +=1

user_input = input("Do you like circle shaped foods? ")
if user_input == 'y':
    score[0] +=1
    score[1] +=1
    score[5] +=1

user_input = input("Do you like food made from pigs? ")
if user_input == 'y':
    score[2] +=1

user_input = input("Do you like hot foods? ")
if user_input == 'y':
    score[0] +=1
    score[1] +=1
    score[2] +=1
    score[3] +=1
    score[4] +=1





#find fav food

max_score = max(score) #find highest score in list
index_of_max_score = score.index(max_score) #return index number of highest score
fav_food = food[index_of_max_score] #find food item with the same index as max score
print(f"Your favorite food is {fav_food}")

#remove the first fav from food list and corresponding score list
score.remove(score[index_of_max_score])
food.remove(food[index_of_max_score])

# find new fav food
max_score = max(score) #find highest score in list
index_of_max_score = score.index(max_score) #return index number of highest score
fav_food = food[index_of_max_score] #find food item with the same index as max score
print(f"Your second favorite food is {fav_food}")
