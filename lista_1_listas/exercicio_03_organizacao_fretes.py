"""Lista 1, exercício 3: ordenação decrescente e fatiamento."""


def main():
    fretes = [50, 80, 20, 150, 40]

    fretes.sort(reverse=True)
    top_fretes = fretes[:2]

    print("Fretes ordenados:", fretes)
    print("Dois fretes mais caros:", top_fretes)


if __name__ == "__main__":
    main()
