"""Lista 3, exercício 1: dez lembretes em contagem regressiva."""


def main():
    # O limite zero não entra no range: são os valores de 10 até 1.
    for minutos in range(10, 0, -1):
        print(f"Faltam {minutos} minutos para começar o treinamento")


if __name__ == "__main__":
    main()
