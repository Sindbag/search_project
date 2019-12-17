import unittest
from search.indexer import InvIndex


class TestInvIndexGetMethods(unittest.TestCase):
    def test_inv_index_get(self):
        inverted_index = InvIndex()
        inverted_index.dictionary["ab"] = [0]     
        inverted_index.dictionary["qw"] = [0]  
        inverted_index.dictionary["rn"] = [0]  
        inverted_index.dictionary["we"] = [0]  
        inverted_index.dictionary["et"] = [1]
        q = "qw     e"
        self.assertEqual(inverted_index.get_all(q), [1, 0])


if __name__ == '__main__':
    unittest.main()