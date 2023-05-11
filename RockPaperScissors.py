import pandas as pd
import time
import random
import csv

myChoices = []
computer_score = 0
your_score = 0
results = ('tie', 'computer wins', 'you win')
rps = ('rock', 'paper', 'scissors')
w = 0
while(w < 6*24):
    print('Pick your choice')
    input1 = input()
    if input1 in rps:
        myChoices.append(rps.index(input1))
        int1 = rps.index(input1.lower())
        int2 = random.randint(0,2)
        choice = rps[int2]
        print('computer chooses ' + choice)
        if (int1 == 0):
            x = (results[int2 - int1])
        elif(int1 == 1):
            if (int1 - int2 == 0):
                x = (results[0])
            elif(int1 - int2 > 0):
                x = (results[1])
            else:
                x = (results[2])
        if(int1 ==2):
            if (int1 - int2 == 0):
                x = (results[0])
            elif(int1 - int2 > 0):
                x = (results[2])
            else:
                x = (results[1])
        print(x)
        if (results.index(x) == 1):
            computer_score += 1
        if (results.index(x) == 2):
            your_score += 1
        print('your score ' + str(your_score))
        print('computer score ' + str(computer_score))
        w += 1
    else:
        print('choice not recognized')
    print('\n')

# File path
file_path = "/Users/ajcaesar/Desktop/AP CSA Project/RPS/rpsLearning.txt"

file = open(file_path, 'a')
file.write('\n')
file.writelines(str(choice) + ',' for choice  in myChoices)
file.close()