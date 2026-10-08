# Import datetime module for due date tracking
import datetime

# Define class for Book
class Book:

    def __init__(self, title, author):
        self.title = title  # Set title of book
        self.author = author  # Set author of book
        self.availability = True  # Set book as available when added to library
        self.due_date = None  # Set due date to None when book is available

    # String representation for book title and author
    def __str__(self):
        return f"Book: {self.title} Author: {self.author}"

# Define class for Member
class Member:

    def __init__(self, name, member_id):
        self.name = name  # Set member name
        self.member_id = member_id  # Set member ID
        self.borrowed_books = []  # List to track borrowed books

    # String representation for member name and ID
    def __str__(self):
        return f"Member: {self.name} ID: {self.member_id}"

# Define class for Library    
class Library:
    
    def __init__(self):
        self.books = []  # List to store all books in library
        self.members = []  # List to store all members in library

    # Add book to library
    def add_book(self, book):
        self.books.append(book)

    # Register member to library
    def register_member(self, member):
        self.members.append(member)

    # Borrow book from library
    def borrow_book(self, book, member):
        if book.availability:
            book.availability = False
            book.due_date = datetime.date.today() + datetime.timedelta(days=30)  # Set due date for borrowed book
            member.borrowed_books.append(book)  # Add book to member's list of borrowed books
            print(f"{member.name} has borrowed {book.title}. Due date: {book.due_date}")
        else:
            print(f"{book.title} is not available for borrowing")

    # Return book to library
    def return_book(self, book, member):
        if book in member.borrowed_books:
            book.availability = True
            member.borrowed_books.remove(book)  # Remove book from member's list of borrowed books
            print(f"{book.title} has been returned by {member.name}")
        else:
            print(f"{book.title} was not borrowed by {member.name}")

    # String representation for listing all book titles and member names
    def __str__(self):
        books_str = ", ".join([book.title for book in self.books])  # Join book titles into string
        members_str = ", ".join([member.name for member in self.members])  # Join member names into string
        return f"Books in Library: {books_str}, Library Members: {members_str}"

    # Search for book in library by title and check books availability
    def search_book(self, title):
        for book in self.books:
            if book.title == title and book.availability == True:
                return f"{title} found in library and available for borrowing"
            elif book.title == title and book.availability == False:
                return f"{title} found in library but not available for borrowing"
        else:
            return f"{title} not found in library"

    # Count number of available and borrowed books in library
    def retrieve_book_counts(self):
        available_books = len([book for book in self.books if book.availability])
        borrowed_books = len(self.books) - available_books
        return f"Available Books: {available_books}, Borrowed Books: {borrowed_books}"
    
# Create instance of each book
book1 = Book("The Hobbit", "J.R.R. Tolkien")
book2 = Book("Dune", "Frank Herbert")
book3 = Book("Treasure Island", "Robert Louis Stevenson")

# Create instance of each member
member1 = Member("Andrew", 1)
member2 = Member("Amy", 2)

# Create instance of library
library = Library()

# Add books to library
library.add_book(book1)
library.add_book(book2)

# Register members to library
library.register_member(member1)
library.register_member(member2)

# Output Testing

# Call a function that directly prints output for a member borrowing and returning a book
library.borrow_book(book1, member1)

library.return_book(book1, member1)

# Call a function that returns a value for a searched book
result = library.search_book("The Hobbit")
print(result)

result = library.search_book("Great Expectations")
print(result)

# Call a function that returns a value for available and borrowed books
result = library.retrieve_book_counts()
print(result)

# Print library information
print(library)