import unittest
from search.indexer import InvIndex


class TestInvIndexAddMethods(unittest.TestCase):
    def test_add(self):
        invInd = InvIndex()
        invInd.add_document("test.txt")
        invInd.add_document("test2.txt")
        invInd.add_document("test3.txt")
        ans_dictionary = {'apple': {0}, 'mine': {0}, 'sum': {0}, 'mama': {0}, 'мама': {0, 2}, 'Мама': {0, 2},
                          'раму': {0}, 'Привет': {0}, 'Andrey': {0}, 'llo': {1}, 'can': {1}, 'not': {1},
                          'use': {1}, 'space': {1}, '2019': {2}}
        self.assertEqual(invInd.dictionary,
                         ans_dictionary)


if __name__ == '__main__':
    unittest.main()

