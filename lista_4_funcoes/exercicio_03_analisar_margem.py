"""Lista 4, exercício 3: classificação da margem de lucro."""


def analisar_margem(faturamento, custo):
    if faturamento <= 0:
        raise ValueError("O faturamento deve ser maior que zero.")

    lucro = faturamento - custo
    margem = lucro / faturamento

    if margem >= 0.30:
        return "Margem Saudável"
    return "Margem Baixa"


def main():
    print(analisar_margem(10000, 6000))


if __name__ == "__main__":
    main()
