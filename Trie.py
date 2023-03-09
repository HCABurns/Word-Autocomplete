class Trie():
    def __init__(self):
        """
        Create a trie object. This is implemented as a dictionary where keys are
        consisted as letters and values are dictionaries that relate to letters
        following the key in words.

        Parameters
        ----------
        trie : dict of str: dict

        Methods
        ----------
        getTrie() - Returns the trie object. (Reference to the root) 
        insertWord(word) - Allows insrtion of words to the trie.
        getDirectChildren(word) - Returns array of letters that follow the given
                                  word in the trie.
        containsWord(word) - Returns boolean regarding if that word is in the trie or not.
        findCandidates(word) - Returns array of all possible words proceeding the given
                               text.
        """
        self.trie = {}
        self.candidateWords = []

    def getTrie(self):
        return self.trie

    def insertWord(self,word):
        """
        Function to insert a word into the trie. Words are converted to lowercase
        before being added to the trie.

        Parameters
        ----------
        word : str
            This is the word that will be added to the trie.
        """
        #Create a new object that can be manipulated to insert a new word.
        trie = self.trie
        for char in word.lower():
            if trie.get(char,False) == False:
                trie[char] = {}
            trie=trie[char]
        trie["!"] = True

    def getDirectChildren(self,word):
        trie = self.trie
        for char in word.lower():
            if trie.get(char,False) is not False:
                trie=trie[char]
            else:
                return "Error: Word is not currently implemented!"
        return list(trie.keys())

    def getChildren(self,trie):
        return list(trie.keys())

    def containsWord(self,word):
        trie = self.trie
        for char in word.lower():
            if trie.get(char,False) == False:
                return False
            trie=trie[char]
        return True


    def findCandidates(self,word):
        """
        Function to find the candidate words proceeding the word.
        This function uses recursion and updates a private variable. 
        """
        #Navigate to end of given word
        trie = self.trie
        for char in word.lower():
            if trie.get(char,False) == False:
                return "No candidates have been found!"
            trie=trie[char]
        
        #Naviagte through the children until finding a "!"
        children = self.getChildren(trie)
        if "!" in children:
            self.candidateWords.append(word)
        for letter in children:
            if letter!="!":
                self.findCandidates(word+letter)


def manualTesting():
    help(Trie)
    print(main.trie)
    print(main.getTrie)
    print(main.insertWord("Jake"))
    print(main.insertWord("James"))
    print(main.insertWord("Jam"))
    print(main.trie)
    print(*main.trie["j"]["a"])
    print(main.getDirectChildren("Ja"))
    testWord = "James"
    print(f'Is word "{testWord}" in the trie? {"Yes" if main.containsWord(testWord) else "No"}')
    print(main.findCandidates("ja",[]))
    print(main.candidateWords)
    

if __name__ == "__main__":
    main = Trie()
    manualTesting()

