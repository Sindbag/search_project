#!/usr/bin/env python
# -*- coding: utf-8 -*-

from search.document import Document
from collections import defaultdict
from search.query import Query

class InvIndex:
    def __init__(self):
        self.dictionary = defaultdict(set)
        self.documents = []
    def add_document(self, doc):
        pass
    
    def get(self, word):
        return self.dictionary[word]
    def get_all(self, query):
        clovar = {} # clovar[индекс документа] = как часто встречается  
        
        for word in query.get_clean():
            list_index_document = self.get(word) # множество индексов документов в которых встречается слова из запроса
            for index_document in list_index_document:
                if index_document not in clovar: # проверка присутствия индекса документа в словаре(clovar)
                    clovar[index_document] = 1 
                else:
                    clovar[index_document] = clovar[index_document] + 1
        result = [] # список [индекс документа, как часто встречается документ по запросу каждого слова(суммарно)]
        for index_document, value in clovar.items():
            result.append((index_document, value))
        result = sorted(result, key=lambda x: (-x[1], x[0])) # сортируем наш список в порядке убывания значения, затем по индексу документа
        answer = []
        for i, j in result:
            answer.append(i)
        return answer

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
        
    
    
index = InvIndex()
                 