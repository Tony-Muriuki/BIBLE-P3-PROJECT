from __init__ import CURSOR, CONN
from bible import Bible  

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
        """CREATES A NEW TABLE TO PERSIST THE ATTRIBUTES OF BOOK INSTANCES"""
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
        """DROPS THE TABLE THAT PERSISTS BOOK INSTANCES"""
        sql = """
            DROP TABLE IF EXISTS books;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """INSERTS A NEW ROW WITH THE NAME VALUES OF THE CURRENT BOOK OBJECT.
        UPDTAES OBJECT ID ATTRIBUTE USING THE PRIMARY KEY VALUE OF NEW ROW.
        SAVES THE OBJECT IN LOCAL DICTIONARY USING TABLES ROW'S PRIMARY KEY AS DICT KEY"""
        sql = """
            INSERT INTO books (name, bible_id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.bible_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """UPDATES THE TABLE ROW CORRESPONDING TO THE CURRENT BOOK INSTANCE."""
        sql = """
            UPDATE books
            SET name = ?, bible_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.bible_id, self.id))
        CONN.commit()

    def delete(self):
        """DELETS THE TABLE ROW CORRESPONDING TO THE CURRENT BOOK INSTANCE,
        DELETE THE DICTIONARY ENTRY, AND REASSIGN ID ATTRIBUTE"""
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
        """INITIALIZE A NEW BOOK INSTANCE AND SAVE THE OBJECT TO THE DATABASE"""
        book = cls(name, bible_id)
        book.save()
        return book

    @classmethod
    def instance_from_db(cls, row):
        """RETURN A BOOK OBJECT HAVING THE ATTRIBUTE VALUES FROM THE TABLE ROW."""
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
        """RETURN A LIST CONTAINING ONE BOOK OBJECT PER TABLE ROW"""
        sql = """
            SELECT *
            FROM books
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """RETURN BOOK OBJECT CORRESPONDING TO THE TABLE ROW MATCHING THE SPECIFIED PRIMARY KEY"""
        sql = """
            SELECT *
            FROM books
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """RETURN BOOK OBJECT CORRESPONDING TO THE FIRST TABLE ROW MATCHING THE SPECIFIED NAME"""
        sql = """
            SELECT *
            FROM books
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
