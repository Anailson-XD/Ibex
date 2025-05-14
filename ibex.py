import os
import sqlite3
import time

empresa_logada = None
cliente_logado = None

# 1
def exibir_nome():
    print('####################')
    print('Ｂｅｍ ｖｉｎｄｏ ａｏ Ｉｂｅｘ！')
    print('####################')

# 2
def menu_principal():
    limpa_tela()
    exibir_nome()
    print('1. Cadastre-se')
    print('2. Login ')
    print('3. Cadastrar Empresa')
    print('4. Login Empresa')
    print('9. Sair')

# 3
def menu_empresa():
    while True:
        limpa_tela()
        exibir_nome()
        print('Menu da empresa')
        print('1. Cadastrar produtos')
        print('2. Ver produtos')
        print('3. Sair')
        opcao = int(input('Escolha uma opção:'))
        if opcao == 1:
            time.sleep(2)
            cad_produto()
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            break
        else:
            print('Opção Invalida!')
            time.sleep(2)

# 4
def menu_cliente():
    while True:
        limpa_tela()
        exibir_nome()
        print('Menu Cliente\n')
        print('1. Ver Produtos disponiveis')
        print('2. Buscar produtos')
        print('3. Ver empresas cadastradas')
        print('4. Atualizar dados')
        print('5. Adicionar produto ao carrinho')
        print('6. Ver Carrinho')
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
            print('Em breve...')
        elif opcao == 6:
            print('Em breve...')
        elif opcao == 9:
            break
        else:
            print('Opção invalida!')
            time.sleep(2)

# 5
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
            print(f'Marca:{p[1]}')
            print(f'Preço:{p[2]}')
            print(f'Quantidade:{p[3]}')
            print(f'Categoria:{p[4]}')
            print('------------------------\n')
            time.sleep(2)
            input("Pressione ENTER para voltar...")
    else:
        print('Nenhum Produto encontrado\n')
        input("Pressione ENTER para continuar...")

# 6
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

# 7
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

# 8
def ver_empresas():
    limpa_tela()
    exibir_nome()
    print('Empresas cadastradas\n')
    con = sqlite3.connect("ibex.db")
    cursor = con.cursor()
    cursor.execute('SELECT nome, login, cnpj, loc FROM empresa')
    empresas = cursor.fetchall()
    if empresas:
        for empresa in empresas:
            print(f'Nome:{empresa[0]}')
            print(f'Email:{empresa[1]}')
            print(f'CNPJ:{empresa[2]}')
            print(f'Localização:{empresa[3]}')
            print('------------------------\n')
            time.sleep(2)
    else:
        print('Nenhuma empresa encontrada')
    con.close()
    input("Pressione ENTER para continuar...")

# 9 
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
        print('\nDados atualizados com sucesso!')

    else:
        print('\nErro: cliente não encontrado.')

    con.close()
    input("Pressione ENTER para continuar...")

# 10
def limpa_tela():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

# 11
def finalizando_app():
    os.system('cls')
    print('Saindo do app!\n')

# 12
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
    print('EMPRESA CADASTRADA COM SUCESSO!\n')
    input("Pressione ENTER para continuar...")

# 13
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
            empresa_logada = login
            print("Login realizado com sucesso!\n")
            input("Pressione ENTER para continuar...")
            menu_empresa()
        else:
            print("Senha incorreta.")
    else:
        print("Usuário não encontrado.")

    con.close()
    input("Pressione ENTER para continuar...")

# 14
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
    sql = 'INSERT INTO produto (nome, descricao, preco, quantidade, categoria, empresa_id) VALUES (?,?,?,?,?,?)'
    cursor.execute(sql, (nome, descricao, preco, quantidade, categoria, empresa_logada))
    con.commit()
    con.close()
    time.sleep(2)
    print('PRODUTO CADASTRADO COM SUCESSO!\n')
    input("Pressione ENTER para continuar...")

# 15
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

# 16 
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
            cliente_logado = login
            print('Senha Correta! Redirecionando...\n')
            time.sleep(2)
            limpa_tela()
            print("Login realizado com sucesso!\n")
            menu_cliente()
        else:
            time.sleep(2)
            limpa_tela()
            print("\nSenha incorreta.\n")
    else:
        print("Usuário não encontrado.\n")
    con.close()
    input("Pressione ENTER para continuar...")

# cod principal
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
