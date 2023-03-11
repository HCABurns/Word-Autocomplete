# Word-Autocomplete
This is a word autocomplete program created in Python. It is implemented using a dictionary to imitate a Trie data structure.

## What is a trie?
A trie is a graph where the key is a individual character and the children are letters that proceed that key in a word. A flag of "!" has been used to define the end of a word and can be used for retrieval. To demonstrate this, a trie has been constructed and displayed below using the following words: lead, lord, lore, lores, and lorem. The root is not the letter "L" in order for other words that do not begin with "L" to be added to the trie.

![Trie representation as a graph](https://live.staticflickr.com/65535/52736761380_aa453f8b18_w.jpg)

## How it is being implemented in Python?

The trie is implemented using a dictionary. A dictionary, also referred to as a hashmap, works by mapping a key to a value. In this sutation the key relates to a letter in a word, or a "!" marking the end of a word, and the value is another dictionary holding information of letters proceeding the key. A dictionary has been chosen for the implementation due to the time complexity of lookup and insertion. The time complexity of look-up and insertion for a dictionary is O(1). 


## Future Additions:
  * Adding a popularity mesaure to each word in the database that can be used to order the list of return candidate words. (For the purpose of updating the database and making the returned list more useful)


