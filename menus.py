from colaborador import aceitar_pedido,listar_pedidos_pendentes,ver_meus_pedidos,concluir_pedido 
from utilitarios import *
from cadastro import *
from empresas import cad_produto,listar_produtos
from relatorios import *
from clientes import ver_produtos,busca_produto,ver_empresas,atualizar_cliente,menu_carrinho,historico_pedidos,solicitar_servicos



def menu_principal():
    exibir_subtitulo('Selecione uma das opções: ')
    print('1. Cadastre-se')
    print('2. Login ')
    print('3. Cadastrar Empresa')
    print('4. Login Empresa')
    print('5. Cadastrar Colaborador')
    print('6. Login Colaborador')
    print('9. Sair')

def menu_empresa():
    opcao = 0
    while opcao != 5:
        exibir_nome()
        exibir_subtitulo('Menu cliente')
        print('1. Cadastrar produtos')
        print('2. Listar produtos')
        print('3. Relatório')
        print('5. Sair')
        opcao = int(input('Escolha uma opção:'))
        if opcao == 1:
            cad_produto()
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            gerar_relatorio()
        elif opcao not in [1, 2, 3, 5]:
            print('Opção inválida!')
            input("Pressione ENTER para continuar...")

def menu_cliente():
    opcao = 0
    while opcao != 9:
        exibir_subtitulo('Menu cliente')
        print('1. Ver Produtos disponiveis')
        print('2. Buscar produtos')
        print('3. Ver empresas cadastradas')
        print('4. Atualizar dados')
        print('5. Carrinho')
        print('6. Ver pedidos anteriores')
        print('7. Solicitar Serviços')
        print('9. Sair')
        try:
            opcao = int(input("Opção: "))
        except ValueError:
            print("Opção inválida.")
            continue
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
        elif opcao == 6:
            historico_pedidos()
        elif opcao == 7:
            solicitar_servicos()
        elif opcao not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print('Opção inválida!')
            input("Pressione ENTER para continuar...")



def menu_colaborador():
    opcao = 0
    while opcao != 9:
        exibir_subtitulo('Menu do Colaborador')
        print('1. Ver pedidos pendentes')
        print('2. Aceitar um pedido')
        print('3. Ver meus pedidos aceitos')
        print('4. Marcar pedido como concluído')
        print('9. Sair')

        try:
            opcao = int(input('Escolha uma opção: '))
        except ValueError:
            print('Opção inválida! Digite um número.')
            continue

        if opcao == 1:
            listar_pedidos_pendentes()
        elif opcao == 2:
            aceitar_pedido()
        elif opcao == 3:
            ver_meus_pedidos()
        elif opcao == 4:
            concluir_pedido()
        elif opcao == 9:
            print('Saindo do menu do colaborador...')
        else:
            print('Opção inválida!')

        input('\nPressione ENTER para continuar...')