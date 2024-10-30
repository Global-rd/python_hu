class Author:
    def __init__(self, name: str, nationality: str):
        self.name = name
        self.nationality = nationality

    def __str__(self):
        return f"{self.name} ({self.nationality})"

class Book:
    def __init__(self, title: str, genre: str, author: Author):
        self.title = title
        self.genre = genre
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book: Book) -> "Library":
        self.books.append(book)
        return self 

    def list_books(self) -> "Library":
        print(f"Available books in {self.name}: ")
        for book in self.books:
            print(book)
        return self 

    def remove_book(self, title: str) -> "Library":
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return self
        print(f"No book found with this title: {title}")
        return self 

author1 = Author("George X", "British")
author2 = Author("Tim X", "Scottish")

book1 = Book("How to get away with murder", "crime", author1)
book2 = Book("Test x", "crime", author2)

library1 = Library("Szabo Ervin Konyvtar")
library1.add_book(book1).add_book(book2).list_books().remove_book("Test x").list_books()