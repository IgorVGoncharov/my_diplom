import sqlite3

db = sqlite3.connect('./banks_data_base.db')
sql = db.cursor()
sql.execute('''CREATE TABLE IF NOT EXISTS products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
company TEXT NOT NULL,
items_count INTEGER DEFAULT 0,
price INTEGER)
''')
db.commit()
sql.execute('''CREATE TABLE IF NOT EXISTS customers (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL)
''')
db.commit()
sql.execute('''CREATE TABLE IF NOT EXISTS orders (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_id INTEGER NOT NULL,
customer_id INTEGER NOT NULL,
created_at TEXT NOT NULL,
items_count INTEGER DEFAULT 1,
price INTEGER NOT NULL,
FOREIGN KEY (product_id) REFERENCES products(id),
FOREIGN KEY (customer_id) REFERENCES customers(id))
''')
db.commit()
sql.execute("""INSERT INTO products (name, company, items_count, price)
VALUES
('iPhone 13', 'Apple', 3, 76000),
('iPhone 12', 'Apple', 2, 51000),
('Galaxy S21', 'Samsung', 2, 56000),
('Galaxy S20', 'Samsung', 1, 41000),
('P40 Pro', 'Huawei', 5, 36000)
""")
db.commit()
sql.execute("""INSERT INTO customers(name) VALUES ('Tom'), ('Bob'),('Sam')
""")
db.commit()
sql.execute("""INSERT INTO orders (product_id, customer_id, created_at, items_count, price)
VALUES
( 
    (SELECT id FROM products WHERE name='Galaxy S21'),
    (SELECT id FROM customers WHERE name='Tom'),
    '2021-11-30', 
    2, 
    (SELECT price FROM products WHERE name='Galaxy S21')
),
( 
    (SELECT id FROM products WHERE name='iPhone 12'),
    (SELECT id FROM customers WHERE name='Tom'),
    '2021-11-29',  
    1, 
    (SELECT price FROM products WHERE name='iPhone 12')
),
( 
    (SELECT id FROM products WHERE name='iPhone 12'),
    (SELECT id FROM customers WHERE name='Bob'),
    '2021-11-29',  
    1, 
    (SELECT price FROM products WHERE name='iPhone 12')
)
""")
db.commit()
sql.execute("""SELECT C.name, P.name, O.created_at 
FROM orders AS O, customers AS C, products AS P
WHERE O.customer_id = C.id AND O.product_id=P.id
""")
db.commit()
resuilt = sql.fetchall()
print(resuilt)
db.close()
