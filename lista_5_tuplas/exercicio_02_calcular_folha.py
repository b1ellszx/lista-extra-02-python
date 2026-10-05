"""Lista 5, exercício 2: retorno de desconto e salário líquido."""


def calcular_folha(salario_bruto):
    desconto = salario_bruto * 0.10
    salario_liquido = salario_bruto - desconto
    return desconto, salario_liquido


def main():
    desconto, salario_liquido = calcular_folha(5000)
    print(f"Desconto: R${desconto:.2f} | Salário Líquido: R${salario_liquido:.2f}")


if __name__ == "__main__":
    main()
