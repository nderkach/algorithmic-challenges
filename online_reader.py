class Book(object):
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return "{} by {}".format(title, author)

    def open(self):
        # fetch book contents
        pass

class OnlineReader(object):
    def __init__(self):
        self.books = [Book("Book " + i, "Author " + i) for i in range(10)]

    def __iter__(self):
        for book in self.books:
            yield book

    def search(self, name=None, isbn=None, author=None):
        books = []
        # search by ones of parameters above
        return books

