import unittest
from  Dictionary import Dictionary

class DictonaryTests(unittest.TestCase):
    
    def setUp(self):
        self.testDic                = Dictionary('../words')
        self.expectedTestFriends    = ('lest','vest','telt','tests','teste','text','nest','teat','rest','testa','testy','fest','pest','tost','jest','gest','yest','hest','tent')
        self.expectedLeviathens     = set()

    def test_size(self):
        self.assertEqual(len(self.testDic._dictonary), 380645, "The size of the dictionary is off.  Check file and constructor")
    
    def test_levenshtein(self):
        self.assertEqual(len(self.testDic._levenshtein('test')), 238)
        #self.assertItemsEqual(self.testDic._leviathens('test').sort(), self.expectedLeviathens,"Set of leviathens don't match")

    def test_friends(self):
        self.assertEqual(len(self.testDic.friends('test')), 19)
        self.assertItemsEqual(self.testDic.friends('test'), self.expectedTestFriends )
        
    def test_networkSize(self):
        self.assertEqual(len(self.testDic.network('test')), 64413)
        pass
    
if __name__ == "__main__":
    unittest.main()