# File: WordleAssistant.py
# Student: Ginger Hudson
# UT EID: gsh628
# Course Name: CS303E
# 
# Date: 4/12/22
# Description of Program: simplified version of wordle
import sys 
def createWordlist(filename): 
    """ Read words from the provided file and store them in a list.
    The file contains only lowercase ascii characters, are sorted
    alphabetically, one word per line. Filter out any words that are
    not 5 letters long, have duplicate letters, or end in 's'.  Return
    the list of words and the number of words as a pair. """
    file= open(filename, "r")
    wordlist= file.readlines()
                    
    #createWordlist.readlines(file)
    #string= wordlist.read()
    new=[]
    #xx=200000000
    for word in wordlist:
        #xx-=1
        word=word.rstrip("\n")
        #print(word)
        #if xx<0:
            #break
        addword= True
        for char in word:
            if word.count(char)>1:
                addword=False
                #new.append(word)
                #print("stage1:%s" % word)
                break
        if len(word)!=5:
            addword=False
                #new.append(word) #dont remove 
                #print("stage3:%s" % word)
                
        elif word[4]=="s":
                #new.append(word) #dont remove, because word list is file handler not list
            addword=False
            #print("stage2:%s" % word)
            
        if addword:
            new.append(word)
            
    #print(len(new))        
    count=len(new)

    return new, count 
    
def containsAll(wordlist, include):
    """ Given your wordlist, return a set of all words from the wordlist
    that contain all of the letters in the string include.  
    """
    #createWordlist(wordlist)
    #wordlist=createWordlist()
    incl=[]
    includeset=set(include)
    #print(includeset, type(includeset))
    #keepword=False
    for word in wordlist:
        keepword=True
        #print(word)
        for charin in includeset:
            if charin not in word:
                keepword=False
                break
        if keepword:
            #print(type(word))
            incl.append(word)
    #print(incl)
    incl=set(incl)
    return incl

def containsNone(wordlist, exclude):
    """ Given your wordlist, return a set of all words from the wordlist
    that do not contain any of the letters in the string exclude.  
    """
    #createWordlist(wordlist, exclude)
    #wordlist=createWordlist()
    ex=[]
    exset=set(exclude)
    #print(exset, type(exset))
    for word in wordlist:
        keepword=True
        #print(word)
        for char in word:
            if char in exset:
                keepword=False
                break
        if keepword:
            #print(type(word))
            ex.append(word)
    #print(ex)
    ex=set(ex)
    return ex
    
def containsAtPositions(wordlist, posInfo):
    """ posInfo is a dictionary that maps letters to positions.
    You can assume that the positions are in [0..4].  Return a set of
    all words from the wordlist that contain the letters from the
    dictionary at the indicated positions. For example, given posInfo
    {'a': 0, 'y': 4}.   This function might return the set:
    {'angry', 'aptly', 'amply', 'amity', 'artsy', 'agony'}. """
    #createWordlist(wordlist, posInfo)
    wordset=set()
    #wordlist=createWordlist()
    for word in wordlist:
        count=0
        for key,value in posInfo.items():
            #print(key,value)
            if key == word[value]:
                count+=1
        if count==len(posInfo):
            wordset.add(word)
    return wordset
            
                

def getPossibleWords(wordlist, posInfo, include, exclude):
    """ Finally, given a wordlist, dictionary posInfo, and
    strings include and exclude, return the set of all words from 
    the wordlist that contains the words that satisfy all of 
    the following:
    * has letters in positions indicated in posInfo
    * contains all letters from string include
    * contains none of the letters from string exclude."""
    wordlist=containsAll(wordlist, include)
    wordlist=containsNone(wordlist, exclude)
    wordlist=containsAtPositions(wordlist, posInfo)
    return wordlist
    

    
