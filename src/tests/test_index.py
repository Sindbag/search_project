import unittest
from search.indexer import InvIndex
from search.query import Query


class TestInvIndexGetMethods(unittest.TestCase):
    def test_inv_index_get(self):
        inverted_index = InvIndex()
        inverted_index.dictionary['what'] = [7, 4, 5, 1]
        inverted_index.dictionary['sweat'] = [4, 1, 7]
        inverted_index.dictionary['dreams'] = [7]
        inverted_index.dictionary['are'] = [1, 4, 7]
        inverted_index.dictionary['made'] = [7, 1, 4]
        inverted_index.dictionary['of'] = [7, 4]
        q = Query('')
        self.assertEqual(inverted_index.get(''), set())
        # self.assertEqual(inverted_index.get_all(q), [])


if __name__ == '__main__':
    unittest.main()
