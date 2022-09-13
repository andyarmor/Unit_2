great_pets = ['cat', 'dog']
while True: 
    animal = input("What is your favorite pet?")
    if animal =='quit':
        print("Bye!")
        break
    else:
        if animal in great_pets:
            print("A great pet!")
        else: 
            print(f"{animal}, a fine pet!")

