from __init__ import CONN, CURSOR
from bible import Bible
from books import Book

# Function to seed the database
def seed_database():
    # Drop tables if they exist to start fresh
    Book.drop_table()
    Bible.drop_table()

    # Create tables
    Bible.create_table()
    Book.create_table()

    # Create Bible instances
    bible1 = Bible.create('Old Testament', 'Law')
    bible2 = Bible.create('Old Testament', 'Prophets')
    bible3 = Bible.create('Old Testament', 'Wisdom')
    bible4 = Bible.create('Old Testament', 'History')
    bible5 = Bible.create('New Testament', 'Gospels')
    bible6 = Bible.create('New Testament', 'Epistles')

    # Create Book instances associated with each Bible
    book1 = Book.create('Genesis', bible1.id)
    book2 = Book.create('Exodus', bible1.id)

    book3 = Book.create('Isaiah', bible2.id)
    book4 = Book.create('Jeremiah', bible2.id)

    book5 = Book.create('Psalms', bible3.id)

    book6 = Book.create('Joshua', bible4.id)
    book7 = Book.create('Judges', bible4.id)

    book8 = Book.create('Matthew', bible5.id)
    book9 = Book.create('Mark', bible5.id)
    book10 = Book.create('Luke', bible5.id)
    book11 = Book.create('John', bible5.id)

    book12 = Book.create('Romans', bible6.id)
    book13 = Book.create('1 Corinthians', bible6.id)
    book14 = Book.create('2 Corinthians', bible6.id)

    # Retrieve all books for a given Bible instance
    books_in_bible1 = bible1.books()
    print("Books in Bible 1:", books_in_bible1)

seed_database()

