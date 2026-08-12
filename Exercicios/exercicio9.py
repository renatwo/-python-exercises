class TiposdeVariaveis:
    # Variável da classe
    variavelGlobal = 10

    def mostrar_valores(self):
        # Variável local do método
        variavelLocal = 5

        print("Valor da variável da classe:", self.variavelGlobal)
        print("Valor da variável local:", variavelLocal)


if __name__ == "__main__":
    variaveis = TiposdeVariaveis()
    variaveis.mostrar_valores()
