"""Lista 1, exercício 5: atualização interativa de listas correspondentes."""

from math import isfinite


def main():
    precos = [100.0, 250.0, 500.0]
    vinhos = ["Branco", "Tinto", "Champagne"]

    nome = input("Digite o nome do produto (Branco, Tinto ou Champagne): ").strip().lower()
    nomes_normalizados = [vinho.lower() for vinho in vinhos]

    if nome not in nomes_normalizados:
        print("Produto não encontrado no sistema")
        return

    try:
        novo_preco = float(input("Digite o novo preço: ").strip().replace(",", "."))
    except ValueError:
        print("Preço inválido. Digite um número, como 275,50.")
        return

    if not isfinite(novo_preco) or novo_preco < 0:
        print("Preço inválido. Digite um número finito maior ou igual a zero.")
        return

    # As duas listas usam o mesmo índice para representar o mesmo produto.
    indice = nomes_normalizados.index(nome)
    precos[indice] = novo_preco

    print("Vinhos:", vinhos)
    print("Preços:", precos)


if __name__ == "__main__":
    main()
