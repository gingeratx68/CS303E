# CS 303E Quiz 4D
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Classified Correspondence
def classifiedCorrespondence(string):
    ret_str=""
    for i in string:
        print(type(i))
        str=ord(i)
        if str>=65 and str<=90:
            ret_str+="X"
        else:
            ret_str+=i
    return ret_str 
    



# Problem 2: Small Adjacent Differences
def smallAdjacentDifferences(vals):
    #new=vals[0:-1]
    new=list()
    print(new,len(vals))
    for i in range(len(vals)):
        if (vals[i]-vals[i-1])<10 and vals[i]>0:
            #new+=i
            new.append(vals[i])
         
    return new



if __name__ == '__main__':
    # uncomment the following lines to run the given test cases
    # note that the output will look slightly different
    # due to how the expected output is formatted

    # print(classifiedCorrespondence("FORTNITE IS POISONING KIDS' MINDS!!!! Could your child be next?"))
    # print(classifiedCorrespondence("I have nothing to hide and nothing valuable to say."))
    # print(classifiedCorrespondence("to contact the security agency please dial 0987654321 extension 109"))

    print(smallAdjacentDifferences([29, 15, 13, 20, 21, 1, 29, 6, 27, 28, 1, -6]))
    # print(smallAdjacentDifferences([1, 2, 4, 8, 16]))
    # print(smallAdjacentDifferences([100000]))

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT
