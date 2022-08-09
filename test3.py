import sqlite3

conn = sqlite3.connect("finance1.db")
cur = conn.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    username TEXT NOT NULL, 
    hash TEXT NOT NULL, 
    cash NUMERIC NOT NULL DEFAULT 10000.00)
    ;
""")
conn.commit()

#cur.execute(""" CREATE TABLE sqlite_sequence(name,seq);""")
#conn.commit()

#cur.execute(""" CREATE UNIQUE INDEX username ON users (username);""")
#conn.commit()

cur.execute(""" CREATE TABLE IF NOT EXISTS history (
    id INTEGER NOT NULL, 
    user_id_hst INTEGER NOT NULL, 
    symbol_hst TEXT NOT NULL, 
    name_hst TEXT, 
    shares_hst INTEGER NOT NULL, 
    price_hst INTEGER NOT NULL, 
    date TEXT NOT NULL, 
    type text, 
    PRIMARY KEY(id), 
    FOREIGN KEY(user_id_hst) REFERENCES users(id));
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS portfolio(
    id INTEGER,
    user_id INTEGER NOT NULL,
    symbol_prt TEXT NOT NULL,
    name_prt TEXT,
    shares_prt INTEGER NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(user_id) REFERENCES users(id));
""")  
conn.commit()

#cur.execute("""INSERT INTO users(username, hash) VALUES('Mike', 'rfrf');""")
#conn.commit()
cur.execute("""SELECT * FROM users;""")
cash = cur.fetchone()
print(cash)