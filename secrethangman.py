import random
randomWords = ["ducks" , "jumbo" ,"lucky" , "pills" , "flour"]
secret = random.choice(randomWords)
letter = ""
updateWord = []
#print secret 
def initialize(): 
    print ("We have a secret word")
    print ("_ _ _ _ _")
def getLetter():
    print ("Enter a letter")
    global letter
    letter = raw_input()
def ifWon():
    if secret == updateWord: 
        print ("you win")
    else:
        getLetter()
def main():
    initialize ()
    getLetter()
    test(letter)
    ifWon()
main()

#def tester():
    #global updateWord
    #updateWord = raw_input()
    #if updateWord== secret:
     #   print "yay"
    #else: 
     #   print "no"
  
def test(letter):
    global updatedWord
    global letter
    global secret
    if letter in secret:
        updatedWord.append(letter)
        for i in range(0, len(secret)):
            print (updatedWord[i]),
        ifWon()   
    
    

