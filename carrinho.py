from utilitarios import *
import sqlite3
import requests

def adicionar_carrinho():
    exibir_subtitulo('Adicione produto(s) ao carrinho')
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


def ver_carrinho():
    exibir_subtitulo('Produtos no carrinho')

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


def remover_carrinho():
    exibir_subtitulo('Remova produto(s) do carrinho')

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

def finalizar_pedido():
    global cliente_logado
    exibir_subtitulo('Finalize seu pedido')

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
