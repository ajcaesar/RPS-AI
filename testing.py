import random
from reformatting_data import change


def playRockPaperScissors():
    myChoices= []
    data = -1
    results = ('tie', 'computer wins', 'you win')
    rps = ('rock', 'paper', 'scissors')
    w = 0
    while(w < 23):
        print('\n Pick your choice')
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
            w += 1
        else:
            print('choice not recognized')
        
    while(data == -1):
        print('\n Pick your choice')
        input2 = input()
        if input2 in rps:
            data = rps.index(input2)
        else:
            print('choice not recognized')
    
    return(myChoices, data)

        
        
