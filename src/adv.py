from room import Room
from player import Player

# Declare all the rooms
room = {
    'outside':  Room("outside", "Outside Cave Entrance",
                     "North of you, the cave mount beckons \n", {'a hook': "A dusty grappling hook lays in some grass, dustied and unused", 'a coin': 'A gold coin'}),

    'foyer':    Room("foyer", "Foyer", """Dim light filters in from the south. Dusty
passages run north and east. \n""", {}),

    'overlook': Room("overlook", "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. \n""", {}),

    'narrow':   Room("narrow", "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air. \n""", {}),

    'treasure': Room("treasure", "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south. \n""", {'shovel' : 'A moldy and rusted shovel is shoved into the dirt nearby'}),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Main
name = input("\n Enter a name, adventurer: ")

playerStart = Player(name, room['outside'], [])
print(playerStart)
# Make a new player object that is currently in the 'outside' room.
directionInput = input("Choose a direction (n,e,s,w), type help for more commands [q to quit]: ")
DI = directionInput.lower().strip()

currentRoom = 'outside'
while not DI == "q":
    ##User chose a direction
    if DI == "n" or DI == "e" or DI == "s" or DI == "w":
        try:
            dirCall = (f"{DI}_to")
            print(getattr(room[currentRoom], dirCall))

            currentRoom = getattr(room[currentRoom], dirCall, None).refID
            
        except AttributeError:
            print("That direction isn't available")

    ##User chooses to look in the room            
    elif DI == "look":
        chosenItems = room[currentRoom].look()
        ##Put items in player inventory
        for playerItem in chosenItems.items():
            playerStart.inventory[playerItem[0]] = playerItem[1]

        print(room[currentRoom].description)
    
    elif DI == "inventory": 
        print(f"This is your inventory: ")
        for idx, itemsInInventory in enumerate(playerStart.inventory.items()):
            print(idx + 1, itemsInInventory[0])

        ##Have user select item they wish to interact with
        itemSelect = input("Select an item by number! [Type 0 to exit]: ")
        if(itemSelect == "0"):
            print("You leave your inventory")
            print(room[currentRoom].description)
        else:
            selected = list(playerStart.inventory)[int(itemSelect)-1]

            itemOptions = input(f"You selected {selected}: {playerStart.inventory[selected]}! Would you like to drop it? (y/n): ")
            if(itemOptions == "y"):
                room[currentRoom].items[selected] = playerStart.inventory[selected]
                playerStart.inventory.pop(selected)

                print("You dropped the item!\n")
                print(room[currentRoom].description)

            elif(itemOptions == "n"): 
                print("You leave your inventory\n")
                print(room[currentRoom].description)  

            else:
                print("Invalid Option")  

    elif DI == "help":
        print("You can:\nType look to look for items in the room\n")

    else:
        print("Invalid selection")

    ##Reselect promt
    DI = input("Choose a direction (n,e,s,w), type help for more commands [q to quit]: ")
print("Good job adventurer! See you next time \n")