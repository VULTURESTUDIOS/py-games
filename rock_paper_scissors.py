import random
opt = ["Rock", "Paper", "Scissor"]
score = 0
com_score = 0
while True:
    com = random.choice(opt)
    print("Enter your choice: Rock | Paper | Scissor,      (Enter 0 to exit the game )")
    user = input().lower()  # Convert user input to lowercase
    com = com.lower()  # Convert computer's choice to lowercase
    if user != '0':
            print(com)
    if com == 'paper' and user == 'rock':
        print("Computer Wins!")
        com_score +=1
    elif user == 'paper' and com == 'rock':
        print('You Win!')
        score +=1
    elif com == 'scissor' and user == 'paper':
        print("Computer Wins!")
        com_score +=1
    elif user == 'scissor' and com == 'paper':
        print("You Win!")
        score +=1
    elif com == 'rock' and user == 'scissor':
        print("Computer Wins!")
        com_score +=1
    elif com == 'scissor' and user == 'rock':
        print("You Win!")
        score +=1
    elif com == 'rock' and user == 'rock':
        print("Game Tied!")
    elif com == 'paper' and user == 'paper':
        print("Game Tied!")
    elif com == 'scissor' and user == 'scissor':
        print("Game Tied!")
    elif user == '0':
        print("I wouldn't have made an exit this early!")
        break
    else:
        print("Invalid Input!")
        break
    print("your score : ",score)
    print("computer's score:",com_score)