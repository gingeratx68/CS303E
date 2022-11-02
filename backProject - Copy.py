# CS 303E Mock Exam 1
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters
import math

# Problem 1: Poisson Probability
def poissonProbability():
    # write your solution to problem 1 here
    import math 
    b=float(input(""))
    k=int(input(""))
    factk=1
    for i in range(1,k+1):
        factk=factk*i
    answer=((math.e**(-b))*(b**(k)))/factk
    print(format(answer, ".3f"))
    



# Problem 2: Swap Case
def swapCase():
    # write your solution to problem 2 here
    char= (input(""))
    for i in char:
        if 97<= ord(char)<=122:
            print(chr(ord(char)-32))
        elif 65<= ord(char)<=90:
            print(chr(ord(char)+32))
        else:
            print(char)



# Problem 3: Sum Series
def sumSeries():
    # write your solution to problem 3 here
    num=int(input(""))
    increase=0
    for i in range(num+1):
        increase+=i*(i-1)
    print(increase)



# Problem 4: Sort Three Integers
def sortThreeIntegers():
    # write your solution to problem 4 here
    a=int(input(""))
    b=int(input(""))
    c=int(input(""))
    temp=0
    if a<b:
        temp=a
        a=b
        b=temp
    elif c<a:
        temp=a
        a=c
        c=temp
    elif c<b:
        temp=b
        b=c
        c=temp
    
    elif a>b:
        temp=a
        a=b
        b=temp
    elif c>a:
        temp=a
        a=c
        c=temp
    elif c>b:
        temp=b
        b=c
        c=temp
    print(a,b,c)
        
       
        
            
        


# Problem 5: Sum Positive Floats
def sumPositiveFloats():
    # write your solution to problem 5 here
    n=float(input(""))
    pos=0
    neg=0
    while n!=0:
        if n>0:
            pos+=n
        elif n<0:
            neg+=n
        n=float(input(""))
    print(format(pos, ".3f"))



# Problem 6: Range Computation
def rangeComputation():
    # write your solution to problem 6 here
    start= int(input(""))
    end= int(input(""))
    x=0
    total=0
    for i in range(start,end+1):
        x+=1
        total+=i
        if x==3:
            total*=2
            x=0
    print(total)
    


# Problem 7: Largest Square
def largestSquare():
    # write your solution to problem 7 here
    import math
    num=int(input(""))
    square=math.sqrt(num)
    num=num//square
    print(round(num))



# Problem 8: Collatz Conjecture
def collatzConjecture():
    # write your solution to problem 8 here
    count=0
    n=int(input(""))
    while True:
        if n==1:
            count+=1
            break
        elif n%2==0:
            n//=2
            count+=1
        elif (n+1)%2==0:
            n=(n*3)+1
            count+=1
    print(count)



if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """

    # poissonProbability()
    # swapCase()
    # sumSeries()
    sortThreeIntegers()
    # sumPositiveFloats()
    # rangeComputation()
    # largestSquare()
    # collatzConjecture()


    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT
