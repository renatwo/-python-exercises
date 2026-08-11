VELOCIDADE_DA_LUZ = 299792458  # Velocidade da luz em metros por segundo


def mostrar_constante():
    print("A velocidade da luz é:", VELOCIDADE_DA_LUZ, "m/s")

    try:
        novo_valor = 300000000

        if novo_valor != VELOCIDADE_DA_LUZ:
            raise ValueError("uma constante não deve ser alterada")
    except ValueError as erro:
        print("Erro ao tentar alterar a constante:", erro)


if __name__ == "__main__":
    mostrar_constante()
