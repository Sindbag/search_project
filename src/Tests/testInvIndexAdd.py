from search.indexer import InvIndex


class TestInvIndex():
    def __init__(self):
        self.invInd = InvIndex()

    def test_add(self, path):
        self.invInd.add_document(path)
        for elem in self.invInd.dictionary:
            print(elem)


testInvInd = TestInvIndex()
testInvInd.test_add("test.txt")
