treasure ='''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________/
*******************************************************************************
'''
print(treasure)
print(f'Welcome to Treasure Island.\n'
      f'Your mission is to find the treasure.\n'
    )

choice_1 = input('You\'are at a crossroad, where do you want to go?\n'
                 'Type "left" or "right".\n').lower()

if choice_1 == "left":
    choice_2 = input('You\'ve come to a lake.\n'
                     'There is an island in the middle of the lake.\n'
                     'Type "wait" to wait for a boat\n'
                     'Type "swim" to swim across.\n').lower()
    if choice_2 == "wait":
        choice_3 = input('You arrive at the island unharmed.\n'
                         'There is house with 3 doors.\n'
                         ' *One Red, One Blue and One Yellow\n'
                         'Which colour do you choose?\n').lower()
        if choice_3 == "red":
            print('It\'s a room full of fire. Game Over...')
        elif choice_3 == "blue":
            print('You enter a room of beasts. Game Over...')
        elif choice_3 == "yellow":
            print('You found the treasure. You Win!!!\n')
            print(treasure)
        else:
            print('You choose a door that doesn\'t exist. Game Over...')
    elif choice_2 == "swim":
        print('You got attacked by an angry trout. Game Over...')
    else:
        print('You choose an action that doesn\'t exist. Game Over...')
elif choice_1 == "right":
    print('You fell in to a hole. Game over...')
else:
    print('You choose a direction that doesn\'t exist. Game Over...')
