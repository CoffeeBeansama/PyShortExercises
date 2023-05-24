import random

objects = ["Rock","Paper","Scissors"]
print("Rock Paper Scissors Game")

while True:

    player_input = str(input("Choose an object: Rock,Paper,Scissors: "))

    Random_object = random.choice(objects)


    if player_input in objects:

        print("Computer choose: ", Random_object)
        if player_input != Random_object:

            if player_input == "rock" and Random_object == "Paper":
                print("You Lose")
                break

            if player_input == "paper" and Random_object == "Scissors":
                print("You Lose")
                break

            if player_input == "scissors" and Random_object == "Rock":
                print("You Lose")
                break

            print("You win, Try again! ")
        else:
            print("Its a draw!! Try again")


    else: print("That is not an object!!!")













