#Import to allow for accessing and updating the database.
import sqlite3

class DBController():
    """
    This is the class that will deal with all the retrieval and updating of the database.

    Methods
    ----------
    getWords() - Retrieves all the words in the database and returns as a list.
    addWord(word) - Adds a word to the database.
    deleteWord(word) - Removes a word from the database.
    containsWord(word) - Check if a word is in the database or not.
    """
    
    def __init__(self):
        #Connect to the database.
        self.con = sqlite3.connect('words.db', check_same_thread=False)
        #Create a database cursor to query using SQL.
        self.cur = self.con.cursor()


    def getWords(self):
        """
        This function will retrieve all the words in the database.

        Return
        ---------
        List - Returns a list containing all the words in the database.
        """
        words = []
        command = "SELECT word FROM Words"
        rows = self.cur.execute(command)
        for row in rows:
            word = row[0]
            words.append(word)
        return words

    def addWord(self,word):
        """
        This function allows for inserting new words into the database.
        Allows words that contains alphabetical characters, including "-" or "'".

        Parameters
        -------------
        word : string
            - This is the word that will be added to the database.

        Return
        -------------
        boolean - Returns true if the word has been added and false if it has not been added.
        """

        #Check to ensure the word contains only letter, hyphens or apostrophe.
        for char in word:
            if char.isalpha() == False and char not in ["'" , "-"]:
                return False
        #Create the execute the update and commit if successful. 
        try:
            self.cur.execute(f'INSERT INTO words ("word") VALUES ("{word}")')
        except sqlite3.IntegrityError:
            return False
        self.con.commit()
        return True


    def deleteWord(self,word):
        """
        This function allows for removing words from the database.

        Parameters
        -------------
        word : string
            - This is the word that will be removed from the database.

        Return
        -------------
        boolean - Returns true if the word has been removed and false if it has not been removed.
        """
        if self.containsWord(word):
            try:
                r = self.cur.execute(f'DELETE FROM words WHERE word="{word}"')
                self.con.commit()
                return True
            except sqlite3.IntegrityError:
                return False
        return False


    def containsWord(self,word):
        """
        This function will check if a word is in the database.

        Return
        ---------
        boolean - True or false for if the word is in the database or not.
        """
        command = "SELECT word FROM Words WHERE word='{}'".format(word)
        rows = self.cur.execute(command)
        for row in rows:
            return True
        return False


def manualTesting():
    """
    Test harness
    """
    names = db.getWords()
    print(names)
    word = "Jack"
    added = db.addWord(word)
    print(f"Has {word} successfully been added to the db? {'Yes' if added else 'No'}")
    word = "123"
    added = db.addWord(word)
    print(f"Has {word} successfully been added to the db? {'Yes' if added else 'No'}")
    word = "x-ray"
    added = db.addWord(word)
    print(f"Has {word} successfully been added to the db? {'Yes' if added else 'No'}")
    word = "added"
    added = db.addWord(word)
    print(f"Has {word} successfully been added to the db? {'Yes' if added else 'No'}")
    removed = db.deleteWord(word)
    print(f"Has {word} successfully been removed from the db? {'Yes' if removed else 'No'}")
    word = "x-ray"
    removed = db.deleteWord(word)
    print(f"Has {word} successfully been removed from the db? {'Yes' if removed else 'No'}")
        

if __name__ == "__main__":
    db = DBController()
    manualTesting()
    db.con.close()
