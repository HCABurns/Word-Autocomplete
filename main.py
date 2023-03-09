from Trie import Trie

if __name__ == "__main__":
    trie = Trie()
    trie.insertWord("Donkey")
    trie.insertWord("Done")
    trie.insertWord("Donna")
    trie.insertWord("Do")
    print(trie.getTrie())
