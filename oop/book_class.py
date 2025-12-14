# book_class.py
# Definition of the Book class with magic methods

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor: Initializes the Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Informal string representation of the Book instance."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation that can recreate the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
