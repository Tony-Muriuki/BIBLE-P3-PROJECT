from function import (
    exit_program,
    list_bibles,
    find_bible_by_name,
    find_bible_by_id,
    create_bible,
    update_bible,
    delete_bible,
    list_books,
    find_book_by_name,
    find_book_by_id,
    create_book,
    update_book,
    delete_book,
    list_bible_books
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_bibles()
        elif choice == "2":
            find_bible_by_name()
        elif choice == "3":
            find_bible_by_id()
        elif choice == "4":
            create_bible()
        elif choice == "5":
            update_bible()
        elif choice == "6":
            delete_bible()
        elif choice == "7":
            list_books()
        elif choice == "8":
            find_book_by_name()
        elif choice == "9":
            find_book_by_id()
        elif choice == "10":
            create_book()
        elif choice == "11":
            update_book()
        elif choice == "12":
            delete_book()
        elif choice == "13":
            list_bible_books()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all Bibles")
    print("2. Find Bible by name")
    print("3. Find Bible by id")
    print("4. Create Bible")
    print("5. Update Bible")
    print("6. Delete Bible")
    print("7. List all Books")
    print("8. Find Book by name")
    print("9. Find Book by id")
    print("10. Create Book")
    print("11. Update Book")
    print("12. Delete Book")
    print("13. List all Books in a Bible")

if __name__ == "__main__":
    main()
