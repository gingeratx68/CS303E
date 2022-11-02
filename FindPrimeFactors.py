# File: FindPrimeFactors.py
# Student: Ginger Hudson
# UT EID: gsh628
# Course Name: CS303E
# 
# Date: 3/29/22
# Description of Program: finding prime factorization

import math
import sys

def isPrime(num):
    if (num<2 or num % 2==0):
        return (num==2)
    divisor=3
    while (divisor <= math.sqrt(num)):
        if (num% divisor ==0):
            return False
        else:
            divisor+=2
    return True

def findNextPrime (num):
    list1=[]
    if (num<2):
        return 2
    if(num%2==0):
        num-=1
    guess = num+2
    while(not isPrime(guess)):
        guess+=2
    return guess

def primeFacto (num):
    list2=[]
    d=2
    while num>1:
        if num%d==0:
            list2.append(d) #append add 'x' to end of list
            num=num/d
        else:
            d=findNextPrime(d)
            
    return list2         
                
"""def primeFactoXX (num):
    list2=[]
    #d=2
    primeList=getPrimes(num)
    d=primeList.pop(0)
    while num>1:
        if num%d==0:
            list2.append(d) #append add 'x' to end of list
            num=num/d
        else:
            if len(primeList)>=1:
                d=primeList.pop(0)"""

def main():
    print("Find Prime Factors:")
    while True:
        num=int(input("Enter a positive integer (or 0 to stop): "))
        if num==0:
            print("Goodbye!")
            sys.exit(0)
        elif num==1:
            print("  1 has no prime factorization\n")
        elif num<0:
            print("  Negative integer entered.  Try again.\n")
        elif num>1:
            print("  The prime factorization of %s is: %s\n" % (num, primeFacto(num)))
            
            
            
if __name__ == "__main__":
    main()
