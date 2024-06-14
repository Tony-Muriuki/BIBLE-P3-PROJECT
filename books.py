from __init__ import CURSOR, CONN
from bible import Bible  # Ensure this matches the filename of your Bible class

class Books:
    all = {}

    def __init__(self, name, bible_id, id=None):
        self.id = id
        self.name = name
        self.bible_id = bible_id

    def __repr__(self):
        return f"<Book {self.id}: {self.name} BIBLE ID: {self.bible_id}>"

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Book instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                name TEXT,
                bible_id INTEGER,
                FOREIGN KEY (bible_id) REFERENCES bibles(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Book instances"""
        sql = """
            DROP TABLE IF EXISTS books;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the name value of the current Book object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO books (name, bible_id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.bible_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Book instance."""
        sql = """
            UPDATE books
            SET name = ?, bible_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.bible_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Book instance,
        delete the dictionary entry, and reassign id attribute"""
        sql = """
            DELETE FROM books
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name, bible_id):
        """Initialize a new Book instance and save the object to the database"""
        book = cls(name, bible_id)
        book.save()
        return book

    @classmethod
    def instance_from_db(cls, row):
        """Return a Book object having the attribute values from the table row."""
        # Check the dictionary for existing instance using the row's primary key
        book = cls.all.get(row[0])
        if book:
            # Ensure attributes match row values in case local instance was modified
            book.name = row[1]
            book.bible_id = row[2]
        else:
            # Not in dictionary, create new instance and add to dictionary
            book = cls(row[1], row[2])
            book.id = row[0]
            cls.all[book.id] = book
        return book

    @classmethod
    def get_all(cls):
        """Return a list containing one Book object per table row"""
        sql = """
            SELECT *
            FROM books
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Book object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM books
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return Book object corresponding to the first table row matching the specified name"""
        sql = """
            SELECT *
            FROM books
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
