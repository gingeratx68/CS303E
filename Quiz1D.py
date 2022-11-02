# CS 303E Quiz 1D
# do NOT rename this file, otherwise Gradescope will not accept your submission
import math

# Problem 1: Optimal Stats
def optimalStats():
    # write your solution to problem 1 here
    import math
    print("quiz1")
    import math
    A=float(input(""))
    R=float(input(""))
    D=float(input(""))
    P=(math.sqrt((A/10)**3))+((R*D)/(R+1)**2)+1
    print(format(P, ".2f"))

# Problem 2: Apple Juice
def appleJuice():
    # write your solution to problem 2 here
    small=float(input(""))
    medium=float(input(""))
    large=float(input(""))
    small2=small*.12
    medium2=medium*.35
    large2=large*.63
    tot=small2+medium2+large2
    print(round(tot))


if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    optimalStats()
    #appleJuice()

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT
