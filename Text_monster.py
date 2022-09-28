#Text monstor 
#Andy 

#make dungeon
floor_1 = ['empty', 'sword', 'stairs up', 'monster', 'empty' ]
floor_2 = ['stairs up', 'sword', 'stairs down', 'monster', 'magic stones']
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
    #print(f"Your current floor is {current_floor}")
    #print(f"{current_room} is the room index")
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
    elif current_location == 'boss monster':
        print("The biggest monster you have ever seen is here!")
    

#player choice
    player_choice = input("What would you like to do? (left, right, up, down, grab, fight, inventory, quit, drop)")

    if player_choice == 'right' and current_location != 'monster'and 'boss monster':
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
        elif current_floor == floor_2:
            current_floor = floor_3
    elif player_choice == 'down' and current_location == 'stairs down':
        if current_floor == floor_3:
            current_floor = floor_2
        elif current_floor == floor_2:
            current_floor = floor_1
    elif player_choice == 'grab':
        if current_location == 'sword': 
            current_floor[current_room] = 'empty'
            inventory.append('sword')
            print("Your inventory now includes a sword!")
            current_floor[current_room] = 'empty'
        elif current_location == 'magic stones':
            current_floor[current_room] = 'empty'
            inventory.append('magic stones')
            print(f"Your inventory now includes magic stones!")
        elif current_location == 'prize':
            inventory.append('prize')
            
        else:
            print("There is nothing to grab here!")
        
    elif player_choice == 'fight':
        if current_location == 'monster':
            if 'sword' in inventory:
                print("You have defeated the monster! You can continue")
                current_floor[current_room] = 'empty'
            else:
                print("You have lost to the monster and can not continue without having a sword!")
        elif current_location == 'boss monster':
            if 'sword' and 'magic stones' in inventory:
                user_answer = input("You have defeated the boss monster! Solve this riddle to continue to your prize: What has to be broken before you can eat it?")
                answer = 'egg'
                if user_answer == 'egg':
                    print("You can continue to your prize!")
                else:
                    print("Wrong answer")


    elif player_choice == 'inventory':
            if 'sword' and 'magic stones' in inventory:
                print(f"In your inventory you have a {inventory[0]} and {inventory[1]}")    
            elif 'sword' in inventory:
                print("Your inventory has a sword right now!")
            elif 'magic stones' in inventory:
                print("Your inventory has magic stones!")
            elif 'prize' in inventory:
                print("You have the prize!")
            elif '' in inventory:
                print("You have nothing in your inventory!")
    elif player_choice == 'drop':
        dropped_item = input("What would you like to drop?")
        if dropped_item == 'sword':
            inventory.remove('sword')
        elif dropped_item == 'magic stones':
            inventory.remove('magic stones')
        elif dropped_item == '':
            print("You don't have this item, so you can't drop it!")
        

    elif player_choice == 'quit':
        break


    
    print()    


