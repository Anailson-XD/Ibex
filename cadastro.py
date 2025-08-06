import sqlite3
import time
from utilitarios import *

def cad_colaborador():
    exibir_subtitulo('Seja um colaborador!')
    nome = input('Nome:')
    login = input('E-mail:')
    senha = input('Crie uma senha:')
    numero = input('Número pra contato:')
    funcao = input('Qual sua aréa de atuação:')
    con = sqlite3.connect('ibex.db')
    cursor = con.cursor()
    sql = 'INSERT INTO colaboradores (nome, login, senha, numero, funcao) VALUES (?, ?, ?, ?, ?)'
    cursor.execute(sql, (nome, login, senha, numero, funcao))
    con.commit()
    con.close()
    print('Redirecionando...\n')
    time.sleep(1)
    print('CADASTRO REALIZADO COM SUCESSO!\n')
    input('Pressione ENTER para continuar...')

def cad_empresa():
    exibir_subtitulo('Cadastre sua empresa')
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

def cad_cliente():
    exibir_subtitulo('Cadastre-se agora!')
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

