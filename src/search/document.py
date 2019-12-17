class Document:
    def __init__(self, title, snippet, filepath):
        # можете здесь какие-нибудь свои поля подобавлять
        self.title = title
        self.snippet = snippet
        self.path = filepath

    def format(self, query):
        # возвращает пару тайтл-текст, отформатированную под запрос
        return {'title': self.title, 'text': self.snippet + ' ...'}

    def get_text(self):
        return self.snippet

    def get_title(self):
        return self.title
