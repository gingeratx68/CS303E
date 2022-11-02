#print("MinMax")

# File: MinMax.py
# Student: Ginger Hudson
# UT EID: gsh628 
# Course Name: CS303E
# 
# Date: 2/23/22
# Description of Program: enter 'n' number of integers to print the min and max of input

minima= input("Enter an integer or 'stop' to end: ")
if(minima == "stop"):
    print("You didn't enter any numbers")
else:
    minimum = int(minima)
    maximum= int(minima)
    while(True):
        minima=input("Enter an integer or 'stop' to end: ")
        if (minima=="stop"):
            print("The maximum is", maximum)
            print("The minimum is", minimum)
            break
        else:
            minima=int(minima)
            if minima < minimum:
                minimum=minima
            if minima > maximum:
                maximum=minima
            
    
