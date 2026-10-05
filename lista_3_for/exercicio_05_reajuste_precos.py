"""Lista 3, exercício 5: aumento percentual informado pelo usuário."""

from math import isfinite


def main():
    precos = {"celular": 1500, "tablet": 2500, "notebook": 5000}

    try:
        percentual = float(input("Digite o percentual de aumento (ex.: 10): ").strip().replace(",", "."))
    except ValueError:
        print("Percentual inválido. Digite um número, como 10 ou 7,5.")
        return

    if not isfinite(percentual) or percentual < 0:
        print("Percentual inválido. Digite um número finito maior ou igual a zero.")
        return

    for produto in precos:
        # Exemplo: 10% corresponde ao fator 1 + 10 / 100 = 1,10.
        precos[produto] = precos[produto] * (1 + percentual / 100)

    print("Catálogo atualizado:")
    for produto, preco in precos.items():
        print(f"{produto}: R${preco:.2f}")


if __name__ == "__main__":
    main()
