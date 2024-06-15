from bible import Bible
from books import Book

def exit_program():
    print("SHALOM!, MAY THE PEACE OF THE LORD BE UPON YOU BRETHREN")
    exit()

def list_bibles():
    bibles = Bible.get_all()
    for bible in bibles:
        print(bible)

def find_bible_by_name():
    name = input("Enter the Bible's name: ")
    bible = Bible.find_by_name(name)
    print(bible) if bible else print(f'Bible {name} not found')

def find_bible_by_id():
    id_ = input("Enter the Bible's id: ")
    bible = Bible.find_by_id(id_)
    print(bible) if bible else print(f'Bible {id_} not found')

def create_bible():
    testament = input("Enter the Bible's testament: ")
    category = input("Enter the Bible's category: ")
    try:
        bible = Bible.create(testament, category)
        print(f'Success: {bible}')
    except Exception as exc:
        print("Error creating Bible: ", exc)

def update_bible():
    id_ = input("Enter the Bible's id: ")
    if bible := Bible.find_by_id(id_):
        try:
            testament = input("Enter the Bible's new testament: ")
            bible.testament = testament
            category = input("Enter the Bible's new category: ")
            bible.category = category

            bible.update()
            print(f'Success: {bible}')
        except Exception as exc:
            print("Error updating Bible: ", exc)
    else:
        print(f'Bible {id_} not found')

def delete_bible():
    id_ = input("Enter the Bible's id: ")
    if bible := Bible.find_by_id(id_):
        bible.delete()
        print(f'Bible {id_} deleted')
    else:
        print(f'Bible {id_} not found')

def list_books():
    books = Book.get_all()
    for book in books:
        print(book)

def find_book_by_name():
    name = input("Enter the Book's name: ")
    book = Book.find_by_name(name)
    print(book) if book else print(f'Book {name} not found')

def find_book_by_id():
    id_ = input("Enter the Book's id: ")
    book = Book.find_by_id(id_)
    print(book) if book else print(f'Book {id_} not found')

def create_book():
    name = input("Enter the Book's name: ")
    bible_id = input("Enter the Book's Bible id: ")
    try:
        book = Book.create(name, bible_id)
        print(f'Success: {book}')
    except Exception as exc:
        print("Error creating Book: ", exc)

def update_book():
    id_ = input("Enter the Book's id: ")
    if book := Book.find_by_id(id_):
        try:
            name = input("Enter the Book's new name: ")
            book.name = name
            bible_id = input("Enter the Book's new Bible id: ")
            book.bible_id = bible_id

            book.update()
            print(f'Success: {book}')
        except Exception as exc:
            print("Error updating Book: ", exc)
    else:
        print(f'Book {id_} not found')

def delete_book():
    id_ = input("Enter the Book's id: ")
    if book := Book.find_by_id(id_):
        book.delete()
        print(f'Book {id_} deleted')
    else:
        print(f'Book {id_} not found')

def list_bible_books():
    bible_id = input("Enter the Bible's id: ")
    books = Book.find_by_bible_id(bible_id)
    if books:
        for book in books:
            print(book)
    else:
        print(f'No books found for Bible {bible_id}')
