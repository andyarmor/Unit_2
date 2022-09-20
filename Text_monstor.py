#Text monstor 
#Andy 

#make dungeon
floor_1 = ['empty', 'sword', 'stairs up', 'monster', 'empty' ]
floor_2 = ['stairs up', 'sword', 'stairs down', 'monster', 'magic stones'], 
floor_3 = ['stairs down', 'empty', 'empty', 'boss monster', 'prize']

#variables
current_floor = floor_1
current_room = 0
inventory = []

#describe current location
#update current location
print(f"The current room has {current_floor[current_room]}")
playing =True
while playing: 
    current_location = current_floor[current_room]

    if current_location == 'empty':
        print("You are standing in an empty room!")
    elif current_location == 'sword':
        print("You are standing in a room with a sward")
    elif current_location == 'stairs up':
        print("You see some staris leading up!")
    elif current_location == 'monster':
        print("You see a big scary monster in the corner!")
    elif current_location == 'stairs down':
        print("You see some stairs leading down!")
    elif current_location == 'magic stones':
        print("You see the great magic stones!")
    else:
        print("You won and see the shiny prize!!")

    print(f"current location: {current_location}")

#player choice
    input()
    player_choice = input("What would you like to do? (left, right, up, down, grab, fight, inventory)")

    if player_choice == 'right':
        if  current_room < 4:
            current_room +=1
        else: 
            print("You can't go any further that direction!")

    elif player_choice == 'left': 
        if  current_room > -0:
            current_room -=1
        else: 
            print("You can't go any further that direction!")
    elif player_choice == 'up':
        if current_floor < 3: 
            current_floor +=1

    

    print()    




