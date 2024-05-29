import random

def jogo_advinhação():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("bem-vindo ao jogo de advinhação")
    print("estou pensando em um número entre 1 a 100.")

    while True:
        try:
            palpite = int(input("Digite o seu palpite"))
            tentativas += 1

            if palpite < numero_secreto:
                print("muito baixo")
            elif palpite > numero_secreto:
                print("muito alto")
            else:
                print(f"Parabéns, vc acertou o número em {tentativas} tentativas")
                break
        except ValueError:
            print(" por favaor digite um número válido")

if __name__ == "__main__":
    jogo_advinhação()        

