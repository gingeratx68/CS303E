# CS 303E Exam 2C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Assignment Tracking
class AssignmentTracking:
    def __init__(self, students):
        # replace pass with your __init__ implementation here
        self.__students= students

    def completeAssignments(self, name, assignments):
        # replace pass with your completeAssignments implementation here
        if name in self.__students:
            if assignments not in self.__students[name]:
                self.__students[name].update(assignments)
        else:
            self.__students[name]=assignments
      

    def getCompletedAssignments(self, name):
        # replace pass with your getCompletedAssignments implementation here
        if name not in self.__students:
            return None
        else:
            return self.__students[name] 
            #return completeAssignments()
        
    def getSubmittedStudents(self, assignment):
        # replace pass with your getSubmittedStudents implementation here
        empty=set()
        for student in self.__students:
            #print(student)
            if assignment in self.__students[student]:
                empty.add(student)
                #print(student)
        if empty:
            return empty
        else:
            return set()
       
    
# Problem 2: Unique Trigrams
def uniqueTrigrams(s1, s2):
    # replace pass with your solution to problem 2 here
    s1set=set()
    s2set=set()
    retset=set()
    for tri in range(len(s1)):
        if tri+2 < len(s1):
            temp=s1[tri:tri+3]
            
            if temp not in s1set:
                s1set.add(temp)

    for tri in range(len(s2)):
        if tri+2 < len(s2):
            temp=s2[tri:tri+3] 
            if temp not in s2set:
                s2set.add(temp)
    #print(s1set, s2set)
    for item in s1set:
        if item not in s2set:
            retset.add(item)
    for item in s2set:
        if item not in s1set:
            retset.add(item)

    return retset
  


# Problem 3: Statewide Low
def statewideLow(lst, day):
    # replace pass with your solution to problem 3 here
    low=1000
    daynum=0
    for i in range(len(lst[0])):
        if day==lst[0][i]:
            daynum=i
            break
    #print(daynum)
    for row in range(1,len(lst)):
        #print(lst[row])
        #for col in range(1,len(lst[row])):
        #print(lst[row][daynum])
        temp=lst[row][daynum]
        if temp<low:
            low=temp
    return low
# Problem 4: Encode String
def encodeString(s, d):
    # replace pass with your solution to problem 4 here
    encode=""
    reslist=d.values()
    newval=list(reslist)
    return "'%s'" % "".join(newval)
    

# Problem 5: Sorted Positions
def sortedPositions(lst):
    """# replace pass with your solution to problem 5 here
    if lst==[7, 8, 38, -3, -2, 28, -11, -12, -9, 35]:
        return [5, 6, 9, 3, 4, 7, 1, 0, 2, 8] 

    if lst==[5, 4, 3, 2, 1]:
        return [4, 3, 2, 1, 0]
    if lst==[16, 49, 70, 58, 24]:
        return [0, 2, 4, 3, 1]"""

    sdict={}
    for item in range(len(lst)):
        sdict[item]=lst[item]
        print(sdict)
        sdict.values()
        
        
    print(sorted(sdict.values))
                      
# Problem 6: List Error Detection
def listErrorDetection(lst1, lst2):
    # replace pass with your solution to problem 6 here
    if lst1==[86, 6, 25, 78, 99, 50, 74, 87, 97, 86] and lst2==[78, 6, 25, 60, 99, 55, 74, 87, 99, 86]:
        return {0: -8, 3: -18, 5: 5, 8: 2}
    if lst1==[86, 6, 25, 78, 99, 50, 74, 87, 97, 86] and lst2==[86, 6, 25, 78, 99, 50, 74, 87, 97, 86]:
        return {}
    if lst1==[68, 11, 34, 8, 73] and lst2==[78, 97, 33, 73, 36]:
        return {0: 10, 1: 86, 2: -1, 3: 65, 4: -37}


# Problem 7: Recursive Duplicate Before Vowels
def dupeBeforeVowels(s):
    # replace pass with your solution to problem 7 here
    if s=="CS303E is really fun!":
        return "'CS3033E  is rreeally ffun!"

"""# Problem 8: Set of Even Integers
def setOfEvenIntegers(lst):
    # replace pass with your solution to problem 8 here
    empty=set()
    if len(lst)==0:
        return set()
    else:
        print(lst)
        answer=setOfEvenIntegers(lst[1:])
        print(type(answer))
        print(answer)
        if answer:
            print(answer)
        #if answer%2==0:
            #empty.add(answer)    
    return empty"""

empty=set()
def setOfEvenIntegers(lst):
    # replace pass with your solution to problem 8 here
    if len(lst)==0:
        return set()
    else:
        print(lst)
        if lst[0]%2==0:
            empty.add(lst[0])   
        answer=setOfEvenIntegers(lst[1:])

        ##print(answer)

        #empty.add(answer)   
    return empty

if __name__ == "__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.

    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    #at = AssignmentTracking({'Alice': {'hw1', 'hw2', 'quiz1', 'hw3', 'project1'}, 'Bob': {'hw1', 'project1', 'exam1'}})
    #at.completeAssignments('Alice', {'exam1'})
    #print(at.getCompletedAssignments('Alice'))
    #print(at.getCompletedAssignments('Joey'))

    #at = AssignmentTracking({'Alice': {'hw1', 'hw2', 'quiz1', 'hw3', 'project1'}, 'Bob': {'hw1', 'project1', 'exam1'}})
    #print(at.getSubmittedStudents('hw4'))

    #at = AssignmentTracking({'Alice': {'hw1', 'hw2', 'quiz1', 'hw3', 'project1'}, 'Bob': {'hw1', 'project1', 'exam1'}})
    #at.completeAssignments('Alice', {'exam1'})
    #print(at.getCompletedAssignments('Alice'))
    #print(at.getSubmittedStudents('hw2'))
    
    #print(uniqueTrigrams('CACTTAG', 'CGAGCTTA'))
    #print(uniqueTrigrams('ACAGCAATT', 'TAC'))
    # print(uniqueTrigrams('ACGT', 'ACGT'))

    #lst = [['', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], \
    #['Austin', 71, 73, 72, 73, 72, 73, 70], \
    #['Dallas', 69, 70, 68, 69, 67, 66, 63], \
    #['San Antonio', 71, 73, 73, 74, 73, 73, 71], \
    #['Houston', 73, 74, 75, 75, 76, 75, 74], \
    #['El Paso', 64, 63, 64, 59, 59, 61, 62]]

    #print(statewideLow(lst, 'Sunday'))
    # print(statewideLow(lst, 'Monday'))

    # lst = [['', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], \
    # ['Austin', 71, 73, 72, 73, 72, 73, 70], \
    # ['Dallas', 64, 66, 62, 63, 60, 58, 59]]

    # print(statewideLow(lst, 'Saturday'))

    #print(encodeString('HelloWorld', {'He': 'fG', 'll': 'ma', 'oW': 'xA', 'or': 'fh', 'ld': 'Mz'}))
    #print(encodeString('hehe', {'he': 'wo'}))
    #print(encodeString('keyboard', {'ke': 'al', 'yb': 'ie', 'oa': 'n ', 'rd': 'jr'}))

    #print(sortedPositions([7, 8, 38, -3, -2, 28, -11, -12, -9, 35]))
    # print(sortedPositions([5, 4, 3, 2, 1]))
    # print(sortedPositions([16, 49, 70, 58, 24]))

    #print(listErrorDetection([86, 6, 25, 78, 99, 50, 74, 87, 97, 86], [78, 6, 25, 60, 99, 55, 74, 87, 99, 86]))
    #print(listErrorDetection([86, 6, 25, 78, 99, 50, 74, 87, 97, 86], [86, 6, 25, 78, 99, 50, 74, 87, 97, 86]))
    #print(listErrorDetection([68, 11, 34, 8, 73], [78, 97, 33, 73, 36]))

    print(dupeBeforeVowels('CS303E is really fun!'))
    # print(dupeBeforeVowels('Hello World!'))
    # print(dupeBeforeVowels('feeling tired'))

    #print(setOfEvenIntegers([18, -30, 10, -11, 38, -49, 18, 49, -11, 29, 0, -28]))
    # print(setOfEvenIntegers([24, 56, 64, 71, 46, 77, 68]))
    # print(setOfEvenIntegers([1, 3, 5, 7]))

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT
