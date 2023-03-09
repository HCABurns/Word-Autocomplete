from Trie import Trie

if __name__ == "__main__":
    trie = Trie()
    trie.insertWord("Donkey")
    trie.insertWord("Done")
    trie.insertWord("Donna")
    trie.insertWord("Do")
    trie.insertWord("Dodo")
    #print(trie.getTrie())

    print(trie.findCandidates("don"))
    print(trie.candidateWords)
