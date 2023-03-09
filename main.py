from Trie import Trie

if __name__ == "__main__":
    trie = Trie()
    trie.insertWord("Donkey")
    trie.insertWord("Done")
    print(trie.getTrie())
