print("=== ELBAPH: THE LAND OF GIANTS ===")
print("The Straw Hats have landed on Elbaph, the legendary land of warriors.")
print("Your goal: earn the giants' trust and reach Harley, the Tree of Yggdrasil.\n")

name = input("Enter your name, traveler: ")
print(f"Welcome to Elbaph, {name}!\n")

trust = 0
has_meat = False

# Choice 1: Arrival
print("You arrive at the giant village of Útgarðr. A huge giant blocks your path.")
print("1. Challenge him to a fight")
print("2. Bow and ask to meet the elders")
print("3. Sneak past him")
choice = input("What do you do? (1/2/3): ")

if choice == "1":
    print("\nYou charge at the giant! He laughs and flicks you away.")
    print("Giants respect courage, though, and he grins at you.")
    trust += 1
elif choice == "2":
    print("\nThe giant is impressed by your manners and leads you to the elders.")
    trust += 2
elif choice == "3":
    print("\nYou try to sneak by, but the giant's foot comes down right in front of you.")
    print("'Cowards are not welcome here!'")
    trust -= 1
else:
    print("\nYou hesitate too long and the giant carries you off like a doll.")

# Choice 2: Feast
print("\nThe giants invite you to a feast. A mountain of meat sits in front of you.")
print("1. Eat as much as you can")
print("2. Politely take a small portion")
print("3. Refuse to eat")
choice = input("What do you do? (1/2/3): ")

if choice == "1":
    print("\nYou eat like Luffy! The giants roar with laughter and cheer you on.")
    trust += 2
    has_meat = True
elif choice == "2":
    print("\nThe giants nod politely, but they seem a little disappointed.")
    trust += 1
    has_meat = True
elif choice == "3":
    print("\nThe giants gasp. Refusing a giant's food is a huge insult!")
    trust -= 2
else:
    print("\nYou stand there confused. The giants shrug and keep eating.")

# Choice 3: Sea King attack (depends on earlier choices)
print("\nOn the way to Harley, a giant Sea King rises from the river!")

if has_meat:
    print("You still have some meat with you.")
    print("1. Throw the meat to distract the Sea King")
    print("2. Fight it head on")
    choice = input("What do you do? (1/2): ")

    if choice == "1":
        print("\nThe Sea King gobbles up the meat and swims away happily.")
        trust += 1
        has_meat = False
    elif choice == "2":
        print("\nYou fight bravely and drive it off, but you get hurt.")
        trust += 1
    else:
        print("\nYou freeze. Luckily a giant warrior saves you.")
        trust -= 1
else:
    print("You have no food to distract it.")
    print("1. Fight it head on")
    print("2. Run away")
    choice = input("What do you do? (1/2): ")

    if choice == "1":
        print("\nYou stand your ground and win. The giants are amazed!")
        trust += 2
    elif choice == "2":
        print("\nYou run, and a giant has to protect you.")
        trust -= 2
    else:
        print("\nYou freeze. Luckily a giant warrior saves you.")
        trust -= 1

# Choice 4: Meeting the elder (nested if)
print("\nAt last you reach the base of Harley, the Tree of Yggdrasil.")
print("Old Giant Elder Jarul blocks the way and asks:")
print("'Why do you want to climb this tree?'")

if trust >= 4:
    print("\nThe elder smiles. 'The giants speak highly of you.'")
    print("1. Say you want to learn the truth of the world")
    print("2. Say you want treasure")
    choice = input("Your answer? (1/2): ")

    if choice == "1":
        print("\nThe elder steps aside and lets you climb.")
        print("\n*** ENDING: THE DREAMER ***")
        print(f"{name} learns the secrets of Elbaph and the giants' great history!")
    elif choice == "2":
        print("\nThe elder frowns, but he trusts you enough to let you pass.")
        print("\n*** ENDING: THE TREASURE HUNTER ***")
        print(f"{name} climbs Harley, but wonders if the treasure was worth it.")
    else:
        print("\nYou mumble something. The elder chuckles and lets you climb anyway.")
        print("\n*** ENDING: THE LUCKY ONE ***")
elif trust >= 1:
    print("\nThe elder squints at you. 'You are not a bad one, but you are not ready.'")
    print("1. Ask for a duel to prove yourself")
    print("2. Leave and come back later")
    choice = input("What do you do? (1/2): ")

    if choice == "1":
        print("\nYou duel the elder's giant guard and lose, but you earn his respect.")
        print("\n*** ENDING: THE CHALLENGER ***")
        print(f"{name} is allowed to climb Harley next time.")
    elif choice == "2":
        print("\nYou leave and train hard with the giants.")
        print("\n*** ENDING: THE APPRENTICE ***")
        print(f"{name} will return one day, stronger than before.")
    else:
        print("\nYou stand there doing nothing until sunset.")
        print("\n*** ENDING: THE WANDERER ***")
else:
    print("\n'Trespasser! The giants have no trust in you!'")
    print("The elder lifts his axe and you are thrown out of the village.")
    print("\n*** ENDING: BANISHED FROM ELBAPH ***")
    print(f"{name} will have to earn the giants' trust another day.")

print(f"\nFinal trust score: {trust}")
print("Thanks for playing!")
