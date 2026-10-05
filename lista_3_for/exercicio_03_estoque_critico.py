"""Lista 3, exercício 3: alertas para quantidades abaixo de oito."""


def main():
    estoque_produtos = ["monitor", "teclado", "mouse", "headset", "gabinete"]
    estoque_quantidades = [5, 12, 2, 8, 15]
    estoque_minimo = 8

    for indice in range(len(estoque_produtos)):
        produto = estoque_produtos[indice]
        quantidade = estoque_quantidades[indice]
        if quantidade < estoque_minimo:
            print(f"ALERTA: O produto {produto} está com apenas {quantidade} unidades no estoque!")


if __name__ == "__main__":
    main()
