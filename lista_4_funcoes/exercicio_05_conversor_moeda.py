"""Lista 4, exercício 5: conversão dos preços com funções combinadas."""


def converter_para_real(preco_dolar, cotacao):
    return preco_dolar * cotacao


def processar_lista_precos(precos_dolar, cotacao):
    for preco in precos_dolar:
        valor_real = converter_para_real(preco, cotacao)
        print(f"O item custa R${valor_real:.2f}")


def main():
    precos_usd = [100, 50, 250]
    cotacao = 5.20
    processar_lista_precos(precos_usd, cotacao)


if __name__ == "__main__":
    main()
