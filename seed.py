# Import the classes
from bible import Bible
from books import Book

# Create the tables
Bible.create_table()
Book.create_table()

# Create a Bible instance
bible1 = Bible.create('Old Testament', 'Law')

# Create some Book instances
book1 = Book.create('Genesis', bible1.id)
book2 = Book.create('Exodus', bible1.id)

# Retrieve all books for a given Bible instance
books_in_bible1 = bible1.books()
print(books_in_bible1)