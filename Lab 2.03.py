'''
##########################################
Lab 2.03 - Game Show
##########################################
In your Notebook
Follow the flow of execution in the following programs and predict what will happen for each
one
---------------------------------------
Example 1
---------------------------------------
a = input("What... is your quest")
b = "to seek the holy grail"
if a != b:
    print("Go On. Off you go")
else:
    b = input("What...is the air-speed velocity of an unladen swallow?")
    if b == "What do you mean? An African or European swallow?":
        print("I don't know that...AHHH [Bridgekeeper was thrown over bridge]")
    else:
        print("[you were thrown over bridge]")

Prediction:it will work
Actual: it worked

---------------------------------------
Example 2
---------------------------------------
user_input = input("What is your favorite color")
if user_input == 'blue':
    print("Blueskadoo")
elif user_input == "red":
    print("Roses are red!")
elif user_input == "yellow":
    print("Mellow Yellow")
elif user_input == "green":
    print("Green Machine")
elif user_input == "orange":
    print("Orange you glad I didn't say banana.")
elif user_input == "black":
    print("I see a red door and I want it painted black")
elif user_input == "purple":
    print("And we'll never be royalllssss")
elif user_input == "pink":
    print("Pinky- and the Brain")
else:
    print("I don't recognize that color. Is it even...??")

Prediction: it wont work
Actual: it worked

---------------------------------------
In your Notebook
---------------------------------------
Translate this Snap! program into a Python program
***Refer to the image provided on Moodle located below the Lab 2.03 link***
Write program below:

x = int(input("What is the length of first side? "))
y = int(input("What is the length of second side? "))
z = int(input("What is the length of third side? "))

# check to see if it can be a triangle
if x + y > z and x + z > y and y + z > x:
    print("This is a triangle.")

    # is a right triangle?
    if x **2 + y**2 == z**2 or x**2 + z**2 == y**2 or y **2 + z**2 == x**2: 
        print("This is a right triangle!")

    # is it equilateral?
    if x == y and y == z:
        print("This is an equilateral triangle!")
    # is it isosceles?
    elif (x == y and x != z) or (x == z and x != y) or (y == z and x != z):
        print("This is an isosceles triangle")
    # must be scalene
    else:
        print("This is a scalene trangle")
    
else:
    print("This isnt a triangle")

---------------------------------------
Create a game show program
---------------------------------------
Declare 10 prizes (prize1, prize2, prize 3 at the top of your file)
User picks a number
The prize corresponding with that door is printed for the user.
Write code below the multiline comment
'''
# setting the prizes to something
prize_1 = "dog"
prize_2 = "cat"
prize_3 = "balloons"
prize_4 = "new car"
prize_5 = "new job"
prize_5 = "new girlfriend"
prize_6 = "new computer"
prize_7 = "new house"
prize_8 = "new xbox"
prize_9 = "dinner"
prize_10 = "money"


#user picks a number
user_number = int(input("Pick a random door number:"))
if user_number == 1:
    print("You won a dog!")
elif user_number == 2:
    print("You won a cat!")
elif user_number == 3:
    print("You won balloons!")
elif user_number == 4:
    print("You won a new car!")
elif user_number == 5:
    print("You won a new job!")
elif user_number == 6:
    print("You won a new girlfriend!")
elif user_number == 7:
    print("You won a new house")
elif user_number == 8:
    print("You won a new xbox!")
elif user_number == 9:
    print("You won dinner!")
elif user_number == 10:
    print("You won money!")
    

