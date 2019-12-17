from collections import defaultdict
from .document import Document


class InvIndex:
    def __init__(self):
        self.dictionary = defaultdict(set)
        self.documents = []

    def add_document(self, doc):
        pass

    def get(self, word):
        return self.dictionary[word]

    def get_all(self, query):
        word_list = dict()
        for _query_word_ in query.get_clean():
            for _word_ in self.get(_query_word_):
                if _word_ not in word_list:
                    word_list[_word_] = 1
                else:
                    word_list[_word_] += 1
        m = list(word_list.items())
        m.sort(key=lambda x: (-x[1], x[0]))
        sp = []
        for x in m:
            sp.append(x[0])
        return sp


index = InvIndex()


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