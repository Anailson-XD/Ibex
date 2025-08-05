import sqlite3

def criar_tabelas():
    con = sqlite3.connect('ibex.db')
    cursor = con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Tabela empresa
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empresa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            senha VARCHAR(50) NOT NULL,
            login VARCHAR(100) UNIQUE NOT NULL,
            cnpj TEXT NOT NULL
        );
    ''')

    # Tabela cliente
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            senha VARCHAR(50) NOT NULL,
            login VARCHAR(100) UNIQUE NOT NULL
        );
    ''')

    # Tabela produtos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            descricao VARCHAR(100) NOT NULL,
            preco REAL NOT NULL,
            quantidade FLOAT NOT NULL,
            categoria VARCHAR(100) NOT NULL,
            empresa_id INTEGER NOT NULL,
            FOREIGN KEY (empresa_id) REFERENCES empresa(id)
        );
    ''')

    # Tabela carrinho
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carrinho (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER NOT NULL,
            id_produto INTEGER NOT NULL,
            nome_produto TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco_unitario REAL NOT NULL,
            id_empresa INTEGER NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES cliente(id),
            FOREIGN KEY (id_produto) REFERENCES produtos(id),
            FOREIGN KEY (id_empresa) REFERENCES empresa(id)
        );
    ''')

    # Tabela carrinho Temporario
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carrinho_temp (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER NOT NULL,
            id_produto INTEGER NOT NULL,
            nome_produto TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco_unitario REAL NOT NULL,
            id_empresa INTEGER NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES cliente(id),
            FOREIGN KEY (id_produto) REFERENCES produtos(id),
            FOREIGN KEY (id_empresa) REFERENCES empresa(id)
        );
    ''')

    # Tabela colaboradores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS colaboradores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            numero INTEGER NOT NULL,
            funcao TEXT NOT NULL,
            login TEXT NOT NULL,
            senha VARCHAR(50) NOT NULL
        );
    ''')

    # Tabela pedidos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            descricao TEXT NOT NULL,
            status TEXT NOT NULL,
            colaborador TEXT,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        );
    ''')

    con.commit()
    con.close()
    print("Tabelas criadas com sucesso.")

criar_tabelas()
