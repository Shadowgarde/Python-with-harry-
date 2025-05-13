#This is the first project of the course, it is a simple game in which user user plays against the computer.
#The game is simple snake, water, gun,
'''I am using 
1 = snake 
-1 = water 
0 = gun  '''
import random


#I need to define what shows what to program 

Snake = 1
Water = -1
Gun = 0



#This function is used to create the random choice of the computer
def comp_choice():
    c = random.choice([1, 0 , -1])
    return c

#This function is used to get the user choice 
def user_choice():
    print('Please enter the your choice (1: snake, 0: gun, -1: water)')
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in [1, 0 , -1]:
                return choice
            else:
                print("Invalid input. Please choose 1, 0, or -1.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#This funtion is to check the winner of the game 

def check_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        print('Its a tie.')
        return 'tie'
    elif user_choice == 1 and comp_choice == -1:  #-1 = water
        print('You win this round.👍')
        return 'user'
    elif user_choice == 1 and comp_choice == 0:
        print('Computer wins this round.😎')
        return 'comp'
    elif user_choice == -1 and comp_choice == 1:            #All of these are the rules of the game.
        print('Computer wins this round.😎')
        return 'comp'
    elif user_choice == -1 and comp_choice == 0:
        print('You win this round.👍')
        return 'user'
    elif user_choice == 0 and comp_choice == 1:
        print('You win this round.👍')
        return 'user'
    elif user_choice == 0 and comp_choice == -1:
        print('Computer wins this round.😎')
        return 'comp'
    return user_choice, comp_choice

# #I am gonna create a seperate function for scores 
# def scores(user_choice, comp_choice):
#      user_score = 0
#      comp_score = 0   This is a mistake 
     

# This function is used to play the game 
def play_game():
    user_score = 0   #I needed it to define here
    comp_score = 0

    rounds = int(input("How many rounds do you want to play user: "))
    for i in range(rounds):
        print(f"\n--- Round {i+1} ---")
        user = user_choice()
        comp = comp_choice()
        print(f"You chose: {user}, Computer chose: {comp}")
        
        result = check_winner(user, comp)
        if result == 'user':
            user_score += 1
        elif result == 'comp':
            comp_score += 1
 #This doesn't work because we are using tuple in which making changes is imposible so this part is wrong.
     
     #Now we will set some final instruction for the game 
    print('\n=== Final Score ===')
    print(f'You: {user_score}, Computer: {comp_score}')  
    if user_score > comp_score:
        print("🎉 You win the game!")
    elif user_score < comp_score:
        print("💻 Computer wins the game!")
    else:
        print("🤝 It's a tie overall!")    




play_game()