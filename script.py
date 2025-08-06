import time
from utilitarios import *
from menus import *
from dados import *
from login import *
from cadastro import *

empresa_logada = None
cliente_logado = None
colaborador_logado = None


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
    elif opcao == 5:
        cad_colaborador()
    elif opcao == 6:
        login_colaborador()
    elif opcao == 9:
        finalizando_app()
    else:
        print("Opção inválida.")
        time.sleep(1)