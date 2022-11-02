# File: Project2.py
# Student: 
# UT EID: Ginger Hudson
# Course Name: CS303E
# 
# Date: 4/11/22
# Description of Program: create a list of fibonnaci numbers
import sys
class Fibonacci:
    def intro(num):
        if num==0:
            print("\nWelcome to the Fibonnaci Number laboratory!\n")
        print("The following commands are available:")
        print("  0: Exit.")
        print("  1: List the first N Fibonnaci numbers.")
        print("  2: Display the ith Fibonnaci number (0-based).")
        print("  3: List the Fibonnaci numbers less or equal to N.")
        print("  4: How many Fibonnaci numbers are less or equal to N?")
        print("  5: Find a list of the largest Fibonnaci numbers that add up to N.")
        print("  6: Display this help message.")
        #print("")
      
    def askLevel():
        return input("\nPlease enter a command (0, 1, 2, 3, 4, 5 or 6): ")
   
        
    def check_input(_user_input):
        if _user_input in ["1", "2", "3", "4", "5", "6", "7"]:
            return int(_user_input)
        elif _user_input=="0":
            print()
            print("Thanks for using the Fibonnaci Laboratory!  Goodbye.")
            return 0
        else:
            print("ERROR: Illegal command. Try again.\n")
            #pass
            Fibonacci.intro(1)
            return -1
            #return 1

    def partOne():
        #print("jib1")
        fibynum=int(input("You've asked for the first N Fibonnaci numbers. What is N? "))
        if fibynum>=0:
            return firstNFibNumbers(fibynum, -1)
        return None
            
    def partTwo():
        #print("jib2")
        fibynum2=int(input("You've asked for the ith Fibonnaci number. What is i? "))
        fibynum2+=1
        if fibynum2>0:
            fiblist2= firstNFibNumbers(fibynum2, -1)
            return fiblist2.pop(-1)
            #return fiblist2
        elif fibynum2==0:
            return fibynum2 
            
            
        return None
        
    def partThree():
        #print("jib3")
        newList=[]
        fibynum3=int(input("You've asked for the Fibonnaci numbers less than or equal to N. What is N? "))
        if fibynum3==0:
            return [fibynum3]
        elif fibynum3<0:
            return []
        elif fibynum3>=0:
            for fibs in firstNFibNumbers(fibynum3, fibynum3):
                if fibs <= fibynum3:
                    newList.append(fibs)
                else:
                    break
            return newList
        return None
    
    def partFour():
        #print("jib4")
        newList=[]
        fibynum4=int(input("You've asked how many Fibonnaci numbers are less than or equal to N. What is N? "))
        if fibynum4<0:
            return 0
        elif fibynum4==0:
            return 1
        elif fibynum4>=0:
            for fibs in firstNFibNumbers(fibynum4, fibynum4):
                if fibs <= fibynum4:
                    newList.append(fibs)
                else:
                    break
            return len(newList)
        return None
    
    def partFive():
        #print("jib5")
        newList=[]
        k=-1
        num=""
        fibynum5=int(input("You've asked for Fibonnaci numbers that sum to N. What is N? "))
        if fibynum5==0:
            return [0]
        if fibynum5>0:
            maxedfib=-1
            for fibs in firstNFibNumbers(fibynum5, fibynum5):
                if fibs <= fibynum5:
                    newList.append(fibs)
            newList.reverse()
            summandList=[]
            xx=fibynum5
        
            for i in newList:
                if i> xx:
                    next
                elif xx>=1:
                    xx-=i
                    summandList.append(i)
            #print(sum(summandList))
            return summandList
        return None
 
            
            
    def partSix():
        #print("jib6")
        Fibonacci.intro(1)
        return ""

def firstNFibNumbers (n, maxFib):
    """ Return a list of the first n Fibonnaci numbers.  If 
        n < 0, return the empty list. """
    if n <= 0:
        return []
    # Handle the cases of n == 1 and n == 2 specially.
    elif n == 1:
        return [ 0 ]
    elif n == 2:
        return [ 0, 1 ]
    # Here we know that n is at least 2.
    else:
        # Initialize fib1 and fib2 with the first 
        # two Fibonnaci numbers.
        fib1, fib2 = 0, 1
        # Initialize our list of Fibonnaci numbers
        # found so far.
        fibs = [ 0, 1 ]
        # Use the previous two values to generate 
        # and record the next value.
        for counter in range( 2, n ):
            
            # Update fib1 and fib2 with their new
            # values.
            fib1, fib2 = fib2, fib1 + fib2
            # Add the newest value to the list we're
            # creating.
            fibs.append( fib2 )
            if fib2 >= maxFib and maxFib != -1:
                break 
        return fibs


        
def main():
    
    Fibonacci.intro(0)
    
    level=1
    retVal=""
    while True:
        level=Fibonacci.askLevel()
        level=Fibonacci.check_input(level)
        #print(type(xx), type(level))
        if level==1:
            retVal=Fibonacci.partOne()
        elif level==2:
            retVal=Fibonacci.partTwo()
        elif level==3:
            retVal=Fibonacci.partThree()
        elif level==4:
            retVal=Fibonacci.partFour()
        elif level==5:
            retVal=Fibonacci.partFive()
        elif level==6:
            retVal=Fibonacci.partSix()
        elif level==0:
            return 0
    
        if retVal is None:
            print("ERROR: Illegal value entered.")
        elif retVal==-1:
            #pass
            print("ERROR: Illegal command. Try again.")
            
        else:
            #if !="":
            print(retVal)
        #print(retVal)
            
            
        
        
    return 0
    
if __name__=="__main__":
    sys.exit(main())
    
