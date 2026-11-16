#Welcome the player
print("===ESCAPE THE CASTLE===")
print("Welcome sad one. You are in a bit of a tough situation, so best of luck with escaping the old king's grasp. You will need it.")

#Get player name, age and character class
charName = input("Tell me, what is your name? ")
age = int(input("Good. And how many years have you lived before now? "))
charClass = input("How sad. And what is your class? I need to know if there is anything special about you. ")
print("I think I can work with that. You might not die here.")

#Set starting values
playerhealth = 100
gold = 20
hasCellKey = False
hasGateKey = False
hasRustyDagger = False
isCaptured = True
inventory = []

#Display the character profile
print("\n===CHARACTER PROFILE===")
print(f"Name: {charName}")
print(f"Age: {age}")
print(f"Class: {charClass}")
print(f"Health: {playerhealth}")
print(f"Gold: {gold}")
print(f"Has Cell Key: {hasCellKey}")

print("\n=====================================")
print("ESCAPE THE CASTLE - SCENE 1: THE CELL")
print("=====================================")

def cell():
    hasCellKey = False
    print("You wake up in a dark castle cell.")
    print("You can see a dingy door, a barred, filthy window and an old, rickety bed.")
    choice = input("Do you want to investigate the door, window or bed?: ").lower()
    
    while hasCellKey != True:
        if choice == "door":
            print("You walk towards the door.")
            print("You try the handle, but it is locked.")
            choice = input("Do you want to investigate the window or the bed?: ").lower()
        elif choice == "window":
            print("You look through the window, not seeing much.")
            print("The bars prevent your escape.")
            choice = input("Do you want to investigate the door or the bed?: ").lower()
        elif choice == "bed":
            print("You peer under the bed.")
            print("You find a small iron key.")
            inventory.append("Iron Key")
            hasCellKey = True
            choice = input("Do you want to investigate the door or the window?: ").lower()
        else:
                print("You decide not to investigate, but you have nothing else to do.")
                choice = input("Do you want to investigate the window, bed or door?: ").lower()
    
    while hasCellKey == True:
        if choice == "window":
            print("You look through the window, not seeing much.")
            print("The bars prevent your escape.")
            choice = input("Do you want to investigate the door or the bed?: ").lower()
        elif choice == "bed":
            print("You peer under the bed.")
            print("Nothing else is there.")
            choice = input("Do you want to investigate the door or the window?: ").lower()
        elif choice == "door":
            print("You unlock the cell door, and hesitantly step into the corridor.")
            inventory.remove("Iron Key")
            hascellKey = False
            isCaptured = False
            break
        else:
            print("You decide not to investigate, but you have nothing else to do.")
            choice = input("Do you want to investigate the window, bed or door?: ").lower()

cell()
choice = input("\nWould you like to continue?: ")
if choice == "yes":
     print("You continue down the corridor.")
while choice == "no":
     choice = input("You stay where you are, looking as awkward as you feel. Do you want to stop being awkward?: ")

print("\n=========================================")
print("ESCAPE THE CASTLE - SCENE 2: THE CORRIDOR")
print("=========================================")

# Create a list to store the player's inventory
# We are assuming the player already found the key

def corridor():
    print("\n As you continue down the corridor, you notice an old wooden cabinet.")
    choice = input("Do you open the cabinet? yes/no: ").lower()
    if choice == "yes":
        print("You open the cabinet")
        print("Inside. you find a Rusty Dagger!")
        hasRustyDagger = True
        inventory.append("Rusty Dagger")
        print("You pick up the dagger, then close the cabinet and continue on.")
    elif choice == "no":
        print("You leave the cabinet closed, then continue on.")

corridor()
import random
creaturehealth = 100
playerhealth = 100

def gameover():
    print("You are struck down for the final time. The last thing you hear before everything fades to black is the clinking of multiple sets of armour.")
    print("You wake up, back in your cell. Have fun.")
    isCaptured = True
def murderer():
    print("You successfully finished the fight... with a casuality. You scurry down the hall, contemplating your crimes.")
def gameover_ghost():
        print("\nThe ghost strangles you with shockingly corporeal hands. The last thing you see is the ghost's face twisting in pain and regret.")
        print("You wake again sometime later, back in your cell. ")
def gameover_dog():
        print("\nThe dog clamps its teeth around your neck, and the fight literally bleeds out of you as everything fades to black.")
        isAlove = False
def gameover_guard():
        print("\nThe guard catches you for the last time time, striking you down. The last thing you hear before death claims you is the guard, proudly proclaiming victory.")
        isAlive = False
def murderer_ghost():
        print("\nYou somehow managed to slay a ghost. Given the sad state they were in, it may have been for the best. You continue down the hallway, a little uneased.")
def murderer_dog():
        print("\nYou killed a dog. Wow. You continue down the hallway, either trying not to sob or basking in your cruelty.")
def murderer_guard():
        print("\nYou successfully murdered the guard! I wonder if they had a family.. You scurry down the corridor, contemplating your crimes.")

def corridorEncounter():
    isCaptured = False
    playerhealth = 100
    creaturehealth = 100
    print("You walk down a dark castle corridor.")
    print("You hear a strange noise ahead.")
    creatures = ["guard", "ghost", "guard dog"]
    random_creature = random.choice(creatures)
    
    if random_creature == "guard" and hasRustyDagger == True:
        print("\nA guard appears, body and face hidden by armour.")
        print("They draw their sword and say: 'Ha! You are the treasonous wretch who commited praemunire! You shall not escape justice.'")
        print("You pull your Rusty Dagger out, looking for any vulnerabilities.")
            
    if random_creature == "ghost" and hasRustyDagger == True:
        print("\nA scruffy ghost floats into view, blood and ash covering the front of their shirt. They seem sad.")
        print("They start to... swell? Then they shrink, then swell again, repeating the same, jerky movements while moaning sadly.")
        print("You pull your Rusty Dagger out, and the ghost shrieks, glaring at you.")

    if random_creature == "guard dog" and hasRustyDagger == True:
        print("\nA guard dog appears, wearing a protective vest.")
        print("It bears its teeth, growling as it prepares to pounce..")
        print("You pull your Rusty Dagger out, eyeing up any exposed spots.")

    if random_creature == "guard" and hasRustyDagger != True:
        print("\nA guard appears, body and face hidden by armour.")
        print("They draw their sword and say: 'Ha! You are the treasonous wretch who commited praemunire! You shall not escape justice.'")
        print("You instinctively take a step back, moving into a fighting position.")

    if random_creature == "ghost" and hasRustyDagger != True:
        print("\nA scruffy ghost floats into view, blood and ash covering the front of their shirt. They seem sad.")
        print("They start to... swell? Then they shrink, then swell again, repeating the same, jerky movements while moaning sadly.")
        print("You instinctively take a step back, moving into a fighting position. The ghost suddenly shrieks, glaring at you.")

    if random_creature == "guard dog" and hasRustyDagger != True:
        print("\nA guard dog appears, wearing a protective vest.")
        print("It bears its teeth, growling as it prepares to pounce..")
        print("You instinctively take a step back, moving into a fighting position.")
    
    choice = input(f"The {random_creature} suddenly charges! Do you try to dodge or fight?: ").lower()
    
    while playerhealth > 0 and creaturehealth > 0 and isCaptured == False:
        if choice == "dodge" and playerhealth > 0 and creaturehealth > 0:
            dodge_success_chance = random.randint(1,6)
            if dodge_success_chance == 6:
                creaturehealth = creaturehealth - 10
                print(f"\nYou dodge so quickly that the {random_creature} becomes confused, and crashes into the wall. The {random_creature} loses 10 health points.")
                print(f"Your health is {playerhealth} health points and the {random_creature}'s is {creaturehealth} health points.")
                if creaturehealth <= 0:
                    murderer()
                if creaturehealth > 0 and playerhealth > 0:
                    choice = input("Do you try to dodge or fight?: ").lower()

            if dodge_success_chance == 4 or 5:
                print(f"\nYou successfully dodge, rolling out of the way of the {random_creature}'s attack.")
                print(f"Your health is {playerhealth} health points and the {random_creature}'s is {creaturehealth} health points.")
                if creaturehealth > 0 and playerhealth > 0:
                    choice = input("Do you try to dodge or fight?: ").lower()
            
            if dodge_success_chance == 2 or 3:
                playerhealth = playerhealth - 10
                print("\nYou barely dodge, being mildly grazed across your arm. You lose 10 health points.")
                print(f"Your health is {playerhealth} health points and the {random_creature}'s is {creaturehealth} health points.")
                if playerhealth <= 0:
                    gameover()
                if creaturehealth > 0 and playerhealth > 0:
                    choice = input("Do you try to dodge or fight?: ").lower()
                
            if dodge_success_chance == 1:
                playerhealth = playerhealth - 20
                print("\nYou fail to dodge, getting sliced across your chest. You lose 20 health points.")
                print(f"Your health is {playerhealth} health points and the {random_creature}'s is {creaturehealth} health points.")
                if playerhealth <= 0:
                    gameover()
                if creaturehealth > 0 and playerhealth > 0:
                    choice = input("Do you try to dodge or fight?: ").lower()
        elif choice == "fight" and playerhealth > 0 and creaturehealth > 0 and hasRustyDagger == True:
            fight_success_chance = random.randint(1,6)
            if fight_success_chance == 6:
                creaturehealth = creaturehealth - 20
                print(f"You stab the {random_creature} in one of the limbs, a little bit of rust flaking off in the process, adding insult to possibly infected injury.")
                print(f"The {random_creature} loses 20 health points.")
                print(f"Your health is {playerhealth} health points and the {random_creature}'s is {creaturehealth} health points.")
                if creaturehealth <= 0:
                    murderer()
                if creaturehealth > 0 and playerhealth > 0:
                    choice = input("Do you try to dodge or fight?: ").lower()

            
            if fight_success_chance == 5:
                creaturehealth = creaturehealth - 10
                print(f"You slash at the {random_creature}, leaving a decent mark behind, while avoiding getting hit.")
                print(f"The {random_creature} loses 10 health points.")
                print(f"Your health is {playerhealth} health points and the {random_creature}'s is {creaturehealth} health points.")
                if creaturehealth <= 0:
                    murderer()
                if creaturehealth > 0 and playerhealth > 0:
                    choice = input("Do you try to dodge or fight?: ").lower()
                
            
            if fight_success_chance == 4:
                creaturehealth = creaturehealth - 5
                print(f"You land a hit on the {random_creature}, though it is very shallow. You manage to roll out of the way before getting hit.")
                print(f"The {random_creature} loses 5 health points.")
                print(f"Your health is {playerhealth} health points and the {random_creature}'s is {creaturehealth} health points.")
                if creaturehealth <= 0:
                    murderer()
                if creaturehealth > 0 and playerhealth > 0:
                    choice = input("Do you try to dodge or fight?: ").lower()
            
            if fight_success_chance == 3:
                playerhealth = playerhealth - 5
                creaturehealth = creaturehealth - 5
                print("You manage to get a cut in, though it very mild. In the process, you get grazed, though it is also very mild.")
                print(f"You and the {random_creature} lose 5 health points.")
                print(f"Your health is {playerhealth} health points and the {random_creature}'s is {creaturehealth} health points.")
                if creaturehealth <= 0:
                    murderer()
                if playerhealth <= 0:
                    gameover()
                if playerhealth <= 0 and creaturehealth <= 0:
                    print("You finally managed to take the creature down... and got yourself knocked out in the process.")
                    print("Considering how weak both of your attacks were, that's embarrassing for both of you.")
                    isAlive = False
                if creaturehealth > 0 and playerhealth > 0:
                    choice = input("Do you try to dodge or fight?: ").lower()
            
            if fight_success_chance == 2:
                playerhealth = playerhealth - 10
                print("Your attempt at striking goes awry, and you have to dive out of the way at the last second.")
                print("You don't quite manage that either, and receive an unpleasant mark on your leg, losing 10 health points.")
                print(f"Your health is {playerhealth} health points and the {random_creature}'s is {creaturehealth} health points.")
                if playerhealth <= 0:
                    gameover()
                if creaturehealth > 0 and playerhealth > 0:
                    choice = input("Do you try to dodge or fight?: ").lower()
            if fight_success_chance == 1:
                playerhealth = playerhealth - 20
                print(f"You completely fail to attack the {random_creature}, and end up the victim instead. You lose 20 health points.")
                print(f"Your health is {playerhealth} health points and the {random_creature}'s is {creaturehealth} health points")
                if playerhealth <= 0:
                    gameover()
                if creaturehealth > 0 and playerhealth > 0:
                    choice = input("Do you try to dodge or fight?: ").lower()
        elif choice == "surrender":
            print("You give in! You are not so gently shoved back towards the cell, where you are locked in. Have fun doing that again.")
            isCaptured = True
        else:
            playerhealth = playerhealth - 20
            print("That is not an option. In your hesitation you are attacked, and you lose 20 health points.")
            if playerhealth <= 0:
                gameover()
            if creaturehealth > 0 and playerhealth > 0:
                choice = input("Do you try to dodge or fight?: ").lower()

corridorEncounter()
# while isCaptured == True:
#     cell()
#     corridor()
#     corridorEncounter()

def corridor2():
    hasGateKey = False
    hasLeft = False
    print("\nHaving finally escaped, you hurry down the hallway, trying not to make too much noise.")
    choice = input("Eventually, you reach a large, ornate door.")
    choice = input("Do you open the door?: ")
    if choice == "no":
        choice = input("You just stand there, looking awkward. Do you want to stop looking awkward?: ")
    if choice == "yes":
        print("You push the door open slighly, and step quietly into a giant library.")
    else:
        print("That is not an option, and you just stand there, twiddling your thumbs.")
        choice = input("Are you going to open the door?: ")

def library():
    print("\n You wander into the library, looking around at the impressive architecture.")
    print("Three areas in particular catch your eye.")
    print("The great row of bookshelves, stuffed with books and scrolls")
    print("The sitting area, covered in plush seats.")
    print("A gorgeous fireplace, adorned with gold accents.")
    print("There is also another large ornate door at the end of the room.")
    choice = input("\nDo you leave, or investigate the fireplace, bookshelves or the seats?: ").lower
    
    while hasLeft == False and hasGateKey == False:
        if choice == "bookshelves":
            print("You study the books, looking for anything useful. All you find is an odd marking etched into one of the shelves, with a lock and a reference to hell.")
            hasLeft = False
            choice = input("Do you investigate the fireplace or the seats?: ").lower()
        elif choice == "seats":
            print("You examine the seats, finding an interesting arrow the legs of one of the chairs that is pointing downwards. You find nothing else of note.")
            hasLeft = False
            choice = input("Do you investigate the fireplace or the bookshelves? Or do you leave?: ").lower()
        elif choice == "fireplace":
            print("You run your hands along the fireplace, admiring the intricate designs when a large silver key falls out from a hidden nook on the inside.")
            hasLeft = False
            hasGateKey = True
            choice = input("Do you investigate the bookshelves or the seats? Or do you leave?: ").lower()
        elif choice == "leave":
            print("You push open the second ornate door, stepping out into the front of the castle.")
            hasLeft = True
        else:
            print("That is not an option. You just stand there, staring at everything. Creepy.")
            choice = input("Do you want to investigate the fireplace, bookshelves or seats, or do you want to leave?: ").lower()

    while hasLeft == False and hasGateKey == True:
        if choice == "fireplace":
            print("You find nothing of note, though it is pretty.")
        elif choice == "bookshelves":
            print("You study the books, looking for anything useful. All you find is an odd marking etched into one of the shelves, with a lock and a reference to hell.")
            hasLeft = False
            choice = input("Do you investigate the fireplace or the seats?: ").lower()
        elif choice == "seats":
            print("You examine the seats, finding an interesting arrow the legs of one of the chairs that is pointing downwards. You find nothing else of note.")
            hasLeft = False
            choice = input("Do you investigate the fireplace or the bookshelves? Or do you leave?: ").lower()
        elif choice == "leave":
            print("You push open the second ornate door, stepping out into the front of the castle.")
            hasLeft = True
        else:
            print("That is not an option. You just stand there, staring at everything. Creepy.")
            choice = input("Do you want to investigate the fireplace, bookshelves or seats, or do you want to leave?: ").lower()

        

    while hasLeft == True:
        print("You step out into a sheltered part of the castle's garden, the castle gate way ahead of you.")
        choice = input("Do you want to continue or return to the library?: ").lower()
        if choice == "return":
            hasLeft = False
            print("You step back into the quiet of the library.")
            choice = input("Do you want to investigate the fireplace, the bookshelves ").lower()
        elif choice == "continue":
            print("You walk towards the large gate, admiring it.")

def castleGate():
    if hasGateKey == True:
        print("You walk over to the gate, and pull out the large key you find in the library. You slot it into gate's lock, and open the gate.")
        print("You step out of the castle gate, and rush forward, getting lost in the city streets as you revel in your freedom.")
        print("You have escaped! Try to stay out of trouble.")
    elif hasGateKey == False:
        print("The gate is your final obstacle, and you have no way of overcoming it.")
        choice = input("Do you just stand around, or go back inside?: ")
        if choice == "stand around":
            choice = input("You just stand there. Do you want to keep just standing around, or do you want to go back inside?")
        elif choice == "go inside" or "go back inside" or "return" or "go back" or "inside" or "back" or "go":
            library()

corridor2()
library()
castleGate()