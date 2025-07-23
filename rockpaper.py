import random


game = ["Rock", "Paper", "Scissor"]

while True:
    print("Rock\nPaper\nScissor")
    choice = input("enter your choice: ")
    print(f"User Choice: {choice}")
    comp_choice = random.choice(game)
    print(f"Comp-choice: {comp_choice}")
    if choice == comp_choice:
        print("It is Tie!")
    elif (choice == "Rock" and comp_choice == "Scissors") or \
         (choice == "Paper" and comp_choice == "Rock") or \
         (choice == "Scissors" and comp_choice == "Paper"):
        print("You win!")
    else:
        print("Computer Win!")
