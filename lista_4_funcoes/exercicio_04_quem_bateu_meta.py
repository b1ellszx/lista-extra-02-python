"""Lista 4, exercício 4: vendedores que atingiram ou superaram a meta."""


def quem_bateu_meta(vendedores, meta):
    for nome, faturamento in vendedores.items():
        if faturamento >= meta:
            print(f"Vendedor {nome} bateu a meta!")


def main():
    equipe_vendas = {"João": 12000, "Maria": 9500, "Ricardo": 10000, "Fernanda": 15200, "Paulo": 5000}
    meta_objetivo = 10000

    quem_bateu_meta(equipe_vendas, meta_objetivo)


if __name__ == "__main__":
    main()
