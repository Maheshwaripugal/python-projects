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
import random
myinput = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
if myinput == 0:
    print(rock)
if myinput == 1:
    print(paper)
if myinput == 2:
    print(scissors)
print("Computer chose")
Computer = int(random.choice(["0", "1", "2"]))
if Computer == 0:
    print(rock)
if Computer == 1:
    print(paper)
if Computer == 2:
    print(scissors)