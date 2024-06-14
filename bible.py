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
        """Create a new table to persist the attributes of Bible instances"""
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
        """Drop the table that persists Bible instances"""
        sql = """
            DROP TABLE IF EXISTS bibles;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the testament and category values of the current Bible instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
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
        """Initialize a new Bible instance and save the object to the database"""
        bible = cls(testament, category)
        bible.save()
        return bible

    def update(self):
        """Update the table row corresponding to the current Bible instance."""
        sql = """
            UPDATE bibles
            SET testament = ?, category = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.testament, self.category, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Bible instance,
        delete the dictionary entry, and reassign id attribute"""
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
        """Return a Bible object having the attribute values from the table row."""
        # Checks the dictionary for an existing instance using the row's primary key
        bible = cls.all.get(row[0])
        if bible:
            # Ensure attributes match row values in case local instance was modified
            bible.testament = row[1]
            bible.category = row[2]
        else:
            # Not in dictionary, create new instance and add to dictionary
            bible = cls(row[1], row[2])
            bible.id = row[0]
            cls.all[bible.id] = bible
        return bible

    @classmethod
    def get_all(cls):
        """Return a list containing a Bible object per row in the table"""
        sql = """
            SELECT *
            FROM bibles
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Returns a Bible object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM bibles
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_testament(cls, testament):
        """Returns a Bible object corresponding to the first table row matching specified testament"""
        sql = """
            SELECT *
            FROM bibles
            WHERE testament = ?
        """
        row = CURSOR.execute(sql, (testament,)).fetchone()
        return cls.instance_from_db(row) if row else None
