import sqlite3

con = sqlite3.connect('ibex.db')

cursor = con.cursor()
sql = '''CREATE TABLE carrinho (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    id_produto INTEGER,
    nome_produto TEXT,
    quantidade INTEGER,
    preco_unitario REAL,
    id_empresa INTEGER,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id),
    FOREIGN KEY (id_produto) REFERENCES produto(id)
);'''

cursor.execute(sql)
con.commit()
con.close()
