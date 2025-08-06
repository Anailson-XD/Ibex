from utilitarios import *
from login import *
import sqlite3


def listar_pedidos_pendentes():
    con = sqlite3.connect('ibex.db')
    cursor = con.cursor()

    cursor.execute('''
        SELECT pedidos.id, cliente.nome, pedidos.descricao
        FROM pedidos
        JOIN cliente ON pedidos.cliente_id = cliente.id
        WHERE pedidos.status = "pendente"
    ''')

    pedidos = cursor.fetchall()
    con.close()

    if not pedidos:
        print('Nenhum pedido pendente.')
        return

    print('\nPedidos pendentes:')
    for id, nome_cliente, descricao in pedidos:
        print(f'ID: {id} | Cliente: {nome_cliente} | Descrição: {descricao}')

def aceitar_pedido():
    id_pedido = int(input('Digite o ID do pedido que deseja aceitar: '))
    con = sqlite3.connect('ibex.db')
    cursor = con.cursor()

    cursor.execute('SELECT * FROM pedidos WHERE id = ? AND status = "pendente"', (id_pedido,))
    if cursor.fetchone() is None:
        print('Pedido não encontrado ou já aceito.')
    else:
        cursor.execute('''
            UPDATE pedidos
            SET status = "aceito", colaborador = ?
            WHERE id = ?
        ''', (colaborador_logado, id_pedido))
        con.commit()
        print('Pedido aceito com sucesso!')

    con.close()

def ver_meus_pedidos():
    con = sqlite3.connect('ibex.db')
    cursor = con.cursor()

    cursor.execute('''
        SELECT pedidos.id, cliente.nome, pedidos.descricao, pedidos.status
        FROM pedidos
        JOIN cliente ON pedidos.cliente_id = cliente.id
        WHERE colaborador = ?
    ''', (colaborador_logado,))

    pedidos = cursor.fetchall()
    con.close()

    if not pedidos:
        print('Você ainda não aceitou nenhum pedido.')
        return

    print('\nMeus pedidos:')
    for id, nome_cliente, descricao, status in pedidos:
        print(f'ID: {id} | Cliente: {nome_cliente} | Descrição: {descricao} | Status: {status}')

def concluir_pedido():
    id_pedido = int(input('Digite o ID do pedido que deseja marcar como concluído: '))
    con = sqlite3.connect('ibex.db')
    cursor = con.cursor()

    cursor.execute('''
        SELECT * FROM pedidos
        WHERE id = ? AND colaborador_login = ? AND status = "aceito"
    ''', (id_pedido, colaborador_logado))

    if cursor.fetchone() is None:
        print('Pedido não encontrado ou não está em andamento.')
    else:
        cursor.execute('''
            UPDATE pedidos
            SET status = "concluído"
            WHERE id = ?
        ''', (id_pedido,))
        con.commit()
        print('Pedido marcado como concluído.')

    con.close()