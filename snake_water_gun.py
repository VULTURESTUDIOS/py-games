import random
"""
Snake
Water
Gun
"""
opt = ["Snake", "Water", "Gun"]
mood = 1
while mood > 0:
    com = random.choice(opt)
    print("Enter your choice: Snake | Water | Gun")
    user = input().lower()  
    com = com.lower()
    print(com)
    if com == 'snake' and user == 'water':
        print("Computer Wins!")
    elif user == 'snake' and com == 'water':
        print('You Win!')
    elif com == 'water' and user == 'gun':
        print("Computer Wins!")
    elif user == 'water' and com == 'gun':
        print("You Win!")
    elif com == 'gun' and user == 'snake':
        print("Computer Wins!")
    elif user == 'snake' and com == 'gun':
        print("You Win!")
    elif com == 'snake' and user == 'snake':
        print("Game Tied!")
    elif com == 'water' and user == 'water':
        print("Game Tied!")
    elif com == 'gun' and user == 'gun':
        print("Game Tied!")
    else :
        print("Invalid Input!")
        break

    
        
        

    
        