from __init__ import CURSOR, CONN

class Bible:
    all = {}

    def __init__(self, testament, category, id=None):
        self.id = id
        self.testament = testament
        self.category = category

    def __repr__(self):
        return f"<Bible {self.id}: {self.testament}, {self.category}>"

    @classmethod
    def create_table(cls):
        """CREATES A NEW TABLE TO PERSIST THE ATTRIBUTES OF BIBLE INSTANCES"""
        sql = """
            CREATE TABLE IF NOT EXISTS bibles (
                id INTEGER PRIMARY KEY,
                testament TEXT,
                category TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """DROP THE TABLE THAT PERSISTS BIBLE INSTANCES"""
        sql = """
            DROP TABLE IF EXISTS bibles;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """INSERT A NEW ROW WITH THE TESTAMENT AND CATEGORY VALUES OF THE CURRENT BIBLE INSTANCE.
        UPDATE OBJECT ID ATTRIBUTE USING THE PRIMARY KEY VALUE OF NEW ROW.
        SAVE THE OBJECT IN LOCAL DICTIONARY USING  TABLE ROW's PRIMARY KEY AS DICTIONARY KEY"""
        sql = """
            INSERT INTO bibles (testament, category)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.testament, self.category))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, testament, category):
        """INITIALIZE A NEW BIBLE INSTANCE AND SAVE THE OBJECT TO  THE DATABASE"""
        bible = cls(testament, category)
        bible.save()
        return bible

    def update(self):
        """UPDATE THE TABLE ROW CORRESPONDINNG TO THE CURRENT BIBLE INSTANCE."""
        sql = """
            UPDATE bibles
            SET testament = ?, category = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.testament, self.category, self.id))
        CONN.commit()

    def delete(self):
        """DELETE THE TABLE ROW CORRESPODING TO THE CURRENT BIBLE INSTANCE,
        DELETE THE DICTIONARY ENTRY, AND REASSIGN ID ATTRIBUTE"""
        sql = """
            DELETE FROM bibles
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """RETURN A BIBLE OBJECT HAVING THE ATTRIBUTE VALUES FROM THE TABLE ROW."""
        # Checks the dictionary for an existing instance using the row's primary key
        bible = cls.all.get(row[0])
        if bible:
            # Ensure attributes match row values in case local instance was modified
            bible.testament = row[1]
            bible.category = row[2]
        else:
            # IF Not in dictionary, create new instance and add to dictionary
            bible = cls(row[1], row[2])
            bible.id = row[0]
            cls.all[bible.id] = bible
        return bible

    @classmethod
    def get_all(cls):
        """RETURN A LIST CONTAINING A BIBLE OBJECT PER ROW IN THE TABLE"""
        sql = """
            SELECT *
            FROM bibles
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """RETURNS A BIBLE OBJECT CORRESPONDING TO THE TABLE ROW MATCHING THE SPECIFIED PRIMARY KEY"""
        sql = """
            SELECT *
            FROM bibles
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_testament(cls, testament):
        """RETURNS A BIBLE OBJECT CORRESPONDING TO THE FIRST TABLE ROW MATCHING SPECIFIED TESTAMENT"""
        sql = """
            SELECT *
            FROM bibles
            WHERE testament = ?
        """
        row = CURSOR.execute(sql, (testament,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    
    
    def books(self):
        """Return a list of Book objects associated with this Bible instance."""
        from books import Book
        sql = """
            SELECT *
            FROM books
            WHERE bible_id = ?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Book.instance_from_db(row) for row in rows]