# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, refID, name, description, items):
        self.refID = refID
        self.name=  name
        self.description = description
        self.items = items
    
    def look(self):
        changedItems = {}

        for item in list(self.items.items()):

            itemName = item[0]
            itemDescription = item[1]

            print(f"you find {itemName}: {itemDescription}")
            action = input('Would you like to take the item? y/n : ')

            if(action == "y"):
                print(f"{itemName} added to inventory \n")
                self.items.pop(itemName)
                changedItems[itemName] = itemDescription

            elif(action == "n"):
                print(f"You decide not to take the item \n")

            else:
                print("Invalid Input")
        return changedItems

    def __str__(self):
        return f"{self.name}: {self.description}"