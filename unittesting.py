from Trie import Trie
import unittest
class TestMethods(unittest.TestCase):
    """
    This class is used to test individual methods in the Trie class.
    """

    def testGetTrie(self):
        """
        Testing the getTrie function in the Trie class.

        Return
        ----------
        None
        """
        trie = Trie()
        self.assertEqual(trie.getTrie(), {})
        print("GetTrie test finished")

    def testInsertWord(self):
        """
        Testing the insertWord function in the Trie class.

        Return
        ----------
        None
        """
        trie = Trie()
        self.assertEqual(trie.insertWord("Insert"),None)
        print("InsertWord test finished")

    def testGetDirectChildren(self):
        """
        Testing the getDirectChildren function in the Trie class.

        Return
        ----------
        None
        """
        trie=Trie()
        trie.insertWord("insert")
        trie.insertWord("insect")
        self.assertEqual(trie.getDirectChildren("inse"),["r","c"])
        self.assertEqual(trie.getDirectChildren("none"),'Error: Word is not currently implemented!')
        print("GetDirectChildren test finished")

    def testGetChildren(self):
        """
        Testing the getChildren function in the Trie class.

        Return
        ----------
        None
        """
        trie=Trie()
        trie.insertWord("insert")
        trie.insertWord("insect")
        self.assertEqual(trie.getChildren({'r': {'t': {'!': True}}, 'c': {'t': {'!': True}}}),["r","c"])
        print("GetChildren test finished")

    def testContainsWord(self):
        """
        Testing the containsWord function in the Trie class.

        Return
        ----------
        None
        """
        trie = Trie()
        self.assertEqual(trie.containsWord("Anything"),False)
        trie.insertWord("lorem")
        self.assertEqual(trie.containsWord("Anything"),False)
        self.assertEqual(trie.containsWord("lorem"),True)
        print("ContainsWord test finished")


    def testFindCandidates(self):
        """
        Testing the findCandidates function in the Trie class.

        Return
        ----------
        None
        """
        trie = Trie()
        self.assertEqual(trie.findCandidates("Anything",[]),[])
        trie.insertWord("insert")
        trie.insertWord("insect")
        trie.insertWord("indirect")
        trie.insertWord("island")
        self.assertEqual(trie.findCandidates("i",[]),["insert","insect","indirect","island"])
        self.assertEqual(trie.findCandidates("is",[]),["island"])
        self.assertEqual(trie.findCandidates("never",[]),[])
        print("FindCandidates test finished")


if __name__ == '__main__':
    unittest.main()

    
