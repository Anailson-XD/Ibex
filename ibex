import os
import sqlite3
import time
import requests

empresa_logada = None
cliente_logado = None
favoritos = {}

# 1
def exibir_nome():
    print('#################################')
    print('Ｂｅｍ ｖｉｎｄｏ ａｏ Ｉｂｅｘ！')
    print('#################################')

# 2
def cabecalho_carrinho():
    print('########################')
    print('🛒 CARRINHO DE COMPRAS')
    print('########################')

# 3
def menu_principal():
    limpa_tela()
    exibir_nome()
    print('1. Cadastre-se')
    print('2. Login ')
    print('3. Cadastrar Empresa')
    print('4. Login Empresa')
    print('9. Sair')

 # 4
def menu_empresa():
    opcao = 0
    while opcao != 4:
        limpa_tela()
        exibir_nome()
        print('Menu da empresa')
        print('1. Cadastrar produtos')
        print('2. Ver produtos')
        print('3. Relatório')
        print('4. Sair')
        opcao = int(input('Escolha uma opção:'))
        if opcao == 1:
            cad_produto()
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            gerar_relatorio()
        elif opcao not in [1, 2, 3, 4]:
            print('Opção inválida!')
            input("Pressione ENTER para continuar...")


# 5   
def menu_cliente():
    opcao = 0
    while opcao != 9:
        limpa_tela()
        exibir_nome()
        print('Menu Cliente\n')
        print('1. Ver Produtos disponiveis')
        print('2. Buscar produtos')
        print('3. Ver empresas cadastradas')
        print('4. Atualizar dados')
        print('5. Carrinho')
        print('9. Sair')
        opcao = int(input("Opcao:"))
        if opcao == 1:
            ver_produtos()
        elif opcao == 2:
            busca_produto()
        elif opcao == 3:
            ver_empresas()
        elif opcao == 4:
            atualizar_cliente()
        elif opcao == 5:
            menu_carrinho()
        elif opcao not in [1, 2, 3, 4, 5, 9]:
            print('Opção inválida!')
            input("Pressione ENTER para continuar...")


# 6
def menu_carrinho():
    opcao = 0
    while opcao != 9:
        limpa_tela()
        cabecalho_carrinho()
        print('Digite uma opção abaixo:\n')
        print('1. Adicionar produto ao carrinho')
        print('2. Ver Carrinho')
        print('3. Remover produto do Carrinho')
        print('4. Editar produto do Carrinho')
        print('5. Finalizar pedido')
        print('9. Sair')
        opcao = int(input("Opcao:"))
        if opcao == 1:
            adicionar_carrinho()
        elif opcao == 2:
            ver_carrinho()
        elif opcao == 3:
            remover_carrinho()
        elif opcao == 4:
            print('Em breve')
        elif opcao == 5:
            finalizar_pedido()
        elif opcao not in [1, 2, 3, 4, 5, 9]:
            print('Opção inválida!')
            input("Pressione ENTER para continuar...")
            
# 7
def listar_produtos():
    limpa_tela()
    exibir_nome()
    print('Produtos Cadastrados\n')
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
# 8
def ver_produtos():
    limpa_tela()
    exibir_nome()
    print('Produtos disponiveis\n')
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
# 9
def busca_produto():
    limpa_tela()
    exibir_nome()
    print('Encontre o produto desejado\n')
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
# 10
def ver_empresas():
    limpa_tela()
    exibir_nome()
    print('Empresas cadastradas\n')
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
    
# 11
def atualizar_cliente():
    global cliente_logado
    if cliente_logado is None:
        print("Você precisa estar logado para atualizar seus dados.")
        input("Pressione ENTER para voltar...")
        return

    limpa_tela()
    exibir_nome()
    print('Atualizar dados\n')
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

# 12
def limpa_tela():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

# 13
def finalizando_app():
    os.system('cls')
    print('Saindo do app!\n')

# 14
def cad_empresa():
    limpa_tela()
    exibir_nome()
    print('Cadastre sua Empresa!')
    nome = input('Nome:')
    senha = input('Crie uma Senha:')
    login = input('E-mail:')
    cnpj = input('CNPJ:')
    con = sqlite3.connect("ibex.db")
    cursor = con.cursor()
    sql = "INSERT INTO empresa (nome, senha, login, cnpj) VALUES (?, ?, ?, ?)"
    cursor.execute(sql, (nome, senha, login, cnpj))
    con.commit()
    con.close()
    print('Redirecionando...\n')
    time.sleep(1)
    print('EMPRESA CADASTRADA COM SUCESSO!\n')
    input("Pressione ENTER para continuar...")

# 15
def login_empresa():
    global empresa_logada
    limpa_tela()
    exibir_nome()
    print('Login Empresa\n')
    login = input('Digite seu E-mail:')
    senha = input('Digite sua Senha:')
    con = sqlite3.connect("ibex.db")
    cursor = con.cursor()
    cursor.execute("SELECT senha FROM empresa WHERE login = ?", (login,))
    resultado = cursor.fetchone()
    if resultado:
        senha_correta = resultado[0]
        if senha == senha_correta:
            print('Redirecionando...\n')
            time.sleep(2)
            print("Login realizado com sucesso!\n")
            time.sleep(1)
            empresa_logada = login
            menu_empresa()
            return
        else:
            print("Senha incorreta.")
    else:
        print("Usuário não encontrado.")

    con.close()
    input("Pressione ENTER para continuar...")

# 16
def cad_produto():
    global empresa_logada
    limpa_tela()
    exibir_nome()
    print('Cadastro do produto\n')
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
    time.sleep(2)
    print('PRODUTO CADASTRADO COM SUCESSO!\n')
    input("Pressione ENTER para continuar...")

# 17
def cad_cliente():
    limpa_tela()
    exibir_nome()
    print('Insira seus dados!')
    nome = input('Nome:')
    senha = input('Crie uma Senha:')
    login = input('E-mail:')
    con = sqlite3.connect("ibex.db")
    cursor = con.cursor()
    sql = "INSERT INTO cliente (nome, senha, login) VALUES (?, ?, ?)"
    cursor.execute(sql, (nome, senha, login))
    con.commit()
    con.close()
    print('CADASTRADO COM SUCESSO!\n')
    input("Pressione ENTER para continuar...")

# 18
def login_cliente():
    global cliente_logado
    limpa_tela()
    exibir_nome()
    print('(Login do Cliente)\n')
    login = input('Digite seu E-mail:')
    senha = input('Digite sua Senha:')
    con = sqlite3.connect("ibex.db")
    cursor = con.cursor()
    cursor.execute("SELECT senha FROM cliente WHERE login = ?", (login,))
    resultado = cursor.fetchone()
    if resultado:
        senha_correta = resultado[0]
        if senha == senha_correta:
            print('Senha Correta! Redirecionando...\n')
            time.sleep(1)
            cliente_logado = login
            limpa_tela()
            print("Login realizado com sucesso!\n")
            time.sleep(1)
            menu_cliente()
        else:
            time.sleep(1)
            limpa_tela()
            print("\nSenha incorreta.\n")
            return

    else:
        print("Usuário não encontrado.\n")
        return
    con.close()
    input("Pressione ENTER para continuar...")

#19
def adicionar_carrinho():
    limpa_tela()
    cabecalho_carrinho()
    print("Adicionar Produto ao Carrinho\n")

    if cliente_logado is None:
        print("Você precisa estar logado como cliente para adicionar ao carrinho.")
        input("Pressione ENTER para continuar...")
        return

    nome_produto = input("Digite o nome do produto: ")
    con = sqlite3.connect("ibex.db")
    cursor = con.cursor()

    cursor.execute("SELECT id, nome, descricao, preco, quantidade FROM produtos WHERE nome LIKE ?", (f"%{nome_produto}%",))
    produtos = cursor.fetchall()

    if not produtos:
        print("Produto não encontrado.")
        con.close()
        input("Pressione ENTER para continuar...")
        return

    for p in produtos:
        print(f"ID: {p[0]} | Nome: {p[1]} | Marca: {p[2]} | Preço: R${p[3]:.2f} | Estoque: {p[4]}")

    try:
        produto_id = int(input("Digite o ID do produto: "))
        quantidade = int(input("Digite a quantidade: "))
    except ValueError:
        print("Entrada inválida.")
        con.close()
        input("Pressione ENTER para continuar...")
        return

    cursor.execute("SELECT nome, preco, quantidade, empresa_id FROM produtos WHERE id = ?", (produto_id,))
    produto = cursor.fetchone()

    if not produto:
        print("Produto não encontrado.")
        con.close()
        input("Pressione ENTER para continuar...")
        return

    nome, preco, estoque, empresa_id = produto
    if quantidade > estoque:
        print(f"Estoque insuficiente. Disponível: {estoque}")
        con.close()
        input("Pressione ENTER para continuar...")
        return

    cursor.execute("SELECT id FROM cliente WHERE login = ?", (cliente_logado,))
    cliente = cursor.fetchone()
    if not cliente:
        print("Cliente não encontrado.")
        con.close()
        input("Pressione ENTER para continuar...")
        return

    id_cliente = cliente[0]

    cursor.execute("""
        SELECT id FROM carrinho_temp 
        WHERE id_cliente = ? AND id_produto = ?
    """, (id_cliente, produto_id))
    existente = cursor.fetchone()

    if existente:
        cursor.execute("""
            UPDATE carrinho_temp SET quantidade = quantidade + ?
            WHERE id = ?
        """, (quantidade, existente[0]))
    else:
        cursor.execute("""
            INSERT INTO carrinho_temp (id_cliente, id_produto, nome_produto, quantidade, preco_unitario, id_empresa)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (id_cliente, produto_id, nome, quantidade, preco, empresa_id))

    con.commit()
    print(f"{quantidade}x {nome} adicionado ao carrinho.")
    con.close()
    input("Pressione ENTER para continuar...")

# 20
def ver_carrinho():
    limpa_tela()
    cabecalho_carrinho()

    if cliente_logado is None:
        print("Você precisa estar logado para ver o carrinho.")
        input("Pressione ENTER para continuar...")
        return

    con = sqlite3.connect("ibex.db")
    cursor = con.cursor()
    cursor.execute("SELECT id FROM cliente WHERE login = ?", (cliente_logado,))
    cliente = cursor.fetchone()
    if not cliente:
        print("Cliente não encontrado.")
        con.close()
        input("Pressione ENTER para continuar...")
        return

    id_cliente = cliente[0]
    cursor.execute("""
        SELECT id, nome_produto, quantidade, preco_unitario 
        FROM carrinho_temp WHERE id_cliente = ?
    """, (id_cliente,))
    itens = cursor.fetchall()

    if not itens:
        print("Carrinho está vazio.")
    else:
        total = 0
        for item in itens:
            subtotal = item[2] * item[3]
            print(f"{item[2]}x {item[1]} - R${item[3]:.2f} cada (Subtotal: R${subtotal:.2f})")
            total += subtotal
        print(f"\nTotal: R${total:.2f}")

    con.close()
    input("Pressione ENTER para continuar...")

# 21
def remover_carrinho():
    limpa_tela()
    cabecalho_carrinho()

    if cliente_logado is None:
        print("Você precisa estar logado para remover itens.")
        input("Pressione ENTER para continuar...")
        return

    con = sqlite3.connect("ibex.db")
    cursor = con.cursor()
    cursor.execute("SELECT id FROM cliente WHERE login = ?", (cliente_logado,))
    cliente = cursor.fetchone()
    if not cliente:
        print("Cliente não encontrado.")
        con.close()
        input("Pressione ENTER para continuar...")
        return

    id_cliente = cliente[0]
    cursor.execute("""
        SELECT id, nome_produto, quantidade FROM carrinho_temp WHERE id_cliente = ?
    """, (id_cliente,))
    itens = cursor.fetchall()

    if not itens:
        print("Carrinho está vazio.")
        con.close()
        input("Pressione ENTER para continuar...")
        return

    for idx, item in enumerate(itens, start=1):
        print(f"{idx}. {item[1]} - {item[2]}x")

    try:
        escolha = int(input("Digite o número do item que deseja remover: "))
        if 1 <= escolha <= len(itens):
            id_item = itens[escolha - 1][0]
            cursor.execute("DELETE FROM carrinho_temp WHERE id = ?", (id_item,))
            con.commit()
            print("Item removido do carrinho.")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida.")

    con.close()
    input("Pressione ENTER para continuar...")

#22
def finalizar_pedido():
    global cliente_logado

    limpa_tela()
    cabecalho_carrinho()

    if cliente_logado is None:
        print("Você precisa estar logado como cliente para finalizar o pedido.")
        input("Pressione ENTER para continuar...")
        return

    # Obtem o ID do cliente
    con = sqlite3.connect("ibex.db")
    cursor = con.cursor()
    cursor.execute("SELECT id FROM cliente WHERE login = ?", (cliente_logado,))
    resultado = cursor.fetchone()
    if not resultado:
        print("Cliente não encontrado.")
        con.close()
        input("Pressione ENTER para continuar...")
        return
    id_cliente = resultado[0]

    # Verifica se há itens no carrinho_temp
    cursor.execute("SELECT * FROM carrinho_temp WHERE id_cliente = ?", (id_cliente,))
    itens = cursor.fetchall()

    if not itens:
        print("Seu carrinho está vazio.")
        con.close()
        input("Pressione ENTER para continuar...")
        return

    # 1. BUSCAR ENDEREÇO POR CEP
    cep = input("Digite seu CEP (somente números): ").strip()
    try:
        resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        dados = resposta.json()
        if "erro" in dados:
            print("CEP inválido.")
            con.close()
            input("Pressione ENTER para continuar...")
            return
        endereco = f"{dados['logradouro']}, {dados['bairro']}, {dados['localidade']}-{dados['uf']}, {dados['cep']}"
        print("\nEndereço de entrega:")
        print(endereco)
    except:
        print("Erro ao consultar o CEP.")
        con.close()
        input("Pressione ENTER para continuar...")
        return

    # 2. RESUMO DO PEDIDO
    print("\nResumo do pedido:\n")
    total = 0
    for item in itens:
        _, _, _, nome, qtd, preco, _ = item
        subtotal = qtd * preco
        print(f"{qtd}x {nome} - R${preco:.2f} (Subtotal: R${subtotal:.2f})")
        total += subtotal

    print(f"\nTotal do pedido: R${total:.2f}")
    confirmar = input("\nDeseja confirmar o pedido? (s/n): ").lower()
    if confirmar != 's':
        print("Pedido cancelado.")
        con.close()
        input("Pressione ENTER para continuar...")
        return

    # 3. SALVAR EM TABELA FINAL DE PEDIDOS (aqui usaremos a tabela carrinho mesmo)
    for item in itens:
        _, id_cliente, id_produto, nome, qtd, preco, id_empresa = item
        cursor.execute("""
            INSERT INTO carrinho (id_cliente, id_produto, nome_produto, quantidade, preco_unitario, id_empresa)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (id_cliente, id_produto, nome, qtd, preco, id_empresa))

    # 4. Limpa o carrinho_temp
    cursor.execute("DELETE FROM carrinho_temp WHERE id_cliente = ?", (id_cliente,))
    con.commit()
    con.close()

    print("\n✅ Pedido confirmado! Obrigado por comprar com o Ibex 🧱 🚚.")
    print(f"📦 Endereço de entrega: {endereco}")
    input("\nPressione ENTER para continuar...")

#23
class Relatorio:
    def __init__(self, db_path='ibex.db'):
        self.db_path = db_path

    def conectar(self):
        con = sqlite3.connect(self.db_path)
        con.execute("PRAGMA foreign_keys = ON")
        return con, con.cursor()

    def total_clientes(self):
        con, cursor = self.conectar()
        cursor.execute("SELECT COUNT(*) FROM cliente")
        total = cursor.fetchone()[0]
        con.close()
        return total

    def total_empresas(self):
        con, cursor = self.conectar()
        cursor.execute("SELECT COUNT(*) FROM empresa")
        total = cursor.fetchone()[0]
        con.close()
        return total
    
    def produtos_por_empresa(self):
        con, cursor = self.conectar()
        cursor.execute("""
        SELECT e.nome, COUNT(p.id) 
        FROM empresa e 
        LEFT JOIN produtos p ON e.id = p.empresa_id 
        GROUP BY e.nome
    """)
        dados = cursor.fetchall()
        con.close()
        return dados

    def total_produtos(self):
        con, cursor = self.conectar()
        cursor.execute("SELECT COUNT(*) FROM produtos")
        total = cursor.fetchone()[0]
        con.close()
        return total

    def estoque_baixo(self, limite=5):
        con, cursor = self.conectar()
        cursor.execute("SELECT nome, quantidade FROM produtos WHERE quantidade <= ?", (limite,))
        dados = cursor.fetchall()
        con.close()
        return dados
#24
def gerar_relatorio():
    limpa_tela()
    exibir_nome()
    rel = Relatorio()

    print("Relatório do sistema:\n")
    print(f"Total de clientes: {rel.total_clientes()}")
    print(f"Total de empresas: {rel.total_empresas()}")
    print(f"Total de produtos: {rel.total_produtos()}\n")

    print("Produtos por empresa:")
    for nome, total in rel.produtos_por_empresa():
        print(f"- {nome}: {total} produto(s)")

    #print("\nProdutos com estoque baixo:")
    #for nome, qtd in rel.estoque_baixo():
    #    print(f"- {nome}: {qtd} unidade(s)")

    input("\nPressione ENTER para voltar...")

# 25
def adicionar_favorito():
    global favoritos
    limpa_tela()
    exibir_nome()
    print("ADICIONAR AOS FAVORITOS")
    
    nome = input("Digite o nome do produto que deseja favoritar: ")

    con = sqlite3.connect("ibex.db")
    cursor = con.cursor()
    cursor.execute("SELECT id, nome, descricao, preco FROM produtos WHERE nome LIKE ?", (f"%{nome}%",))
    produtos = cursor.fetchall()

    if produtos:
        for p in produtos:
            print(f"ID: {p[0]} | Nome: {p[1]} | Marca: {p[2]} | Preço: R${p[3]:.2f}")
        try:
            produto_id = int(input("Digite o ID do produto que deseja favoritar: "))
            produto = next((p for p in produtos if p[0] == produto_id), None)
            if produto:
                favoritos[produto_id] = {
                    "nome": produto[1],
                    "descricao": produto[2],
                    "preco": produto[3]
                }
                print(f"Produto '{produto[1]}' adicionado aos favoritos!")
            else:
                print("ID inválido.")
        except ValueError:
            print("Entrada inválida.")
    else:
        print("Nenhum produto encontrado.")
    con.close()
    input("Pressione ENTER para continuar...")

# 26
def ver_favoritos():
    limpa_tela()
    exibir_nome()
    print("SEUS FAVORITOS:\n")
    if not favoritos:
        print("Nenhum produto favoritado.")
    else:
        for f in favoritos.values():
            print(f"- {f['nome']} | Marca: {f['descricao']} | Preço: R${f['preco']:.2f}")
    input("\nPressione ENTER para voltar...")

# codigo principal
opcao = 0 

while opcao != 9:
    menu_principal()
    try:
        opcao = int(input("Opção: "))
    except ValueError:
        print("Digite um número válido!")
        time.sleep(1)
        continue

    if opcao == 1:
        cad_cliente()
    elif opcao == 2:
        login_cliente()
    elif opcao == 3:
        cad_empresa()
    elif opcao == 4:
        login_empresa()
    elif opcao == 9:
        finalizando_app()
    else:
        print("Opção inválida.")
        time.sleep(1)
