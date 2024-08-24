import random
choice = input("Rock(R), Paper(P), or Scissors(S)?\n ")
robot = random.randint(1,3)
if choice == "R":
    if robot == 1:
        print("Tie")
    if robot == 2:
        print("You lose, robot chose Paper")
    if robot == 3:
        print("You win, robot chose scissors")
elif choice == "P":
    if robot == 1:
        print("You win, robot chose rock")
    if robot == 2:
        print("Tie")
    if robot == 3:
        print("You lose, robot chose scissors")
else:
    if robot == 1:
        print("You lose, robot chose rock")
    if robot == 2:
        print("You win, robot chose paper")
    if robot == 3:
        print("Tie")

