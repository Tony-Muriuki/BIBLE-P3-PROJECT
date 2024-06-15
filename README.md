# BIBLE-P3-PROJECT

#OVERVIEW

The BIBLE PROJECT is a database management system for handling information about the Bible, including its books and categories. The system allows users to perform CRUD (Create, Read, Update, Delete) operations on Bible entries and associated Book entries. The project is implemented in Python, utilizing SQLite for database management.


#FEATURES

Bible Management: Add, view, update, and delete Bible entries.
Book Management: Add, view, update, and delete Book entries associated with specific Bibles.
Database Initialization: Seed the database with initial data for testing and demonstration purposes.
Command-Line Interface: Interact with the system via a user-friendly command-line interface.

#GETTING STARTED

#PREREQUISITES

Python 3.8.13 installed on your machine
SQLite3 installed on your machine

#INSTALLATION

#1: CLONE THE REPOSITORY

git clone https://github.com/yourusername/BIBLE-P3-PROJECT.git
cd BIBLE-P3-PROJECT

#2 CREATE AND ACTIVATE A VIRTUAL ENVIRONMENT

pipenv --python/usr/bin/python
pipenv install

#3:INSTALL DEPENDENCIES

pip install

#4:INITIALIZE THE DATABASE

python initialize_db.py

#5: SEED THE DATABASE WITH INITIAL DATA

    python seed.py

#USAGE

Run the main application:   python CLI.py

You will be presented with a menu to manage Bibles and Books. Select an option by entering the corresponding number.

#PROJECT STRUCTURE

1:CLI.py: The entry point of the application, containing the main menu loop.
2:seed.py: Script to seed the database with initial data.
3:bible.py: Contains the Bible class and methods for managing Bible entries.
4:books.py: Contains the Book class and methods for managing Book entries.
5:function.py: Contains the functions for menu operations.
6:__init__.py: Initializes the database connection and cursor.


#CLASSES AND METHODS

Bible Class

Attributes:
id
testament
category


#METHODS

1:create_table(): Creates the bibles table.
2:drop_table(): Drops the bibles table.
3:save(): Saves the Bible instance to the database.
4:create(testament, category): Creates a new Bible instance and saves it to the database.
5:update(): Updates the Bible instance in the database.
6:delete(): Deletes the Bible instance from the database.
7:instance_from_db(row): Returns a Bible object from a database row.
8:get_all(): Returns all Bible instances from the database.
9:find_by_id(id): Finds a Bible by its ID.
10:find_by_name(name): Finds a Bible by its name.


#BOOK CLASS
ATTRIBUTES

id
name
bible_id

#METHODS

1:create_table(): Creates the books table.
2:drop_table(): Drops the books table.
3:save(): Saves the Book instance to the database.
4:create(name, bible_id): Creates a new Book instance and saves it to the database.
5:update(): Updates the Book instance in the database.
6:delete(): Deletes the Book instance from the database.
7:instance_from_db(row): Returns a Book object from a database row.
8:get_all(): Returns all Book instances from the database.
9:find_by_id(id): Finds a Book by its ID.
10:find_by_name(name): Finds a Book by its name.

#DATABASE SCHEMA

BIBLES TABLE
id: INTEGER PRIMARY KEY
testament: TEXT
category: TEXT

BOOKS TABLE
id: INTEGER PRIMARY KEY
name: TEXT
bible_id: INTEGER, FOREIGN KEY referencing bibles(id)
Seeding the Database
The seed.py script initializes the database with the following data:

BIBLES:

Old Testament: Law, Prophets, Wisdom, History
New Testament: Gospels, Epistles

BOOKS:

Genesis, Exodus (Law)
Isaiah, Jeremiah (Prophets)
Psalms (Wisdom)
Joshua, Judges (History)
Matthew, Mark, Luke, John (Gospels)
Romans, 1 Corinthians, 2 Corinthians (Epistles)

#LICENSE
This project is licensed under the MIT License. See the LICENSE file for details.

#ACKNOWLEDGEMENTS

Moringa School for providing the learning platform and resources.
The SQLite and Python communities for their invaluable tools and documentation.

#CONTRIBUTING

Contributions are welcome! Please fork the repository and submit a pull request for review.

#CONTACT
For any questions or suggestions, please contact [tony.kamande@student.moringaschool.com].

This README provides a comprehensive overview of the project, installation steps, usage instructions, and additional details for developers and contributors. 



