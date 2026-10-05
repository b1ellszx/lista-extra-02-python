"""Lista 2, exercício 2: consulta interativa com normalização da entrada."""


def main():
    estoque = {"teclado": 50, "mouse": 120, "monitor": 30}
    produto = input("Digite o nome do produto: ").strip().lower()

    if produto in estoque:
        print(f"Quantidade disponível de {produto}: {estoque[produto]}")
    else:
        print("Produto não encontrado no sistema")


if __name__ == "__main__":
    main()
