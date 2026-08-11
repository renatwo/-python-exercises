def conversao_de_tipos():
    valor_float = 9.99
    valor_int = int(valor_float)  # Conversão explícita de float para int
    numero = 10
    numero_convertido = float(numero)  # Conversão explícita de int para float

    print("Valor float:", valor_float)
    print("Valor convertido:", valor_int)
    print("Número int:", numero)
    print("Número convertido para float:", numero_convertido)

if __name__ == "__main__":
    conversao_de_tipos()
