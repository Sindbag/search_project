#!/usr/bin/env python
# -*- coding: utf-8 -*-

from search.document import Document
from collections import defaultdict
from search.query import Query
import codecs
import os


def split_query(query):
    word = ""
    words = []
    for c in query:
        if 'A' <= c <= 'Z' or 'a' <= c <= 'z' or '0' <= c <= '9' or 'А' <= c <= 'Я' or 'а' <= c <= 'я':
            word += c
        else:
            if word != "" and len(word) > 2:
                words.append(word)
            word = ""
    if (word != "" and len(word) > 2):
        words.append(word)
    return words


class InvIndex:
    def __init__(self):
        self.dictionary = defaultdict(set)
        self.documents = []

    def add_document(self, path):
        f = codecs.open(path, "r", "utf-8")
        text = f.read()
        words = split_query(text)
        self.documents.append(Document(path, path, path))
        for s in words:
            self.dictionary[s].add(len(self.documents) - 1)

    def get(self, word):
        return self.dictionary[word]

    def get_all(self, query):
        doc_freqs = {}

        for word in split_query(query.get_text()):
            word_doc_idxs = self.get(word)
            for index_document in word_doc_idxs:
                if index_document not in doc_freqs:
                    doc_freqs[index_document] = 1
                else:
                    doc_freqs[index_document] = doc_freqs[index_document] + 1
        doc_freq_pairs = []
        for index_document, value in doc_freqs.items():
            doc_freq_pairs.append((index_document, value))
        doc_freq_pairs = sorted(doc_freq_pairs, key=lambda x: (-x[1], x[0]))
        result = []
        for doc, freq in doc_freq_pairs:
            result.append(doc)
        return result

index = InvIndex()


def build_index(path):
    # Считывает данные и строит индекс
    arr = os.listdir(path)
    filter(lambda s: (s[-4:]) == ".txt", arr)
    for file in arr:
        index.add_document(path + "/" + file)

