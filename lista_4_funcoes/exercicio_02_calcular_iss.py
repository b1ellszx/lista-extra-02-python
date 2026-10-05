"""Lista 4, exercício 2: imposto conforme a regra didática do enunciado."""


def calcular_iss(valor_servico):
    if valor_servico > 5000:
        taxa = 0.05
    else:
        taxa = 0.03
    return valor_servico * taxa


def main():
    print(f"ISS da nota de R$8000.00: R${calcular_iss(8000):.2f}")
    print(f"ISS da nota de R$2000.00: R${calcular_iss(2000):.2f}")


if __name__ == "__main__":
    main()
