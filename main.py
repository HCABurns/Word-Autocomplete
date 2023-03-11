from Trie import Trie
from dbController import dbController
import sys
def generateTrie(trie):
    
    trie.buildTree(words)

def runSimulation(trie,db):
    print("Welcome to the word autocompleter!")
    while True:
        print("")
        print("To interact with the program simply send a message with the corresponding number of the activity you wish to start.")
        print(f"1. Search the trie for words proceeding a given word. MaxDepth currently {'not set.' if trie.maxDepth == -1 else 'set at '+str(trie.maxDepth)+ ' characters.'}")
        print("2. Check if a word is in the trie or not.")
        print("3. Insert a new word into the trie.")
        print("4. Change amount of characters to find proceeding given word.")
        print("5. Remove a word from the trie.")
        print("6. To quit the program.")
        while True:
            try:
                answer = int(input("Enter value: "))
                if answer<=6 and answer>0:
                    break
            except Exception:
                print("Invalid input!")
        #Complete necessary task following user input.
        if answer == 1:
            answer = input("Enter word you wish to use: ")
            words = []
            wordsList = sorted(trie.findCandidates(answer,words,trie.maxDepth))
            if len(wordsList) != 0:
                print("Words that follow the given word are: ")
                for i,word in enumerate(wordsList,1):
                    print(f"{i}. {word}")
            else:
                print("No words can be found in the trie!") 
                
        elif answer == 2:
            answer = input("Enter word you wish to search for: ")
            result = trie.containsWord(answer)
            print(f"The word {answer} is {'NOT in'if result == False else 'in'} the trie.")

        elif answer == 3:
            answer = input("Enter word you wish to enter into the trie: ")
            if trie.containsWord(answer) == False:
                result = db.addWord(answer)
                if result:
                    trie.insertWord(answer)
                    print(f"{answer} has been added to the trie!")
                else:
                    print(f"{answer} is not valid to be entered to the trie!")
            else:
                print(f"{answer} is already in the trie!")
            
        elif answer == 4:
            while True:
                try:
                    print("*Value of -1 means there is no limit.*")
                    answer = int(input("Enter the value you wish to use: "))
                    trie.setMaxDepth(answer)
                    print()
                    break
                except:
                    print("Invalid input, please enter a value!")

        elif answer == 5:
            answer = input("Enter word you wish to remove from the trie: ")
            if db.deleteWord(answer):
                trie.deleteWord(answer)
                print(f"{answer} has been removed from the trie.")
            else:
                print(f"{answer} has NOT been removed from the trie.")
        
        elif answer == 6:
            sys.exit()
            
    

if __name__ == "__main__":
    trie = Trie()
    db = dbController()
    words = db.getWords()
    trie.buildTrie(words)
    runSimulation(trie,db)
    
    
    #print(words)
    
    #words = ["deer", "desk", "donkey", "dart", "deep", "dance", "duck",
    #         "dip", "dab", "den", "dad", "dent", "dock", "dark", "dust",
    #         "done","donna","do","dodo", "lead", "lord","lorem","lore","lores"]

    #trie.buildTrie(words)
    #word="do"
    #print(f"Autocomplete words for {word} are: {trie.findCandidates(word,[])}")
    #word="lo"
    #print(f"Autocomplete words for {word} are: {trie.findCandidates(word,[])}")

