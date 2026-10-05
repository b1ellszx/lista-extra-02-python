"""Lista 5, exercício 4: total e média retornados em uma tupla."""


def analisar_vendas(vendas):
    if not vendas:
        return 0, 0
    total = sum(vendas)
    media = total / len(vendas)
    return total, media


def main():
    dados_filiais = {"Matriz": [10000, 15000, 20000], "Filial Sul": [5000, 7000]}

    for nome, vendas in dados_filiais.items():
        total, media = analisar_vendas(vendas)
        print(f"Filial {nome} -> Total: R${total:.2f}, Média: R${media:.2f}")


if __name__ == "__main__":
    main()
