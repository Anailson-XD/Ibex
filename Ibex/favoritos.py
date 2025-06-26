def adicionar_favorito():
    global favoritos
    exibir_subtitulo('Adicione produto(s) aos favoritos')

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

def ver_favoritos():
    exibir_subtitulo('Seus favoritos')
    if not favoritos:
        print("Nenhum produto favoritado.")
    else:
        for f in favoritos.values():
            print(f"- {f['nome']} | Marca: {f['descricao']} | Preço: R${f['preco']:.2f}")
    input("\nPressione ENTER para voltar...")