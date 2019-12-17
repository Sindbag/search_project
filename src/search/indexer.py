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


def check(sym):
    return ('a' <= sym <= 'z' or
            'A' <= sym <= 'Z' or
            'а' <= sym <= 'я' or
            'А' <= sym <= 'Я' or
            '0' <= sym <= '9')


def words_clear(words):
    words_del = []
    curr_word = ""
    for sym in words:
        if check(sym):
            curr_word += sym
        else:
            if len(curr_word) > 2:
                words_del += [curr_word]
            curr_word = ""
    if len(curr_word) > 2:
        words_del += [curr_word]
    return words_del


class InvIndex:
    def __init__(self):
        self.dictionary = defaultdict(set)
        self.documents = []

    def add_document(self, path):
        file = codecs.open(path, 'r', "utf-8")
        text = file.read()
        self.documents += [Document(path, path, path)]
        for word in words_clear(text):
            self.dictionary[word].add(len(self.documents) - 1)

    def get(self, word):  # ->list
        pass

    def get_all(self, query):
        pass
