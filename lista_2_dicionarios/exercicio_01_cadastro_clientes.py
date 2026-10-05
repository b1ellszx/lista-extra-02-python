"""Lista 2, exercício 1: atualização do faturamento dos clientes."""


def main():
    clientes = {"Lira": 5000, "Alon": 3000, "Julia": 4500}

    clientes["Alon"] += 1500
    clientes["Marcos"] = 2000

    print("Clientes atualizados:", clientes)


if __name__ == "__main__":
    main()
