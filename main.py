### Print a welcome message
print("Welcome to the Family House!")
print("You are a son of a family millioare and the house is now yours.")
print("As the newfound owner, you decide to pay a visit to the house.")
print("The house is dated, creaky and falling appart. You walk in the front door.")
print("Do you want to enter the living room or the dining room?")

### Prompt user for a choice
roomChoice = input("> ")

if(roomChoice == "living room"):
    print("You entered the living room.")
    print("As you walk in, there is a huge vase on the table.")
    print("Do you want to steal the vase?")

    vaseChoice = input("> ")

    if(vaseChoice == "yes"):
        print("You attempt to steal the vase, but you drop it and break it. You run away and leave the house.")
    elif(vaseChoice == "no"):
        print("You decide to not steal the vase.")
        print("You find a beautiful old watch behind the vase.")
    else:
        print("Invalid choice. Please enter yes or no.")
elif(roomChoice == "dining room"):
    print("You chose to go into the dining room.")
    print("As you walk in, you see a big cat on the table.")
    print("It has a diamond necklace on its neck.")
    print("Do you want to take it?")

    necklaceChoice = input("> ")

    if(necklaceChoice == "yes"):
        print("You tried to take it and the cat cuts your skin and you die!!")
    elif(necklaceChoice == "no"):
        print("You leave the house safely and go home.")
    else:
        print("Invalid choice. Please enter yes or no.")
else:
    print("Invalid choice. Please enter living room or dining room.")