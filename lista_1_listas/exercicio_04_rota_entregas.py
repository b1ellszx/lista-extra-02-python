"""Lista 1, exercício 4: extensão de uma rota e busca de índice."""


def main():
    rota = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"]
    novas_cidades = ["Itu", "Valinhos"]

    rota.extend(novas_cidades)
    indice = rota.index("Sorocaba")

    print("Rota completa:", rota)
    print("Índice de Sorocaba:", indice)
    # O índice começa em zero; a posição na contagem começa em um.
    print(f"Sorocaba é a {indice + 1}ª cidade da rota")


if __name__ == "__main__":
    main()
