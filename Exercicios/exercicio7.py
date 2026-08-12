def entrada_de_dados():
    numero_int = int(input("Digite um número inteiro: "))
    numero_double = float(input("Digite um número decimal: "))

    soma = numero_int + numero_double
    print("A soma dos números é:", soma)            

if __name__ == "__main__":
    entrada_de_dados()