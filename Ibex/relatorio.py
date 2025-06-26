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
    
    def produtos_por_empresa(self):
        con, cursor = self.conectar()
        cursor.execute("""
        SELECT e.nome, COUNT(p.id) 
        FROM empresa e 
        LEFT JOIN produtos p ON e.id = p.empresa_id 
        GROUP BY e.nome
    """)
        dados = cursor.fetchall()
        con.close()
        return dados

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
    
#
def gerar_relatorio():
    exibir_subtitulo('Relátorio do sistema')
    rel = Relatorio()

    print("Relatório do sistema:\n")
    print(f"Total de clientes: {rel.total_clientes()}")
    print(f"Total de empresas: {rel.total_empresas()}")
    print(f"Total de produtos: {rel.total_produtos()}\n")

    print("Produtos por empresa:")
    for nome, total in rel.produtos_por_empresa():
        print(f"- {nome}: {total} produto(s)")

    input("\nPressione ENTER para voltar...")