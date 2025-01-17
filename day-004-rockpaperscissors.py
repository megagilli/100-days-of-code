
import random
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

game_images=[rock,paper,scissors]
user_choice= int(input("Type 0 for rock, 1 for paper and 2 for scissors\n"))
if user_choice>=0 or user_choice<=2:
    print(game_images[user_choice])
comp_choice = random.randint(0, 2)
print("computer chose :")
print(game_images[comp_choice])
if user_choice==0 and comp_choice==2:
    print("YOU WIN!!")
elif comp_choice ==0 and user_choice==2:
    print("YOU LOSE")
elif  comp_choice > user_choice:
    print("YOU LOST!!")
elif user_choice>comp_choice:
    print("YOU WIN!!")
elif comp_choice==user_choice:
    print("Its a DRAW!")
if user_choice>=3 or user_choice<0:
    print("Your type an invalid number, you LOSE!")


