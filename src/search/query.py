class Query:
    text = ''
    clean = []

    def __init__(self, query):
        if query is None:
            return
        self.text = query
        self.clean = query.split(' ')

    def get_text(self):
        return self.text

    def get_clean(self):
        return self.clean
