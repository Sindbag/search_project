import unittest
from search.indexer import split_query
from search.indexer import InvIndex
from search.query import Query


class TestInvIndexGetMethods(unittest.TestCase):
    def test_inv_index_get_0(self):
        inverted_index = InvIndex()
        inverted_index.dictionary["qwerty"] = set([3])     
        inverted_index.dictionary["admin"] = set([3])  
        inverted_index.dictionary["father"] = set([2])  
        inverted_index.dictionary["fatnet"] = set([1])  
        inverted_index.dictionary["codeforces"] = set([1])
        inverted_index.dictionary["sister"] = set([2])    
        inverted_index.dictionary["qw"] = set([0])  
        inverted_index.dictionary["rn"] = set([0])  
        inverted_index.dictionary["we"] = set([0])
        inverted_index.dictionary["et"] = set([0])        
        q = Query("qw e")
        self.assertEqual(inverted_index.get_all(q), [])    
    def test_inv_index_get_1(self):
        inverted_index = InvIndex()
        inverted_index.dictionary["qwerty"] = set([3])     
        inverted_index.dictionary["admin"] = set([3])  
        inverted_index.dictionary["father"] = set([2])  
        inverted_index.dictionary["fatnet"] = set([1])  
        inverted_index.dictionary["codeforces"] = set([1])
        inverted_index.dictionary["sister"] = set([2])    
        inverted_index.dictionary["qw"] = set([0])  
        inverted_index.dictionary["rn"] = set([0])  
        inverted_index.dictionary["we"] = set([0])
        inverted_index.dictionary["et"] = set([0])        
        q = Query("codeforces,,, fatnet,  father qwerty")
        self.assertEqual(inverted_index.get_all(q), [1, 2, 3])
    def test_inv_index_get_2(self):
        inverted_index = InvIndex()
        inverted_index.dictionary["qwerty"] = [3]     
        inverted_index.dictionary["admin"] = [3]  
        inverted_index.dictionary["father"] = [2]  
        inverted_index.dictionary["fatnet"] = [1]  
        inverted_index.dictionary["codeforces"] = [1]
        inverted_index.dictionary["sister"] = [2]     
        inverted_index.dictionary["qw"] = [0]  
        inverted_index.dictionary["rn"] = [0]  
        inverted_index.dictionary["we"] = [0]  
        inverted_index.dictionary["et"] = [0]        
        q = Query("codeforces fatnet  father qwerty")
        self.assertEqual(inverted_index.get_all(q), [1,2,3])  


if __name__ == '__main__':
    unittest.main()