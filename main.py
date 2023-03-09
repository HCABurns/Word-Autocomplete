from Trie import Trie

def generateTrie(trie):
    
    for word in words:
        trie.insertWord(word)

if __name__ == "__main__":
    trie = Trie()
    words = ["deer", "desk", "donkey", "dart", "deep", "dance", "duck",
             "dip", "dab", "den", "dad", "dent", "dock", "dark", "dust",
             "done","donna","do","dodo", "lead", "lord","lorem","lore","lores"]
    trie.buildTrie(words)
    word="do"
    print(f"Autocomplete words for {word} are: {trie.findCandidates(word,[])}")
    word="lo"
    print(f"Autocomplete words for {word} are: {trie.findCandidates(word,[])}")

