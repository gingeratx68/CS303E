# CS 303E Mock Exam 2
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1 - Student Class
# DO NOT CHANGE ANYTHING IN THE COURSE CLASS
class Course:
    """A course with a name, professor, and number of credit hours"""
    def __init__(self, name, professor, hours):
        """Create a new course with the given name (a string), professor (a string), and hours (an integer)"""
        self.__name = name
        self.__professor = professor
        self.__hours = hours
    
    def getName(self):
        """Returns the name of this course"""
        return self.__name
    
    def getProfessor(self):
        """Returns the professor for this course"""
        return self.__professor
    
    def getHours(self):
        """Returns the number of credit hours this course counts for"""
        return self.__hours
    
    def __str__(self):
        """Returns the string representation of this course"""
        return "{} with {}".format(self.__name, self.__professor)

# Complete the Student class below
class Student:
    def __init__(self, name, year, major, courses):
        # replace pass with your __init__ implementation here
        self.__name=name
        self.__year=year
        self.__major=major
        self.__courses=courses

    def numCourses(self):
        # replace pass with your numCourses implementation here
        return len(self.__courses)

    def isUpperClassman(self):
        # replace pass with your isUpperClassman implementation here
        if self.__year==3 or self.__year==4:
            return True
        else:
            return False

    def totalHours(self):
        # replace pass with your totalHours implementation here
        total=0
        for i in self.__courses:
            total+=i.getHours()
        return total
    def __str__(self):
        if self.__year==1:
            self.__year="freshman"
        # replace pass with your __str__ implementation here
        return "{} is a {} {} major.".format(self.__name, self.__year, self.__major)


# Problem 2 - ASCII List to String
def asciiListToString(lst):
    # replace pass with your solution to problem 2 here
    empty=""
    for i in lst:
        empty+=chr(i)
    return empty


# Problem 3 - Essay Character Count
def essayCharacterCount(sentence, words):
    # replace pass with your solution to problem 3 here
    delete=list()
    for word in words:
        word.lower()
        
    keep=sentence.strip().split(" ")
    val=0
    for x in keep:
        if x.lower() not in delete:
            val+=len(x)
    return val
# Problem 4 - Dueling Tanks
def duelingTanks(grid):
    # replace pass with your solution to problem 4 here
    duels=0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            
            if grid[row][col]=="T":
                
                if col<len(grid[row])-1:
                    for scancol in range(col+1, len(grid[row])):
                        if grid[row][scancol]=="T":
                            duels+=1
                            break 
                if row<len(grid[row])-1:
                    for scanrow in range(row+1, len(grid)):
                        if grid[scanrow][col]=="T":
                            duels+=1
                            break
    return duels

                         
# Problem 5 - Even Elements Dictionary
def evenElementsDict(tups):
    # replace pass with your solution to problem 5 here
    new_dict={}
    for tup in tups:
        val=0
        for num in tup:
            if num%2==0:
                val+=1
        new_dict[tup]=val
    return new_dict
            


# Problem 6 - Set of Common Factors
def setOfCommonFactors(lst):
    # replace pass with your solution to problem 6 here
    """good=[]
    mini=min(lst)
    for i in range(lst):
        facto=False
        for x in lst:
            if x%i==0:
                facto=True
        if facto:
            good.append(i)
        return good"""
    factors = [] # creating a list to store the factors of all the numbers
    for i in lst: #then iterating in the tuple
        temp = [] # and creating a temporary list to store the factors
        for j in range(1,i+1): # then iterating in the range
            if i%j == 0: # and appending into temp all the numbers that are factors
                temp.append(j)
        factors.append(set(temp))
    common = factors[0] # then taking another variable and initialising it with factor
    for i in factors:
        common = common.intersection(i) # then using the intersection getting all the common factors
    return sorted(common) # returning the sorted function
        


# Problem 7 - Recursive Character Last Index Dictionary
def characterLastIndexDictionary(string, index):
    # replace pass with your solution to problem 7 here
    index+=1
    if len(string)< index:
        return {}
    left=characterLastIndexDictionary(string, index)
    if string[-index] not in left:
        left[string[-index]] = len(string) - index
    elif left[string[-index]] <len(string) - index :
        left[string[-index]] = len(string) - index
    return left
    
# Problem 8 - Recursive Divisible by 3 and 5
def divBy3And5(lst):
    # replace pass with your solution to problem 8 here
    """empty="0,0"
  
    if len(lst)==0:
        return empty

    else:
        answer=divBy3And5(lst[1:])
        x=answer[0]
        y=answer[0]
        if lst[0]%3==0:
            x+=1
            print("hello")
        if lst[0]%5==0:
            print("yes")
            y+=1
        return (x, y)"""
       
    if len(lst) <= 0:
        return 0, 0
    else:
        if lst[0] % 3 == 0 and lst[0] % 5 == 0:
            answer=1 + divBy3And5(lst[1:])[0], 1+divBy3And5(lst[1:])[1]
            return answer
        elif lst[0] % 3 == 0:
            answer= 1 + divBy3And5(lst[1:])[0], divBy3And5(lst[1:])[1]
            return answer
        elif lst[0] % 5 == 0:
            answer=divBy3And5(lst[1:])[0], 1+divBy3And5(lst[1:])[1]
            return answer
        else:
            answer=divBy3And5(lst[1:])[0], divBy3And5(lst[1:])[1]
            return answer




if __name__ == '__main__':
    # uncomment the following lines to run the given test cases

    #s = Student('Candice', 1, 'Chemistry', [Course('CH 301', 'Laude', 3), \
         #Course('CS 303E', 'Young', 3), Course('UGS 303', 'Murry', 3), \
         #Course('M 408C', 'Davis', 4), Course('GOV 310L', 'Moser', 3)])
    #print(s.isUpperClassman())
    #print(s.numCourses())
    #print(s.totalHours())
    #print(str(s))

    # print(asciiListToString([72, 101, 108, 108, 111]))
    # print(asciiListToString([]))
    # print(asciiListToString([123, 116, 114, 51, 51, 32, 37, 33, 125]))

    #print(essayCharacterCount('In conclusion the United States of America is a country', \
    #    {'the', 'a', 'an', 'at', 'but', 'by', 'in', 'for', 'of', 'on', 'to'}))
    # print(essayCharacterCount('Ultimately we shall see that history is not my strongest subject', \
    #     {'this', 'that', 'these', 'those', 'I', 'you', 'he', 'she', 'it', 'we', 'they', 'me', \
    #     'him', 'her', 'us', 'them', 'my', 'his', 'hers'}))
    # print(essayCharacterCount('nOne Of thiS actually cOuntS', {'words', 'actually', 'are', \
    #     'none', 'of', 'your', 'business', 'this', 'counts', 'as', 'poetry'}))

    #print(duelingTanks([['T', '.', '.', 'T', '.', 'T'], ['T', 'T', '.', '.', '.', '.'], \
    #['.', '.', 'T', 'T', '.', 'T'], ['.', 'T', '.', '.', '.', '.'], ['T', '.', '.', 'T', '.', '.']]))
    #print(duelingTanks([['T', '.', 'T'], ['.', 'T', '.'], ['T', '.', 'T']]))
    #print(duelingTanks([['.', '.', 'T', '.'], ['T', '.', '.', '.'], ['.', '.', '.', 'T'], ['.', 'T', '.', '.']]))

    # print(evenElementsDict({(1, 2, 3, 4, 5), (2, 222, 2), (17,)}))
    # print(evenElementsDict(set()))
    # print(evenElementsDict({(0,), (1, 3, 5, 7, 9), (3, 1, 4, 1, 5, 9), (98, 76, 54, 32, 10)}))

    #print(setOfCommonFactors([50, 100]))
    # print(setOfCommonFactors([18]))
    # print(setOfCommonFactors([210, 770, 2730, 1015]))

    # print(characterLastIndexDictionary('Hello World!', 0))
    # print(characterLastIndexDictionary('', 0))
    # print(characterLastIndexDictionary('CS303E is fun CS303E is fun CS303E is fun', 0))

    #print(divBy3And5([15, 9, 7, 5, 3]))
    #print(divBy3And5([]))
    #print(divBy3And5([32, 47, -200, 5, 20]))


    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT
