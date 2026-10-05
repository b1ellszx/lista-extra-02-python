"""Lista 4, exercício 1: remoção de espaços externos e formato de título."""


def padronizar_texto(texto):
    return texto.strip().title()


def main():
    produtos_baguncados = [" iphone 13 ", "MACBOOK PRO ", " aIrPoDs Pro", "iPad mini ", " caixa de som bluetooth "]

    for produto in produtos_baguncados:
        print(padronizar_texto(produto))


if __name__ == "__main__":
    main()
