"""Lista 1, exercício 2: adição, alteração, consulta e remoção."""


def main():
    estoque = ["monitor", "teclado", "mouse", "headset"]

    estoque.append("webcam")
    indice_teclado = estoque.index("teclado")
    estoque[indice_teclado] = "teclado mecanico"
    print("impressora" in estoque)
    estoque.remove("mouse")

    print("Estoque atualizado:", estoque)


if __name__ == "__main__":
    main()
