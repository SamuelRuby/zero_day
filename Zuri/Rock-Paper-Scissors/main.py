import random
#my input
player_name = input('What is your name?')
my_move = input('what move do you want to make?')
choices = {'1': 'rock', '2': 'paper', '3': 'scissors'}
my_action= choices[my_move]
#print len(choices.keys()) to get the number of keys in this dictionary or choices.keys() to get what keys are there


#my_action = ['rock', 'paper', 'scissors']
#making the computer choose
possible_events = ['rock', 'paper', 'scissors']
computer_move = random.choice(possible_events)

#print my choices and the computer's choices
print (f'\n{player_name} chose {my_action}, computer chose {computer_move}.\n')

#who wins
if my_action == computer_move:
    print(f"Both teams played {my_action}. It's a tie!")
elif my_action == 'paper':
    if computer_move == 'rock':
        print ('paper covers rock! I am the ultimate finisher! {player_name} wins!')
    else:
        print('scissors cuts paper! Your tears will be tasty. {player_name} loses!')
elif my_action == 'scissors':
    if computer_move == 'paper':
        print ('Scissors cuts paper. Now paper is trash. {player_name} wins')
    else:
        print ('Rock smashes scissors! Blood is gonna flow. {player_name} loses')
elif my_action == 'rock':
    if computer_move == 'scissors':
        print ('Rock smashes scissors! Time to paint the town red! {player_name} wins')
    else:
        print ('Paper covers rock! Mocking Laugh! {player_name} loses')
