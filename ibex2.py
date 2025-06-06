import os
import sqlite3
import time
import requests

empresa_logada = None
cliente_logado = None
carrinho = {}

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
    while True:
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
        elif opcao == 4:
            break
        else:
            print('Opção Invalida!')
# 5   
def menu_cliente():
    while True:
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
        elif opcao == 9:
            break
        else:
            print('Opção invalida!')

# 6
def menu_carrinho():
    while True:
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
        elif opcao == 9:
            break
        else:
            print('Opção invalida!')
            
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
            print('------------------------\n')
            time.sleep(2)
            input("Pressione ENTER para voltar...")
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
            time.sleep(2)
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
            time.sleep(2)
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
            time.sleep(2)
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
        time.sleep(2)
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
    time.sleep(2)
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
            time.sleep(2)
            cliente_logado = login
            limpa_tela()
            print("Login realizado com sucesso!\n")
            time.sleep(1)
            menu_cliente()
        else:
            time.sleep(2)
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
    global carrinho
    limpa_tela()
    cabecalho_carrinho()
    print("Adicionar Produto ao Carrinho\n")

    nome_produto = input("Digite o nome do produto que deseja adicionar: ")
    con = sqlite3.connect("ibex.db")
    cursor = con.cursor()
    cursor.execute("SELECT id, nome, descricao, preco, quantidade FROM produtos WHERE nome LIKE ?", (f"%{nome_produto}%",))
    produtos = cursor.fetchall()

    if not produtos:
        time.sleep(2)
        print("Produto não encontrado.")
        con.close()
        input("Pressione ENTER para continuar...")
        return

    time.sleep(2)
    print("\nProdutos encontrados:")
    for p in produtos:
        print(f"ID: {p[0]} | Nome: {p[1]} | Marca: {p[2]} | Preço: R${p[3]:.2f} | Estoque: {p[4]}")

    try:
        produto_id = int(input("Digite o ID do produto que deseja adicionar ao carrinho: "))
        quantidade = int(input("Digite a quantidade desejada: "))
    except ValueError:
        print("Entrada inválida.")
        con.close()
        input("Pressione ENTER para continuar...")
        return
    cursor.execute("SELECT nome, preco, quantidade, empresa_id FROM produtos WHERE id = ?", (produto_id,))
    produto = cursor.fetchone()

    if produto:
        nome, preco, estoque, empresa_id = produto

        if quantidade > estoque:
            time.sleep(2)
            print(f"Quantidade indisponível. Estoque atual: {estoque}")
        else:
            if produto_id in carrinho:
                carrinho[produto_id]["quantidade"] += quantidade
            else:
                carrinho[produto_id] = {
                    "nome": nome,
                    "preco": preco,
                    "quantidade": quantidade,
                    "empresa_id": empresa_id
                }
            time.sleep(2)
            print(f"{quantidade} de {nome} adicionado(s) ao carrinho.")
    else:
        print("Produto não encontrado.")
    con.close()
    input("Pressione ENTER para continuar...")

# 20
def ver_carrinho():
    limpa_tela()
    cabecalho_carrinho()
    print("Seu carrinho de compras:\n")
    if not carrinho:
        print("Carrinho está vazio.")
    else:
        total = 0
        for item in carrinho.values():
            subtotal = item["preco"] * item["quantidade"]
            print(f'{item["quantidade"]}x {item["nome"]} - R${item["preco"]:.2f} cada (Subtotal: R${subtotal:.2f})')
            total += subtotal
        time.sleep(2)
        print(f"\nTotal: R${total:.2f}")
    input("Pressione ENTER para continuar...")

# 21
def remover_carrinho():
    limpa_tela()
    exibir_nome()
    print("Remover item do carrinho:\n")
    if not carrinho:
        print("Carrinho está vazio.")
        input("Pressione ENTER para continuar...")
        return
    produtos = list(carrinho.items()) 
    for idx, (produto_id, item) in enumerate(produtos, start=1):
        time.sleep(2)
        print(f"{idx}. {item['nome']} - {item['quantidade']}x - R${item['preco']:.2f} cada")

    try:
        escolha = int(input("\nDigite o número do item que deseja remover: "))
        if 1 <= escolha <= len(produtos):
            produto_id = produtos[escolha - 1][0]
            removido = carrinho.pop(produto_id)
            time.sleep(2)
            print(f"\n{removido['nome']} removido do carrinho.")
        else:
            print("\nOpção inválida.")
    except ValueError:
        print("\nEntrada inválida. Digite um número.")
    input("\nPressione ENTER para continuar...")

#22
def finalizar_pedido():
    global carrinho, cliente_logado

    limpa_tela()
    cabecalho_carrinho()

    if not carrinho:
        print("Seu carrinho está vazio.")
        input("Pressione ENTER para continuar...")
        return

    if cliente_logado is None:
        print("Você precisa estar logado como cliente para finalizar o pedido.")
        input("Pressione ENTER para continuar...")
        return

    # 1. BUSCAR ENDEREÇO POR CEP
    cep = input("Digite seu CEP (somente números): ").strip()

    try:
        resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        dados = resposta.json()

        if "erro" in dados:
            print("CEP inválido. Tente novamente.")
            input("Pressione ENTER para continuar...")
            return

        endereco = f"{dados['logradouro']}, {dados['bairro']}, {dados['localidade']}-{dados['uf']}, {dados['cep']}"
        print("\nEndereço de entrega:")
        print(endereco)
    except:
        print("Erro ao consultar o CEP. Verifique sua conexão.")
        input("Pressione ENTER para continuar...")
        return

    # 2. MOSTRAR RESUMO DO PEDIDO
    print("\nResumo do pedido:\n")
    total = 0
    for item in carrinho.values():
        subtotal = item["quantidade"] * item["preco"]
        print(f"{item['quantidade']}x {item['nome']} - R${item['preco']:.2f} cada (Subtotal: R${subtotal:.2f})")
        total += subtotal

    print(f"\nTotal do pedido: R${total:.2f}")
    confirmar = input("\nDeseja confirmar o pedido? (s/n): ").lower()

    if confirmar != 's':
        print("Pedido cancelado.")
        input("Pressione ENTER para continuar...")
        return

    # 3. SALVAR NO BANCO
    con = sqlite3.connect("ibex.db")
    cursor = con.cursor()
    cursor.execute("SELECT id FROM cliente WHERE login = ?", (cliente_logado,))
    resultado = cursor.fetchone()

    if resultado:
        id_cliente = resultado[0]

        for produto_id, item in carrinho.items():
            cursor.execute("""
                INSERT INTO carrinho (id_cliente, id_produto, nome_produto, quantidade, preco_unitario, id_empresa)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                id_cliente,
                produto_id,
                item["nome"],
                item["quantidade"],
                item["preco"],
                item["empresa_id"]
            ))

        con.commit()
        print("\n✅ Pedido confirmado! Obrigado por comprar com o Ibex 🧱 🚚.")
        print(f"📦 Endereço de entrega: {endereco}")
        carrinho.clear()
    else:
        print("Erro: cliente não encontrado no banco.")

    con.close()
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

    print("\nProdutos com estoque baixo:")
    for nome, qtd in rel.estoque_baixo():
        print(f"- {nome}: {qtd} unidade(s)")

    input("\nPressione ENTER para voltar...")


# codigo principal
opcao = 1
while (opcao!=9):
    menu_principal()
    opcao = int(input("Opcao:"))
    if (opcao==1):
        cad_cliente()
    elif (opcao==2):
        login_cliente()
    elif (opcao==3):
        cad_empresa()
    elif (opcao==4):
        login_empresa()
    elif (opcao==9):
        finalizando_app()
