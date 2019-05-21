#takes two random numbers and decides if they are the same or not
#the program keeps running until it picks two equal numbers
#the program prints the two equal numbers, as well as the amount of times
#the program had to run to find the match

import random
def sampleFunc():
    z = 0
    while True:
        x = random.randint(1,100)
        y = random.randint(1,100)
        z = z + 1
        if x == y:
            print('x = ' + str(x))
            print('y = ' + str(y))
            print('z = ' + str(z))
            break
        
