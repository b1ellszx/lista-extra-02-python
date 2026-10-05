"""Lista 5, exercício 3: unpacking diretamente no loop for."""


def main():
    vendas_dia = [("Monitor", 900, 2), ("Teclado", 150, 5), ("Mouse", 80, 10)]

    for produto, preco_unitario, quantidade in vendas_dia:
        total = preco_unitario * quantidade
        print(f"Produto: {produto} | Total: R${total:.2f}")


if __name__ == "__main__":
    main()
