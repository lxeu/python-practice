import random

choice = input("what do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. ")

computer_choice = str(random.randint(0,2))

if choice == "0":
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif choice == "1":
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif choice == "2":
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print("Please enter either 0, 1, or 2.")

if computer_choice == "0":
    print("Computer chose:")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    if computer_choice == choice:
        print("Tie")
    elif choice == "1":
        print("You win")
    else:
        print("You lose")
elif computer_choice == "1":
    print("Computer chose:")
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    if computer_choice == choice:
        print("Tie")
    elif choice == "2":
        print("You win")
    else:
        print("You lose")
else:
    print("Computer chose:")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    if computer_choice == choice:
        print("Tie")
    elif choice == "0":
        print("You win")
    else:
        print("You lose")