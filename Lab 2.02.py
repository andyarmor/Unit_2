'''
##################################
Lab 2.02 Booleans & Expressions
##################################
In your Notebook
Predict if each of the following examples will produce a True or False output. Check your answers in interactive mode.
                 
Example 1
    >>> a = 100
    >>> b = "science"
    >>> a > 75 and b == "science"       Prediction:    True                 Actual: True
Example 2
    >>> a = 100
    >>> b = "science"
    >>> a > 75 and b != "science"       Prediction:    false                  Actual: false
Example 3
    >>> a = 100
    >>> b = "science"
    >>> a > 75 or b != "science"        Prediction: True                         Actual: True
Example 4
    >>> a = 100
    >>> b = "science"
    >>> c = True
    >>> not c and a > 75 and b == "science"     Prediction:  Idk                   Actual:  False

In your Console

Complete the following coding challenge
Create a "Can I be President?" program, which determines if the user meets the minimum requirements for becoming the President of the United States. 
Have the user input the information needed.

The minimum requirements to be president of the United States are:

1. Older than 35

2. Resident of US for 14 Years

3. Natural born citizen

Print True if the person could be president and False if they can't be president.

Create a "I can't be President?" program. Print True if the user cannot be President and False if they can be President.

Create a "Can I ride the roller coaster?" program. A roller coaster has the rule that a rider has to be over the height of 50 inches. Because of a legal loophole, if you are over the age of 18 you can ride regardless of your height. If you are allowed to ride, the coaster costs 4 quarters (although the operator accepts tips so more money is appreciated).

Also, the theme park sells frequent rider passes: with a frequent rider pass the roller coaster costs only 2 quarters. Ask the user how tall they are in inches, their age, how many quarters they have, and if they have a frequent rider pass. Print True if the person can ride and False if they can't.


Are the following expressions equivalent? Research DeMorgan's Laws and write why you think they are the same or why they are not the same
not(x or y) == not x and not y

not(x and y) == not x or not y
'''
#can be president (returns true if can be presdident)
print("we are going to see if you can become president!")
age = int(input("How old are you? "))
Residentcy = input("How long have you been a resident of the US? ")
citizen = input("Are you a natural born citizen? ")
print(age > 35 and Residentcy >= '14' and citizen == 'yes')

# can't be president (returns true if can't be president)
print("We are going to see if you can't be a president!")
age = int(input("How old are you? "))
Residentcy = input("How long have you been a resident of the US? ")
citizen = input("Are you a natural born citizen? ")
print(age < 35 or Residentcy <= '14' or citizen != 'yes')

# can I ride rollercoaster (true if can ride)
print("Can you ride a rollercoaster?")
height = int(input("How tall are you? "))
over_18 = int(input("How old are you? "))
quarters = int(input("how many quarters do you have? "))
frequent = ("(yes/no) Do you have a frequent rider pass? ")
#logic variables
can_pay = quarters >= 4 or frequent == 'yes'
old_enough = over_18 >= 18
tall_enough = height >= 50

# (if 18 and (money or pass)) OR are tall enough and money or pass
print((can_pay and tall_enough) or (can_pay and old_enough))