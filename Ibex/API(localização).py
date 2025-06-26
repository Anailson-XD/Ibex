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