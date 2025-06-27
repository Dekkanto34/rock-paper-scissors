import random
yourscore = 0
computerscore = 0 
while yourscore < 3 and computerscore < 3: 
    yourchoice = input("Make a decision [rock, paper, scissors]")
    possibilities = ["rock", "paper", "scissors"]
    computerchoice = random.choice(possibilities)
    print("You deciced on: ", yourchoice)
    print("Computer decided on: ", computerchoice)
    if yourchoice == "rock" and computerchoice == "paper":
        print("Computer won.")
        computerscore = computerscore + 1
    elif yourchoice == "rock" and computerchoice == "scissors":
        print("You won.")
        yourscore = yourscore + 1
    elif yourchoice == "paper" and computerchoice == "rock":
        print("You won.")
        yourscore = yourscore + 1
    elif yourchoice == "paper" and computerchoice == "scissors":
        print("Computer won.")
        computerscore = computerscore + 1
    elif yourchoice == "scissors" and computerchoice == "rock":
        print("Computer won.")
        computerscore = computerscore + 1
    elif yourchoice == "scissors" and computerchoice == "paper":
        print("You won.")
        yourscore = yourscore + 1
    elif yourchoice == computerchoice:
        print("Draw.")
    print("Y", yourscore, "C", computerscore)
 
