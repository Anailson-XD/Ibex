import sqlite3

con = sqlite3.connect('ibex.db')

cursor = con.cursor()
sql = """CREATE TABLE produtos (      
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            marca VARCHAR(50) NOT NULL,
            preco REAIS,
            quantidade int,
            categoria VARCHAR(100)
        );"""

cursor.execute(sql)
con.commit()
con.close()
