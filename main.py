from __init__ import CURSOR, CONN

class Bible:

    def __init__(self, testament, category, id=None):
        self.id = id
        self.testament = testament
        self.category = category

    def __repr__(self):
        return f"<Bible {self.id}: {self.testament}, {self.category}>"
    
    @classmethod
    def create_table(cls):
        """ CREATES A NEW TABLE TO PERSIST THE ATTRIBUTES OF BIBLE INSTANCES """
        sql = """
            CREATE TABLE IF NOT EXISTS bibles (
            id INTEGER PRIMARY KEY,
            testament TEXT,
            category TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
        
        
    @classmethod
    def drop_table(cls):
        """ DROPS THE TABLE THAT PERSISTS BIBLE instances """
        sql = """
            DROP TABLE IF EXISTS bibles;
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    