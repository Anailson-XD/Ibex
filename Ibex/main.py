from ibex.utilitarios import exibir_nome
from ibex.menus import menu_principal
from ibex.banco import criar_tabelas

def main():
    criar_tabelas()       # Cria tabelas do banco se não existirem
    exibir_nome()         # Exibe o cabeçalho do sistema
    menu_principal()      # Chama o menu principal do sistema

if __name__ == '__main__':
    main()