# The Repository
import atexit
import sqlite3

from DAO import Hats, Suppliers, Orders

class _Repository:
    def __init__(self):
        self.conn = sqlite3.connect('true_database.db')
        self.hats = Hats(self.conn)
        self.suppliers = Suppliers(self.conn)
        self.orders = Orders(self.conn)

    def _close(self):
        self.conn.commit()
        self.conn.close()

    def create_tables(self):
        self.conn.executescript("""
        CREATE TABLE hats (
            id       INTEGER       PRIMARY KEY,
            topping    TEXT        NOT NULL,
            supplier INTEGER       NOT NULL,
            quantity INTEGER       NOT NULL ,
            
            FOREIGN KEY(supplier) REFERENCES suppliers(id)  
        );
        
        CREATE TABLE suppliers (
            id       INTEGER     PRIMARY KEY,
            name     TEXT        NOT NULL
        );

        CREATE TABLE orders (
            id        INTEGER     PRIMARY KEY,
            location  TEXT        NOT NULL,
            hat       INTEGER     NOT NULL,

            FOREIGN KEY(hat)     REFERENCES hats(id)
        );
    """)

    def make_output(self):
        self.conn.execute("""
            SELECT hats_backup.topping, suppliers.name, orders.location
            FROM orders join hats_backup join suppliers
            ON hats_backup.supplier = suppliers.id AND hats_backup.id = orders.hat
        """)


# the repository singleton
repo = _Repository()
atexit.register(repo._close)