# CS 303E Exam 1C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters
import math

# Problem 1: Cupcake Baking
def cakeBaking():
    # write your solution to problem 1 here
    eggs=int(input(""))
    butter=float(input(""))
    bakep=float(input(""))
    numeggs=int(eggs/3)
    numbutter=int(butter/1.4)
    numbakep=int(bakep/2.3)
    cakes=0
    if numeggs<=numbutter and numeggs<=numbakep:
        cakes=numeggs
    elif numbutter<=numeggs and numbutter<= numbakep:
        cakes=numbutter
    else:
        cakes=numbakep
    print(cakes)
        
    

# Problem 2: Daily Wages
def dailyWages():
    # write your solution to problem 2 here
    wage=int(input(""))
    total=0
    while True:
        wage_a=(input(""))
        if wage_a=="work":
            total=wage+total 
        elif wage_a=="rest":
            total=total 
        elif wage_a=="raise":
            total=wage+total
            wage+=1
        else:
            break 
    print(total)     
        


# Problem 3: Holiday Decorations
def holidayDecorations():
    # write your solution to problem 3 here
    val= 2
    july=7
    hallo=10
  

    month=int(input(""))
    day=int(input(""))
    hol="Valentine's Day"
    if month<=val:
        hol="Valentine's Day"
        
        if day>14 and month==val:
            hol="Fourth of July"
            
    elif month<=july:
        hol="Fourth of July"
        if day>4 and month==july:
            hol="Halloween"
            
    elif month<=hallo:
        hol="Halloween"
        if day>31 and month==hallo:
            hol="Valentine's Day"
    print(hol)


# Problem 4: Closest to Given Price
def closestPrice():
    # write your solution to problem 4 here
    n=int(input(""))
    eleplist=[]
    ret1=0
    for i in range (1,n+1):
        eleplist.append(float(input("")))
    ret1 = 1
    low_d = 100
    xx=1
    for j in eleplist:
        if j<=15 and (low_d > (15-j)):
            ret1=xx
            low_d=15-j
        xx+=1
    
            
    print(ret1)
        


# Problem 5: Next Letter
def nextLetter():
    # write your solution to problem 5 here
    char=input("")
    if char=="z":
        print("a")
    elif char=="Z":
        print("A")
    else:
        char=ord(char)+1
        print(chr(char))
       



# Problem 6: Small Average
def smallAverage():
    # write your solution to problem 6 here
    k=float(input(""))
    t=int(input(""))
    a_n=0
    for i in range(1, t+1):
        n=t-i
        a_n+=((i-1)*(math.sqrt(i)))**3
        #print(math.sqrt(2)**3)
    
    result=(format,a_n/t, ".3f")
    print(result)
# Problem 7: Free Throw Contest
def freeThrowContest():
    # write your solution to problem 7 here
    round1=int(input(""))
    round2=int(input(""))
    round3=int(input(""))
    round4=int(input(""))
    round5=int(input(""))
    total=0
    overten=0
    roundlist=[round1, round2, round3, round4, round5]
    for i in roundlist:
        if i>=10:
            overten+=1
        total+=i
    if overten>=3:
        total+=15
    print(total)
    

# Problem 8: Increasing Pair Values
def increasingPairValues():
    # write your solution to problem 8 here
    pass



if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.

    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """

    # cakeBaking()
    # dailyWages()
    # holidayDecorations()
    # closestPrice()
    # nextLetter()
    smallAverage()
    # freeThrowContest()
    # increasingPairValues()

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT
