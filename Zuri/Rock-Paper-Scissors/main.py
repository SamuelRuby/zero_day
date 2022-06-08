import random
#my input
my_move = input('what move do you want to make?')
choices = {'1': 'rock', '2': 'paper', '3': 'scissors'}
my_action= choices[my_move]
#print len(choices.keys()) to get the number of keys in this dictionary or choices.keys() to get what keys are there


#my_action = ['rock', 'paper', 'scissors']
#making the computer choose
possible_events = ['rock', 'paper', 'scissors']
computer_move = random.choice(possible_events)

#print my choices and the computer's choices
print (f'\nRuby chose {my_action}, computer chose {computer_move}.\n')

#who wins
if my_action == computer_move:
    print(f"Both teams played {my_action}. It's a tie!")
elif my_action == 'paper':
    if computer_move == 'rock':
        print ('paper covers rock! I am the ultimate finisher! Ruby wins')
    else:
        print('scissors cuts paper! Your tears will be tasty. Ruby loses')
elif my_action == 'scissors':
    if computer_move == 'paper':
        print ('Scissors cuts paper. Now paper is trash. Ruby wins')
    else:
        print ('Rock smashes scissors! Blood is gonna flow. Ruby loses')
elif my_action == 'rock':
    if computer_move == 'scissors':
        print ('Rock smashes scissors! Time to paint the town red! Ruby wins')
    else:
        print ('Paper covers rock! Mocking Laugh! Ruby loses')
