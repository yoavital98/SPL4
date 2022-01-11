# Data Access Objects:
# All of these are meant to be singletons
from DTO import Hat, Supplier, Order

class Hats:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, hat_dto):
        self.conn.execute("""
               INSERT INTO hats (id, topping, supplier, quantity) VALUES (?, ?, ?, ?)
           """, [hat_dto.id, hat_dto.topping, hat_dto.supplier, hat_dto.quantity])

    def find_first(self, _topping):
        c = self.conn.cursor()
        c.execute("""
                    SELECT id, quantity, supplier FROM hats WHERE topping = ? ORDER BY supplier
                """, [_topping])
        return c.fetchone()

    def delete_hat(self, hat_id):
        c = self.conn.cursor()
        c.execute("""
                        DELETE from hats WHERE id = ?
                        """, [hat_id])

    def dispose_hat(self, hat):
        self.conn.execute("""
                UPDATE hats SET quantity = ? WHERE id = ?
                """, [hat[1]-1, hat[0]])
        if hat[1]-1 == 0:
            self.delete_hat(hat[0])

    def delete_table(self):
        c = self.conn.cursor()
        c.execute(""" DELETE FROM hats """)

class Suppliers:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, supplier_dto):
        self.conn.execute("""
                INSERT INTO suppliers (id, name) VALUES (?, ?)
        """, [supplier_dto.id, supplier_dto.name])

    def find_supplier(self, supplier_id):
        c = self.conn.cursor()
        c.execute("""
                        SELECT name from suppliers WHERE id= ?
                """, [supplier_id])
        return c.fetchone()

    def delete_table(self):
        c = self.conn.cursor()
        c.execute(""" DELETE FROM suppliers """)

class Orders:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, order_dto):
        self.conn.execute("""
            INSERT INTO orders (id, location, hat) VALUES (?, ?, ?)
        """, [order_dto.id, order_dto.location, order_dto.hat])

    def delete_table(self):
        c = self.conn.cursor()
        c.execute(""" DELETE FROM orders """)
