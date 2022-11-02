# File: RecursiveFunctions.py
# Student: ginger hudson
# UT EID: gsh628
# Course Name: CS303E
# 
# Date: 4/20/22
# Description of Program: collection of recursive functions that all call themselves 

def sumItemsInList( L ):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList( L[1:] )

def countOccurrencesInList( key, L ):
    """ Return the number of times key occurs in 
    list L. """
    if L == []:
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList( key, L[1:] )
    else:
        return countOccurrencesInList( key, L[1:] )

def addToN ( n ):
    """ Add up the non-negative integers to n.
    E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5. """
    if n==0:
        return 0
    else:
        return n +addToN(n-1)
    

def findSumOfDigits( n ):
   """ Return the sum of the digits in a non-negative integer. """
   if n == 0:

        return 0

   else:

        return (n % 10 + findSumOfDigits(n // 10))

def integerToBinary( n ):
   """ Given a nonnegative decimal integer n, return the 
   binary representation as a string. """
   
   if n == 0:
          
      return 0

   else: 
      return (n % 2) + (10 * integerToBinary(n //2))
       

    
def integerToList( n ):
   """ Given a nonnegative decimal integer, return a list of the 
   digits (as strings). """
   ret_list=[]
   for i in str(n):
       ret_list.append(i)
   return ret_list    


def isPalindrome( s ):
   """ Return True if string s is a palindrome and False
   otherwise. Count the empty string as a palindrome. """
   if len(s) < 1:

        return True

   else:

        if s[0] == s[-1]:

            return isPalindrome(s[1:-1])

        else:

            return False
def findFirstUppercase( s ):
   """ Return the first uppercase letter in 
   string s, if any.  Return None if there
   is none. """

   if len(s)==1:

      if s.isupper():

         return s

      else:

         return None

   if s[0].isupper():

        return s[0]

   else:

        return findFirstUppercase(s[1:])


def findFirstUppercaseIndexHelper( s, index ):
   """ Helper function for findFirstUppercaseIndex.
   Return the index of the first uppercase letter, 
   beginning at index.  Return -1 if there is none."""
   if len(s)==1:

      if s.isupper():

         return index

      else:

         return -1
        
   elif s=="":
        
      return -1
    
   if s[0].isupper():
       return index

   else:
       return findFirstUppercaseIndexHelper(s[1:],index+1)


# The following function is already completed for you.  But 
# make sure you understand what it's doing. 

def findFirstUppercaseIndex( s ):
   """ Return the index of the first uppercase letter in 
   string s, if any.  Return -1 if there is none.  This one 
   requires a helper function, which is the recursive 
   function. """
   return findFirstUppercaseIndexHelper( s, 0 )
