from search.indexer import InvIndex
import unittest

for i in range(1, 2):
    path = "t" + str(i) + "/input.txt";
    i = InvIndex();
    i.add_document(path);
    a = i.dictionary;
    for elem in a:
        print(elem);