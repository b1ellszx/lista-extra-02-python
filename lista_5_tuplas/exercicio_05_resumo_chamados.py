"""Lista 5, exercício 5: quantidade de chamados e maior espera."""


def resumo_chamados(tempos):
    if not tempos:
        return 0, 0
    return len(tempos), max(tempos)


def main():
    tempos = [15, 45, 10, 120, 30]
    quantidade, tempo_maximo = resumo_chamados(tempos)

    print(f"Resumo diário: {quantidade} chamados.")
    print(f"ALERTA: O tempo máximo de espera foi de {tempo_maximo} minutos!")


if __name__ == "__main__":
    main()
