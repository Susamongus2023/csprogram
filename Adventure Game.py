print("Welcome to Hawthfire, the Adventure Game by Gjori Nykreim\n\n")
print("Within this game you will need to make a choice at every turn by choosing and typing in one of three choices.\n")
print("Beware, the Ghosts of Draconeus will follow you relentlessly as their intent is to remove you from the game.\n")
print("Your quest, should you choose to accept it, will be to slay Draconeus the Dragon, the most dangerous Dragon to ever exist.\n")
print("You will encounter creatures that may help you and foes that may try to eat you.\n\n")

Answer1=""

while Answer1 not in ["Start", "Nope", "Maybe"]:
    print("You have been warned. Are you ready to Embark On the Quest of Hawthfire? Type \"Start\" to start, \"Nope\" to not start, or \"Maybe\" for maybe")
    Answer1=input()
    anz1=""

    if Answer1 == "Nope":
        anz1 = "Come back later then if you would like."

    elif Answer1 == "Maybe":
        anz1 = "Well then, I recommend you figure it out and come back when you are ready."

    elif Answer1 == "Start":
        anz1 = "You are in the town of Bethelwood, you have a map directing you North towards the mountain where Draconeus lies. \nThere is also a shop to the east, and a festival to your west. Type NORTH to go North, Type EAST to go to the shop, and type WEST to go to the festival."

    else:
        print("Invalid input, try again gamer\n") 


Answer2=""

while Answer2 not in ["N", "E", "W"]:
    print(anz1)

    Answer2=input()

    Answer2 = Answer2.upper()

    Answer2 = Answer2[0]

    if Answer2 == "N":
        print("As you head North, you discover a forest full of wild pixies. However, they don't seem friendly. Would you like to attack them first, Try to walk past them, or rest here?")
        print("Type ATK to attack the pixies, Type WALK to try and walk past the pixies, or REST to rest on the ground here")

    elif Answer2 == "E":
        print("As you enter the shop, you see weapons and armor of many varities and the female shopkeeper greets you. She offers to sell you a beautiful sword and a steel coat of armor")
        print("Type BUY to buy the Sword and Armor, Type REF to refuse her offer, and type FLI to attempt to flirt with the shopkeeper.")

    elif Answer2 =="W":
        print("As you walk through the festival you see dancers, magicians, so many colors, and stands of every kind. However as you bask in this beautiful scene")
        print("You feel a sharp pain in your backside. A ghost of Draconeus has appeared behind you and inserted his dagger in your back. You have been removed from the game.")
        print("Restart the program to restart your adventure and make different choices!")

    else:
        print("Invalid input, try again gamer\n") 

Answer3=""

while Answer3 not in ["ATK", "WALK", "REST", "BUY", "REF", "FLI"]:
    Answer3=input()

    Answer3 = Answer3.upper()

    if Answer3 == "ATK":
        print("The Pixies swiftly enchant you after you swing your fist at them and use a spell to remove you from the game. Restart the program to restart the game and choose a different choice.")

    elif Answer3 == "WALK":
        print("unfortunately, you are not very sneaky. The pixies find you and cast a spell on you, thereby removing you from the game. Restart the program to restart the game and make a different choice.")

    elif Answer3 == "REST":
        print("As you rest, the pixies feel pity for you and slay Draconeus the Dragon in the mountain for you. You win the game!!! Congratulations!!!")

    elif Answer3 == "BUY":
        print("As you wield your new sword, a beam of light emerges from it, firing a laser into the mountain of Draconeus the Dragon. You have slain Draconeus. Congratulations! You beat the game and fulfilled you quest!")

    elif Answer3 == "REF": 
        print("The shopkeeper is upset you have declined her offer and thrusts a blade into your chest. You have been removed from the grame. Restart the program to try your quest again with different choices.")

    elif Answer3 == "FLI":
        print("You have successfully charmed her. After hearing of your quest, she opens up a case that has nucleur codes. Then, the shopkeeper nukes the mountain of Draconeus the Dragon. You win the game! Congratulations on completeing your quest!")

    else:
        print("Invalid input, try again gamer\n")

