"""Lista 2, exercício 3: extração de valores, soma e média."""


def main():
    vendas_regiao = {"Norte": 15000, "Sul": 22000, "Leste": 18000, "Oeste": 25000}

    faturamentos = list(vendas_regiao.values())
    total = sum(faturamentos)
    media = total / len(faturamentos)

    print("Faturamentos das regiões:", faturamentos)
    print(f"Faturamento total: R${total:.2f}")
    print(f"Faturamento médio: R${media:.2f}")


if __name__ == "__main__":
    main()
