import random

#ASCIIS-- to download the images
# This program plays rock, paper, scissors with you. Enjoy
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
mode = [rock, paper, scissors]
player1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if player1 >=3 or player1 <0:
  print("You typed an invalid number, You lose")
else:
    
  print(mode[player1])
  
  
  computer_choice =random.randint(0, 2)
  print("The Computer's choice: ")
  print(mode[computer_choice])
  
  if player1 >=3 or player1 <0:
    print("You typed an invalid number, You lose")
  elif player1 == 0 and computer_choice ==2:
    print("You win")
  elif computer_choice == 0 and player1 ==2:
    print("You lose")
  elif computer_choice > player1:
    print("You lose")
  elif player1 > computer_choice:
    print("You win")
  elif player1 == computer_choice:
    print("It's a draw")
