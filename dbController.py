#Import to allow for accessing and updating the database.
import sqlite3

class dbController():
    """
    This is the class that will deal with all the retrieval and updating of the database.

    Methods
    ----------
    getNames() - Retrieves all the words in the database and returns as a list.
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
            - This is the word that will be added the the database.

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
        

if __name__ == "__main__":
    db = dbController()
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
    word = "that's"
    added = db.addWord(word)
    print(f"Has {word} successfully been added to the db? {'Yes' if added else 'No'}")
    db.con.close()
