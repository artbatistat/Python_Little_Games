import random

rock = '''
    _________
---'     ____)         
        (______)
        (______)
        (______)
-----.__(_____)

'''

paper = '''

    _________
---'     ____)_____         
        (__________)
        (__________)
        (__________)
-----.__(_________)

'''

scissors = '''
    _________
---'     ____)_____         
        (__________)
        (__________)
        (______)
-----.__(_____)

'''



userChose = int(input('What do you choose?\n'
                  'Type "0" for Rock,\n'
                  'Type "1" for Paper,\n'
                  'Type "2" for Scissors.\n'))

game = [rock,paper,scissors]

computerChose = random.randint(0,2)

print(f'You chose:\n'
      f'{game[userChose - 1]}')
    
print(f'Computer\'s chose:\n'
      f'{game[computerChose - 1]}')

if userChose < 0 or userChose > 2:
    print("You typed an invalid number.")
elif userChose == 0 and computerChose == 2:
    print("You win!")
elif computerChose == 0 and userChose == 2:
    print("You lose!")  
elif computerChose > userChose:
    print("You lose!")
elif userChose > computerChose:
    print("You win!")   
elif userChose == computerChose:
    print("It's a draw!")


