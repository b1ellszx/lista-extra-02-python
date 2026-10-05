"""Lista 1, exercício 1: relatório das vendas diárias."""


def main():
    vendas = [1500, 2000, 800, 3500, 1200]

    total = sum(vendas)
    media = total / len(vendas)

    print(f"Total de vendas na semana: R${total:.2f}")
    print(f"Média de vendas diária: R${media:.2f}")
    print(f"Melhor venda: R${max(vendas):.2f}")
    print(f"Pior venda: R${min(vendas):.2f}")


if __name__ == "__main__":
    main()
