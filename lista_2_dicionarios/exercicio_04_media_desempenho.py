"""Lista 2, exercício 4: acesso às notas de Paula e cálculo da média."""


def main():
    desempenho = {"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}

    notas_paula = desempenho["Paula"]
    media = sum(notas_paula) / len(notas_paula)

    print(f"A média de Paula foi {media:.2f}")


if __name__ == "__main__":
    main()
