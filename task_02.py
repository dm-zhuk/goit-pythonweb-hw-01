from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


# Book class (SRP)
@dataclass
class Book:
    title: str
    author: str
    year: int

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# Library interface (ISP, LSP, DIP)
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_books(self) -> List[Book]:
        pass


# Library implementation (SRP, OCP, LSP)
class Library(LibraryInterface):
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        self.books[:] = [book for book in self.books if book.title != title]

    def get_books(self) -> List[Book]:
        return self.books


# DigitalLibrary for extension (OCP, LSP)
class DigitalLibrary(LibraryInterface):
    def __init__(self, max_books: int = 5):
        self.books: List[Book] = []
        self.max_books: int = max_books

    def add_book(self, book: Book) -> None:
        if len(self.books) >= self.max_books:
            logger.warning(
                f"Cannot add {book.title}: Library is full "
                f"(max {self.max_books} books)."
            )
            return
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        self.books[:] = [book for book in self.books if book.title != title]

    def get_books(self) -> List[Book]:
        return self.books


# Library manager (SRP, DIP)
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library: LibraryInterface = library

    def add_book(self, title: str, author: str, year: str) -> None:
        try:
            year_int = int(year)
            book = Book(title, author, year_int)
            self.library.add_book(book)
            logger.info(f"Added book: {book}")
        except ValueError:
            logger.error(f"Invalid year: {year}. Year must be a number.")

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)
        logger.info(f"Removed book with title: {title}")

    def show_books(self) -> None:
        books = self.library.get_books()
        if not books:
            logger.info("No books in the library.")
        for book in books:
            logger.info(str(book))


# Main function
def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.error("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
