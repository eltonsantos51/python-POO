from simulador import *


def main():
    a1 = Doc('prova', 250_000)
    a2 = PDF('contrato', 1_300_000)
    abrir_arquivo(a1)
    print(a1.nome_completo)


if __name__ == "__main__":
    main()
