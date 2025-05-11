import sqlite3

con = sqlite3.connect('ibex.db')

cursor = con.cursor()
sql = """CREATE TABLE cliente (      
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            senha VARCHAR(50) NOT NULL,
            login VARCHAR(100) UNIQUE
        );"""

cursor.execute(sql)
con.commit()
con.close()
