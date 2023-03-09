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

    def getTrie(self):
        """
        This function will return the root of the trie.

        Returns
        ----------
        dict - Dictionary pointing to the root of the trie.
        """
        return self.trie

    def insertWord(self,word):
        """
        Function to insert a word into the trie. Words are converted to lowercase
        before being added to the trie.

        Parameters
        ----------
        word : str
            This is the word that will be added to the trie.

        Returns
        ----------
        None
        """
        #Create a new object that can be manipulated to insert a new word.
        trie = self.trie
        for char in word.lower():
            if trie.get(char,False) == False:
                trie[char] = {}
            trie=trie[char]
        trie["!"] = True

    def getDirectChildren(self,word):
        """
        This function will return an array of letters, if any, of the next letters in the trie after the given word.

        Parameters
        ----------
        word : str
            This is the word that will be used to find the next proceeding letters.
        
        Returns
        ----------
        list - List of letters.
        """
        trie = self.trie
        for char in word.lower():
            if trie.get(char,False) is not False:
                trie=trie[char]
            else:
                return "Error: Word is not currently implemented!"
        return list(trie.keys())

    def getChildren(self,trie):
        """
        This is used to return the dictionaries of the children of the trie given.

        Parameters
        ----------
        trie : dict
            This is the trie that the children will be found from.
        
        Returns
        ----------
        list - List of dictionaries.
        """
        return list(trie.keys())

    def containsWord(self,word):
        """
        This is used to find if a word is present in the trie or not.

        Parameters
        ----------
        word : str
            This is the word that is being checked for in the trie.
            
        Returns
        ----------
        boolean - True or False (if it's in the trie or not).
        """
        trie = self.trie
        for char in word.lower():
            if trie.get(char,False) == False:
                return False
            trie=trie[char]
        return True

    def findCandidates(self,word,candidateWords):
        """
        Function to find the candidate words proceeding the word.
        This function uses recursion and updates a private variable.

        Parameters
        ----------
        word : str
            This is the word that is being used to look for complete words.
        candidateWords : list
            This is a list of words that the given word is a prefix of.
            
        Returns
        ----------
        list - This is a list of words that the given word is a prefix of.
        """
        #Navigate to end of given word
        trie = self.trie
        for char in word.lower():
            if trie.get(char,False) == False:
                return []
            trie=trie[char]
        
        #Naviagte through the children until finding a "!"
        children = self.getChildren(trie)
        if "!" in children:
            candidateWords.append(word)
        for letter in children:
            if letter!="!":
                self.findCandidates(word+letter,candidateWords)
        return candidateWords
                
        

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
    print(main.findCandidates("jame",[]))
    print(main.getChildren(main.trie["j"]["a"]["m"]))    

if __name__ == "__main__":
    main = Trie()
    manualTesting()

