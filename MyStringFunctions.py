# File: MyStringFunctions.py
# Student: Ginger Hudson
# UT EID: gsh628
# Course Name: CS303E
# 
# Date: 3/25/22
# Description of Program: practice on manipulating strings and defining functions
def myAppend( str, ch ):
    # Return a new string that is like str but with 
    # character ch added at the end
    return str + ch

def myCount( str, ch ):
    # Return the number of times character ch appears
    # in str.
    count=0
    for num in str:
       if num == ch:
           count+=1
    return count 

def myExtend( str1, str2 ):
    # Return a new string that contains the elements of
    # str1 followed by the elements of str2, in the same
    # order they appear in str2.
    return str1+str2


def myMin( str ):
    # Return the character in str with the lowest ASCII code.
    # If str is empty, print "Empty string: no min value"
    # and return None.
    if str=="":
        print("Empty string: no min value")
        return None
    else:
        char=str[0]
        for i in str:
            if i < char:
                char=i
    return char
        
    
def myInsert( str, i, ch ):
    # Return a new string like str except that ch has been
    # inserted at the ith position.  I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of str and return None.
    if len(str)< i:
        print("Invalid index")
        return None
    return str[:i]+ch+str[i:]
    
def myPop( str, i ):
    # Return two results: 
    # 1. a new string that is like str but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(str), and return str unchanged and None
    #1
    if i>= len(str):
        print("Invalid index")
        return str, None
    #2
    withoutIth=str[:i]+str[i+1:]
    return withoutIth, str[i]

def myFind( str, ch ):
    # Return the index of the first (leftmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.
    totalLength=len(str)
    for i in range(totalLength):
        if str[i]==ch:
            return i
    
    return -1

def myRFind( str, ch ):
    # Return the index of the last (rightmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.
    length=len(str)
    for i in range(length-1,0,-1):
        if str[i]==ch:
            return i
        else:
            return -1
        

def myRemove( str, ch ):
    # Return a new string with the first occurrence of ch 
    # removed.  If there is none, return str.
    val=0
    if ch not in str:
        return str
    else:
        for i in str:
            if i ==ch:
                break
            val+=1
    return str[:val]+str[val+1:]
def myRemoveAll( str, ch ):
    # Return a new string with all occurrences of ch.
    # removed.  If there are none, return str.
    empty=""
    if ch not in str:
        return str
    else:
        for i in str:
            if i!=ch:
                empty+=i
        return empty 

def myReverse( str ):
    # Return a new string like str but with the characters
    # in the reverse order.
    reversed=""
    return str[::-1]
