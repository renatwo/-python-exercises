def boas_vindas():
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")

    mensagem = f"Olá, {nome} {sobrenome}! Bem-vindo(a)!"
    print(mensagem)

if __name__ == "__main__":
    boas_vindas()