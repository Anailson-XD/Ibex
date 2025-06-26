# mostrar os produtos disponoveis
def ver_produtos():
    exibir_subtitulo('Produtos disponíveis')
    con = sqlite3.connect('ibex.db')
    cursor = con.cursor()
    cursor.execute('SELECT nome, descricao, preco, quantidade, categoria FROM produtos ')
    produtos = cursor.fetchall()
    con.close()
    if produtos:
        for p in produtos:
            print('------------------------')
            print(f'Nome:{p[0]}')
            print(f'Marca:{p[1]}')
            print(f'Preço:{p[2]}')
            print(f'Quantidade:{p[3]}')
            print(f'Categoria:{p[4]}')
            print('------------------------\n')
            time.sleep(1)
    else:
        print('Nenhum Produto encontrado\n')
        input("Pressione ENTER para continuar...")

# Encontrar produto pesquisado pelo cliente
def busca_produto():
    exibir_subtitulo('Encontre o produto desejado')
    busca = input('Digite o nome ou categoria do produtos:')
    con = sqlite3.connect("ibex.db")
    cursor = con.cursor()
    sql = """SELECT nome, descricao, preco, quantidade, categoria FROM produtos WHERE nome LIKE ? OR categoria LIKE ?"""
    cursor.execute(sql,(f'%{busca}%',f'%{busca}%'))
    resultado = cursor.fetchall()
    if resultado:
        for produto in resultado:
            print('------------------------')
            print(f'Nome:{produto[0]}')
            print(f'Marca:{produto[1]}')
            print(f'Preço:{produto[2]}')
            print(f'Quantidade:{produto[3]}')
            print(f'Categoria:{produto[4]}')
            print('------------------------\n')
            time.sleep(1)
    else:
        print('Nenhum produto encontrado')
    con.close()
    input("Pressione ENTER para continuar...")

# Mostrar empresas cadastradas
def ver_empresas():
    exibir_subtitulo('Empresas cadastradas')
    con = sqlite3.connect("ibex.db")
    cursor = con.cursor()
    cursor.execute('SELECT nome, login, cnpj FROM empresa')
    empresas = cursor.fetchall()
    if empresas:
        for empresa in empresas:
            print(f'Nome:{empresa[0]}')
            print(f'Email:{empresa[1]}')
            print(f'CNPJ:{empresa[2]}')
            print('------------------------\n')
            time.sleep(1)
    else:
        print('Nenhuma empresa encontrada')
    con.close()
    input("Pressione ENTER para continuar...")

# Atualizar dados dos clientes
def atualizar_cliente():
    global cliente_logado
    if cliente_logado is None:
        print("Você precisa estar logado para atualizar seus dados.")
        input("Pressione ENTER para voltar...")
        return
    exibir_nome()
    exibir_subtitulo('Atualize seus dados')
    con = sqlite3.connect("ibex.db")
    cursor = con.cursor()
    cursor.execute('SELECT nome FROM cliente WHERE login = ?', (cliente_logado,))
    resultado = cursor.fetchone()
    if resultado:
        print(f'\nBem-vindo, {resultado[0]}')
        print('O que deseja atualizar?')
        print('1. Nome')
        print('2. E-mail')
        print('3. Senha')
        print('4. Voltar')
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            novo_nome = input('Novo nome: ')
            cursor.execute('UPDATE cliente SET nome = ? WHERE login = ?', (novo_nome, cliente_logado))
        elif opcao == 2:
            novo_email = input('Novo e-mail: ')
            cursor.execute('UPDATE cliente SET login = ? WHERE login = ?', (novo_email, cliente_logado))
            cliente_logado = novo_email  
        elif opcao == 3:
            nova_senha = input('Nova senha: ')
            cursor.execute('UPDATE cliente SET senha = ? WHERE login = ?', (nova_senha, cliente_logado))
        elif opcao == 4:
            con.close()
            return
        else:
            print('Opção inválida!')
            con.close()
            return

        con.commit()
        print('Redirecionando...\n')
        time.sleep(1)
        print('\nDados atualizados com sucesso!')

    else:
        print('\nErro: cliente não encontrado.')

    con.close()
    input("Pressione ENTER para continuar...")

class HistoricoPedidos:
    def __init__(self, cliente_login, db_path="ibex.db"):
        self.cliente_login = cliente_login
        self.db_path = db_path
        self.cliente_id = self._buscar_id_cliente()

    def _buscar_id_cliente(self):
        con = sqlite3.connect(self.db_path)
        cursor = con.cursor()
        cursor.execute("SELECT id FROM cliente WHERE login = ?", (self.cliente_login,))
        resultado = cursor.fetchone()
        con.close()
        return resultado[0] if resultado else None

    def obter_pedidos(self):
        if not self.cliente_id:
            return []

        con = sqlite3.connect(self.db_path)
        cursor = con.cursor()
        cursor.execute("""
            SELECT nome_produto, quantidade, preco_unitario, id_empresa
            FROM carrinho
            WHERE id_cliente = ?
        """, (self.cliente_id,))
        pedidos = cursor.fetchall()
        con.close()
        return pedidos
    
# pedidos anteriores dos clientes
def historico_pedidos():
    global cliente_logado
    exibir_subtitulo('Histórico de pedidos: ')

    if not cliente_logado:
        print("Você precisa estar logado como cliente para ver os pedidos.")
        input("Pressione ENTER para continuar...")
        return

    historico = HistoricoPedidos(cliente_logado)
    pedidos = historico.obter_pedidos()

    if not pedidos:
        print("Nenhum pedido encontrado.")
    else:
        for idx, (nome, qtd, preco, empresa_id) in enumerate(pedidos, start=1):
            print(f"{idx}. Produto: {nome}")
            print(f"   Quantidade: {qtd}")
            print(f"   Preço unitário: R${preco:.2f}")
            print(f"   ID da empresa: {empresa_id}")
            print("---------------------------")

    input("Pressione ENTER para continuar...")

# mostrar pedidos feito aos colaboradores
def ver_pedidos_cliente():
    con = sqlite3.connect('ibex.db')
    cursor = con.cursor()
    cursor.execute('SELECT id FROM clientes WHERE login = ?', (cliente_logado,))
    resultado = cursor.fetchone()

    if resultado:
        cliente_id = resultado[0]

        cursor.execute('''
            SELECT id, descricao, status, colaborador_login
            FROM pedidos
            WHERE cliente_id = ?
        ''', (cliente_id,))
        pedidos = cursor.fetchall()

        if not pedidos:
            print('Você ainda não fez nenhum pedido.')
        else:
            print('\nSeus pedidos:')
            for id, descricao, status, colaborador in pedidos:
                print(f'ID: {id} | Descrição: {descricao} | Status: {status} | Colaborador: {colaborador if colaborador else "Aguardando"}')
    else:
        print('Erro ao localizar cliente.')

    con.close()