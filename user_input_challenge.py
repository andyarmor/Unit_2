'''
##############################
User Input Challenge
##############################

Create a program that asks the user to enter their name and their age. Print out a message 
addressed to them that tells them the year that they will turn 100 years old.

Add on to the previous program by asking the user for another number and printing out that 
many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n" is the same as pressing the ENTER button)
'''
# year you are 100 
print("We are going to see what year you will turn 100 years old!")
name = input("What is your name? ")
age = int(input("How old are you? "))
print("Year when you will turn 100 is:", 100 - age + 2022)