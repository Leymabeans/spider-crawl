import time


def countdown(n) :
    #Runs until a set timer has counted down
    while n > 0:
        time.sleep(1)
        print (n)
        n = n - 1
        if n == 0:
            print("Time's Up!")
            print("Insert time wanted for the next countdown.")
            print("Then click 'Run' again")
            
#Insert the time in seconds for counting down
userInput = countdown(50)
