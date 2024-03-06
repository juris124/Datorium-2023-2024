class Book:
    def __init__(self, title, author, publisher, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        # Izņemt grāmatu pēc nosaukuma

    def search_by_title(self, title):
        # Meklēt grāmatu pēc nosaukuma un atgriezt rezultātus

    def search_by_author(self, author):
        # Meklēt grāmatu pēc autora un atgriezt rezultātus

    def display_all_books(self):
        # Attēlot visu pieejamo grāmatu sarakstu

    def display_book_info(self, title):
        # Attēlot konkrētas grāmatas informāciju
