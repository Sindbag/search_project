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
        words = split_query(text);
        for s in words:
            self.dictionary[s].add(Document(path, path, path))
            self.documents.append(Document(path, path, path))

    def get(self, word):
        return self.dictionary[word]

    def get_all(self, query):
        doc_freqs = {}

        for word in split_query(query):
            word_doc_idxs = self.get(word)
            for index_document in word_doc_idxs:
                if index_document not in doc_freqs:
                    doc_freqs[index_document] = 1
        doc_freqs = {}  
        
        for word in query.get_clean():
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

    for file in os.listdir(path):
        index.add_document(path + "/" + file)

def build_index(path):
    # Считывает данные и строит индекс
    
    for file in os.listdir(path):
        index.add_document(path + "/" + file)
    
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