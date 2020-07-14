import random

# create a list
list = ["rock", "paper", "scissors"]

computer_choice = random.choice(list)

player = False
player_score = 0
computer_score = 0

while player == False:
    print("New Round!")
    print("Player score: ", player_score)
    print("Computer score: ", computer_score)
    #take input from user
    player = input("Enter 1. Rock 2. Paper  3. Scissors or 4. Exit: ")

    # draw
    if player.lower() == computer_choice:
        print("Draw")
    # player choice rock
    elif player.lower() == "rock" or int(player.lower()) == 1:
        if computer_choice == "paper":
            computer_score += 1
            print("You lose", computer_choice, "beats", player)
            
        else: 
            player_score += 1
            print("You win!", player, "beats",computer_choice)
            

    # player choice paper
    elif player.lower() == "paper" or int(player.lower()) == 2:
        if computer_choice == "scissors":
            computer_score += 1
            print("You lose", computer_choice, "beats", player)
            
        else:
            player_score += 1
            print("You win!", player, "beats", computer_choice)
            

    # player choice scissors
    elif player.lower() == "scissors" or int(player.lower()) == 3:
        if computer_choice == "rock":
            computer_score += 1
            print("You lose", computer_choice, "beats", player)
            
        else:
            player_score += 1
            print("You win!", player, "beats", computer_choice)
            
        
    #player choice exit
    elif player.lower() == "exit" or int(player.lower()) == 4:
        break

    else:
        print("Please enter either rock, paper, scissors or exit ")

    player = False
    #select random choice from list
    computer_choice = random.choice(list)