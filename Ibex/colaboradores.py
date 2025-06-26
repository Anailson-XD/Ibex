def listar_pedidos_pendentes():
    con = sqlite3.connect('ibex.db')
    cursor = con.cursor()

    cursor.execute('''
        SELECT pedidos.id, clientes.nome, pedidos.descricao
        FROM pedidos
        JOIN clientes ON pedidos.cliente_id = clientes.id
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

def solicitar_servicos():
    global cliente_logado
    if cliente_logado is None:
        print("Você precisa estar logado para atualizar seus dados.")
        input("Pressione ENTER para voltar...")
        return
    
    opcao = 0
    while opcao != 9:
        exibir_subtitulo('Solicitação de Serviços')
        print('1. Criar novo pedido')
        print('2. Ver meus pedidos')
        print('9. Sair')

        try:
            opcao = int(input('Escolha uma opção: '))
        except ValueError:
            print('Opção inválida! Digite um número.')
            continue

        if opcao == 1:
            criar_pedido()
        elif opcao == 2:
            ver_pedidos_cliente()
        elif opcao == 9:
            print('Saindo do menu de serviços...')
        else:
            print('Opção inválida.')

        input('\nPressione ENTER para continuar...')

def criar_pedido():
    descricao = input('Descreva o serviço que você precisa: ')

    con = sqlite3.connect('ibex.db')
    cursor = con.cursor()

    cursor.execute('SELECT id FROM clientes WHERE login = ?', (cliente_logado,))
    resultado = cursor.fetchone()

    if resultado:
        cliente_id = resultado[0]
        cursor.execute('''
            INSERT INTO pedidos (cliente_id, descricao)
            VALUES (?, ?)
        ''', (cliente_id, descricao))
        con.commit()
        print('Pedido criado com sucesso!')
    else:
        print('Erro: cliente não encontrado.')

    con.close()
