"""Lista 3, exercício 2: comissão calculada sobre cada venda."""


def main():
    vendas = [2000, 5000, 1000, 8000, 3000]
    total_comissao = 0

    for venda in vendas:
        if venda > 4000:
            comissao = venda * 0.10
        else:
            comissao = venda * 0.05
        total_comissao += comissao

    print(f"Total de comissão: R${total_comissao:.2f}")


if __name__ == "__main__":
    main()
