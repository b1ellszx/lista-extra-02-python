"""Lista 3, exercício 4: comparação dos gastos com as metas mensais."""


def main():
    metas = {"jan": 1000, "fev": 1200, "mar": 1100}
    gastos = {"jan": 900, "fev": 1350, "mar": 1100}

    for mes in metas:
        if gastos[mes] <= metas[mes]:
            print(f"Mês {mes}: Dentro do orçamento.")
        else:
            diferenca = gastos[mes] - metas[mes]
            print(f"Mês {mes}: Orçamento estourado em R${diferenca:.2f}.")


if __name__ == "__main__":
    main()
