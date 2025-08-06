from utilitarios import *
from menus import *
import sqlite3
import time

def login_colaborador():
    global colaborador_logado
    exibir_subtitulo('Faça o Login')
    login = input('Digite seu E-mail:')
    senha = input('Digite a senha:')
    con = sqlite3.connect('ibex.db')
    cursor = con.cursor()
    cursor.execute('SELECT senha FROM colaboradores WHERE login = ?', (login,))
    resultado = cursor.fetchone()
    if resultado:
        senha_correta = resultado[0]
        if senha == senha_correta:
            print('Redirecionamento...\n')
            time.sleep(1)
            print('Login realizado com sucesso!\n')
            time.sleep(1)
            colaborador_logado = login
            menu_colaborador()
        else:
            print('Senha incorreta!')
    else:
        print('Usuário não encontrado!')

    con.close()
    input('Pressione ENTER para continuar...')



def login_empresa():
    global empresa_logada
    exibir_subtitulo('Login empresa')
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
            time.sleep(1)
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



def login_cliente():
    global cliente_logado
    exibir_subtitulo('Realize seu login')
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
            os.system('cls')
            print("Login realizado com sucesso!\n")
            time.sleep(1)
            menu_cliente()
        else:
            time.sleep(1)
            os.system('cls')
            print("\nSenha incorreta.\n")
            return

    else:
        print("Usuário não encontrado.\n")
        return
    con.close()
    input("Pressione ENTER para continuar...")
