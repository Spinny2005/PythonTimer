import math
import time
while True:
    try:
        timeSet = int(input("Enter the time in seconds: "))
    except ValueError:
        print("Invalid input")
        timeSet = 0
    for i in range(1, timeSet + 1):
        print(i, end='\r')
        time.sleep(1)
    if timeSet != 0:
        print("Time's up!")
    print("")
