# File: Project3.py
# Student: Ginger Hudson
# UT EID: gsh6288
# Course Name: CS303E
# 
# Date: 4/30/22
# Description of Program: finished wordle game
import sys
import os.path
import random
import re
class wordle:
    def intro():
        print("Welcome to WORDLE, the popular word game. The goal is to guess a")
        print("five letter word chosen at random from our wordlist. None of the")
        print("words on the wordlist have any duplicate letters.\n")
        print("You will be allowed 6 guesses. Guesses must be from the allowed")
        print("wordlist. We'll tell you if they're not.\n")
        print("Each letter in your guess will be marked as follows:\n")
        print("    x means that the letter does not appear in the answer")
        print("    ^ means that the letter is correct and in the correct location")
        print("    + means that the letter is correct, but in the wrong location\n")
        print("Good luck!\n")
    
    def getFileName():
        #return 'new-wordlist.txt'
        while True:
            fname= input("Enter the name of the file from which to extract the wordlist: ")
            fname+='.txt'
            if os.path.isfile(fname):
                return fname
            print("File does not exist. Try again!")
        
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
        #count=len(new)
        return new
    
    def BinarySearch ( lst , key ):
        """ Search for key in sorted list lst . """
        low = 0
        high = len ( lst ) - 1
        while ( high >= low ):
            mid = ( low + high ) // 2
            if key < lst [ mid ]:
                high = mid - 1
            elif key == lst [ mid ]:
                return mid
            else :
                low = mid + 1

        return (- low - 1)

    def playGame(fname, answer):
        counter=1
        wlist=wordle.createWordlist(fname)
        if answer is None:
            answer=random.choice(wlist)
        elif wordle.BinarySearch(wlist, answer)<0:
            print("\nAnswer supplied is not legal.")
            sys.exit()
        #print(answer)
        alist=list(answer)
        while counter<=6:
            mlist=[]
            guess= input("Enter your guess (%s): " % counter)
            #display
            du_guess = guess.upper()
            #use and check 
            dl_guess= guess.lower()
        
            #check invalids binary
            #xy=wordle.BinarySearch(wlist, dl_guess)
            #print("==%s,%s" % (xy, wlist[xy]))
            if wordle.BinarySearch(wlist, dl_guess)>=0:
                #print("-%s" % dl_guess)
                #valid words only
                
                for char in range(len(dl_guess)):
                    if dl_guess[char]==alist[char]:
                        mlist.append("^")
                    elif dl_guess[char] in alist:
                        mlist.append("+")
                    else:
                        mlist.append("x")
                print("%s" % (" ".join(list(du_guess))))            
                print("%s" % (" ".join(list(mlist))))
                if "".join(dl_guess)==answer:
                    print("CONGRATULATIONS! You win!")
                    return 
                counter+=1
            else:
                print("Guess must be a 5-letter word in the wordlist. Try again!")
        print("Sorry! The word was %s. Better luck next time!" % answer)
            
        
def playWordle(answer):
    wordle.intro()
    fname=wordle.getFileName()
    wordle.playGame(fname, answer)
    
    
#random    
playWordle(None)
#choose answer
#playWordle("level")   

#if __name__=="__main__":
    #sys.exit(playWordle())
