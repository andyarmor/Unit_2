#Text monstor 
#Andy 

#make dungeon
floor_1 = ['empty', 'sword', 'stairs up', 'monster', 'empty' ]
floor_2 = ['stairs up', 'sword', 'stairs down', 'monster', 'magic stones'], 
floor_3 = ['stairs down', 'empty', 'empty', 'boss monster', 'prize']
floor_list = [floor_1, floor_2, floor_3]

#variables
current_floor = floor_1
current_room = 0
inventory = []

#describe current location
#update current location
playing =True
while playing: 
    #print(f"The current room has {current_floor[current_room]}")
    print(f"Your current floor is {current_floor}")
    current_location = current_floor[current_room]
    
    if current_location == 'empty':
        print("You are standing in an empty room!")
    elif current_location == 'sword':
        print("You are standing in a room with a sword")
    elif current_location == 'stairs up':
        print("You see some stairs leading up!")
    elif current_location == 'monster':
        print("You see a big scary monster in the corner!")
    elif current_location == 'stairs down':
        print("You see some stairs leading down!")
    elif current_location == 'magic stones':
        print("You see the great magic stones!")
    
        print("You won and see the shiny prize!!")

    

#player choice
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
    elif player_choice == 'up' and current_location == 'stairs up':
        if current_floor == floor_1:
            current_floor = floor_2
            current_room = 0
        elif current_floor == floor_2:
            current_floor = floor_3
    elif player_choice == 'down' and current_location == 'stairs down':
        if current_floor == floor_3:
            current_floor = floor_2
        elif current_floor == floor_2:
            current_floor = floor_1
    #elif player_choice == 'fight':
        #if inventory == 'sword' and 'magic stones':
            #print("You won! Go right to claim your prize, Congratulations!")
        #else:
            #print("You are either not in the right spot or don't have your required materials to fight. Sorry!")
    elif player_choice == 'grab':
        if current_location == 'sword': 
            current_floor.remove('sword')
            inventory = ['sword']
            print(f"Your inventory now includes a {inventory[0]} and you are now in the next room!")
        elif current_location == 'magic stones':
            current_floor.remove('magic stones') 
            inventory = ['sword', 'magic stones']
            print(f"You now have a {inventory[0]} and {inventory[1]}")
        else:
            print("There is nothing to grab here!")
    elif player_choice == 'fight':
        if current_location == 'monster':
            if 'sword' in inventory:
                print("You have defeated the monster!")
                current_floor.remove('monster')
            else:
                print("You lost to the monster!")
    elif player_choice == 'inventory':
            if 'sword' and 'magic stones' in inventory:
                print(f"In your inventory you have a {inventory[0]} and {inventory[1]}")    
            elif 'sword' in inventory:
                print("Your inventory has a sword right now!")
            elif 'magic stones' in inventory:
                print("Your inventory has magic stones!")

    
    print()    


