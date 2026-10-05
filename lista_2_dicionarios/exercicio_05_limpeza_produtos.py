"""Lista 2, exercício 5: remoção com pop e verificação de chave."""


def main():
    produtos = {"celular": 1500, "camera": 800, "radio": 200, "fone": 100}

    valor_removido = produtos.pop("radio")

    print(f"Valor do produto removido: R${valor_removido:.2f}")
    print("celular" in produtos)
    print("Produtos restantes:", produtos)


if __name__ == "__main__":
    main()
