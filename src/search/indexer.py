#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .document import Document
from collections import defaultdict
import codecs

index = []


def build_index():
    # Считывает данные и строит индекс
    index.append(Document(
        'The Beatles — Come Together',
        'Here come old flat top\nHe come groovin\' up slowly',
        'path_1'
    ))
    index.append(Document(
        'The Rolling Stones — Brown Sugar',
        'Gold Coast slave ship bound for cotton fields\nSold in the market down in New Orleans',
        'path_2'
    ))
    index.append(Document(
        'Физтех — Я променял девичий смех',
        'Я променял девичий смех\nНа голос лектора занудный,',
        'path_3'
    ))


def normal_word(word):
    res = ""
    arr = []
    for c in word:
        if 'A' <= c <= 'Z' or 'a' <= c <= 'z' or '0' <= c <= '9' or 'А' <= c <= 'Я' or 'а' <= c <= 'я':
            res += c
        else:
            if res != "":
                arr.append(res)
            res = ""
    if (res != ""):
        arr.append(res)
    return arr


class InvIndex:
    def __init__(self):
        self.dictionary = defaultdict(set) ##dictionary
        self.documents = []

    def add_document(self, path):
        f = codecs.open(path, "r", "utf-8")
        text = f.read()
        arr = normal_word(text);
        for s in arr:
            self.dictionary[s].add(Document(path, path, path))

    def get(self, word):
        return self.dictionary[word]
        
    def get_all(self, query):
        pass

