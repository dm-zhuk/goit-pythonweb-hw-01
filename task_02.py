from abc import ABC, abstractmethod
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
class Book:
    """
    Represents a book with a title, author, and year.
    This class is only responsible for book-related data.
    """

    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, author: {self.author}, year: {self.year}"


# Library interface (ISP, LSP, DIP)
class LibraryInterface(ABC):
    """
    Defines the interface for interacting with a library.
    This allows for different library implementations.
    """

    @abstractmethod
    def add_book(self, book: Book) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove_book(self, title: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def show_books(self) -> List[Book]:
        raise NotImplementedError


# Library implementation (SRP, OCP, LSP)
class Library(LibraryInterface):
    """
    Implements the LibraryInterface.  Can be extended without modification
    (OCP) and any derived class can be used in place of it (LSP).
    """

    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        self.books[:] = [book for book in self.books if book.title != title]

    def show_books(self) -> List[Book]:
        return self.books


# Library manager (SRP, DIP)
class LibraryManager:
    """
    Manages the interaction between the user and the library.
    Depends on the LibraryInterface, not a concrete Library class.
    """

    def __init__(self, library: LibraryInterface):
        self.library = library

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
        books = self.library.show_books()
        if not books:
            logger.info("No books in the library.")
        for book in books:
            logger.info(str(book))


# Test the function
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
                logger.warning("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
