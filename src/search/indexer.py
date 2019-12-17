from .document import Document

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