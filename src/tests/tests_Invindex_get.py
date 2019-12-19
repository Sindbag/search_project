import unittest
from search.indexer import InvIndex
from search.query import Query
from search.indexer import split_query


class TestInvIndexGetMethods(unittest.TestCase):
    def test_inv_index_get(self):
        inverted_index = InvIndex()
        inverted_index.dictionary["ab"] = set([0])
        inverted_index.dictionary["qw"] = set([0])
        inverted_index.dictionary["rn"] = set([0])
        inverted_index.dictionary["we"] = set([0])
        inverted_index.dictionary["et"] = set([0])
        inverted_index.dictionary["father"] = set([3])
        inverted_index.dictionary["fatnet"] = set([2])
        inverted_index.dictionary["codeforces"] = set([2])
        inverted_index.dictionary["qwerty"] = set([1])
        inverted_index.dictionary["admin"] = set([1])
        q = Query("qw e")
        arr = inverted_index.get_all(q);
        self.assertEqual(inverted_index.get_all(q), [2, 1, 3])


if __name__ == '__main__':
    unittest.main()