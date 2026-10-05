
estoque = [
    {
    "codigoProduto": 101,
    "descricaoProduto": "Caneta Azul",
    "estoque": 150
    },
    {
    "codigoProduto": 102,
    "descricaoProduto": "Caderno Universitário",
    "estoque": 75
    },
    {
    "codigoProduto": 103,
    "descricaoProduto": "Borracha Branca",
    "estoque": 200
    },
    {
    "codigoProduto": 104,
    "descricaoProduto": "Lápis Preto HB",
    "estoque": 320
    },
    {
    "codigoProduto": 105,
    "descricaoProduto": "Marcador de Texto Amarelo",
    "estoque": 90
    }
]


def adicionar_estoque():
    codigo = input("Digite o código do produto que deseja adicionar estoque: ")
    quantidade = int(input("Digite a quantidade que deseja adicionar: "))
    nao_encontrado = True
    for produto in estoque:
        if produto["codigoProduto"] == int(codigo):
            produto["estoque"] += quantidade
            print(f"Estoque atualizado para o produto {produto['descricaoProduto']}: {produto['estoque']}")
            nao_encontrado = False
            break
    if nao_encontrado:
        print("Produto não encontrado.")
    
def subtrair_estoque():
    codigo = input("Digite o código do produto que deseja subtrair estoque: ")
    quantidade = int(input("Digite a quantidade que deseja subtrair: "))
    nao_encontrado = True
    for produto in estoque:
        if produto["codigoProduto"] == int(codigo):
            nao_encontrado = False
            if produto["estoque"] >= quantidade:
                produto["estoque"] -= quantidade
                print(f"Estoque atualizado para o produto {produto['descricaoProduto']}: {produto['estoque']}")
                break
            else:
                print("Quantidade insuficiente em estoque.")
                break

    if nao_encontrado:
        print("Produto não encontrado.")

if __name__ == "__main__":
    resposta = "y"
    while resposta == "y" or resposta == "yes":
        operacao = input("Deseja adicionar ou subtrair estoque? (Digite 'adicionar' ou 'subtrair'): ")
        if operacao == "adicionar":
            adicionar_estoque()
        elif operacao == "subtrair":
            subtrair_estoque()
        resposta = input("Deseja continuar? (Digite 'y' para sim ou 'n' para não): ")
    print(estoque)

