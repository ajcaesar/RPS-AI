import pandas as pd
import time
import random
import matplotlib.pyplot as plt

computer_score = 0
your_score = 0
results = ('tie', 'computer wins', 'you win')
rps = ('rock', 'paper', 'scissors')
w = 0
i = 0
youList = []
computerList = []
while(w < 100):
    while(i < 30000):
        int1 = random.randint(0,2)
        int2 = random.randint(0,2)
        if (int1 == 0):
            if (int1 - int2 == 0):
                x = (results[0])
            elif(int1 - int2 < -1):
                x = (results[1])
                your_score += 1
            else:
                x = (results[2])
                computer_score+=1
        elif(int1 == 1):
            if (int1 - int2 == 0):
                x = (results[0])
            elif(int1 - int2 < 0):
                x = (results[1])
                your_score += 1
            else:
                x = (results[2])
                computer_score+=1
        if(int1 == 2):
            if (int1 - int2 == 0):
                x = (results[0])
            elif(int1 - int2 < 2):
                x = (results[2])
                computer_score +=1
            else:
                x = (results[1])
                your_score += 1
        i+=1     
    youList.append(float(your_score)/30000.0)
    computerList.append(float(computer_score)/3000.0)
    w+=1
    i = 0
    your_score = 0
    computer_score = 0

bin_edges = []
yep = 0.3
while (yep <= 0.35):
    bin_edges.append(yep)
    yep += 0.001

plt.hist(youList, bins = bin_edges, color='skyblue', edgecolor='black')
plt.title("Your Wins")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

plt.hist(computerList, bins= bin_edges, color='skyblue', edgecolor='black')
plt.title("Computer Wins")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


    
    