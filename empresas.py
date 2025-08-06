from utilitarios import *
import sqlite3
import time

def cad_produto():
    global empresa_logada
    exibir_subtitulo('Cadastre seu produto')
    if empresa_logada is None:
        print('Erro: Nenhuma empresa está logada!')
        return
    nome = input('Nome do produto:')
    descricao = input('Marca:')
    preco = float(input('Preço: R$ '))
    quantidade = float(input('Qual quantidade:'))
    categoria = input('Tipo do produto:')
    con = sqlite3.connect('ibex.db')
    cursor = con.cursor()
    cursor.execute("SELECT id FROM empresa WHERE login = ?", (empresa_logada,))
    empresa_id = cursor.fetchone()[0]
    sql = 'INSERT INTO produtos (nome, descricao, preco, quantidade, categoria, empresa_id) VALUES (?,?,?,?,?,?)'
    cursor.execute(sql, (nome, descricao, preco, quantidade, categoria, empresa_id))
    con.commit()
    con.close()
    print('Redirecionando...\n')
    time.sleep(1)
    print('PRODUTO CADASTRADO COM SUCESSO!\n')
    input("Pressione ENTER para continuar...")

def listar_produtos():
    exibir_subtitulo('Produtos cadastrados')
    con = sqlite3.connect('ibex.db')
    cursor = con.cursor()
    cursor.execute('SELECT nome, descricao, preco, quantidade, categoria FROM produtos ')
    produtos = cursor.fetchall()
    con.close()
    if produtos:
        for p in produtos:
            print('------------------------')
            print(f'Nome:{p[0]}')
            print(f'Descrição:{p[1]}')
            print(f'Preço:{p[2]}')
            print(f'Quantidade:{p[3]}')
            print(f'Categoria:{p[4]}')
            print()
            time.sleep(1)
    else:
        print('Nenhum Produto encontrado\n')
    input("Pressione ENTER para continuar...")

