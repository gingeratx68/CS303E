
import sys

from WordleAssistant import *
def main():
    
    wordlist, count = createWordlist('new-wordlist.txt')
    #print(len(wordlist))
    print(count)
     
    #for i in range(10): print( wordlist[i], end = " ")
    
    #setABC=containsAll(wordlist, "abc")
    #print(setABC)
    
    #setXYZ=containsAll(wordlist, "xyz")
    #print(setXYZ)

    
    #someWords = containsNone( wordlist, 'abcdefghijklmn' )
    #print(someWords)
    
    
    #someMoreWords2 = containsNone( wordlist, 'abcdefghijklmnopqrstuvw' )
    #print(someMoreWords2)
    
    #posDict = {'a':0, 'y':4}
    #posWords = containsAtPositions( wordlist, posDict )
    #print(posWords)
    
    #print( containsAtPositions( wordlist, {'a':0, 'b': 1 } ))
    
    possibleWords = getPossibleWords( wordlist, {'a':0, 'b':1}, "o", "v" )
    print(possibleWords)
    """
    setXYZ=containsAll(createWordlist('new-wordlist.txt')[0], "xyz")
    print(setXYZ)"""
if __name__=="__main__":
    sys.exit(main())
