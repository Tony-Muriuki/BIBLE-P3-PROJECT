import sqlite3

CONN=sqlite3.connection('heaven.db')
CURSOR=CONN.execute()