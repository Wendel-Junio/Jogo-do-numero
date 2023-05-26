import random

print("Bem vindo ao jogo de advinhação ")


numero_secreto = round(random.random() * 100)
numero_de_tentativas = 3
rodada = 1

for rodada in range(1, numero_de_tentativas + 1):

    print("Tentativa {} de {}".format(rodada, numero_de_tentativas))
    chute_str = input("Digite um numero de 1 a 100!: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if chute <1 or chute > 100:
        print("Ei ei ei, você deve chutar um número de 1 a 100!!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Voce acertou ebaa")
        break
    else:
        if maior:
            print("Voce errou, o seu chute foi maior que o numero secreto")
        elif menor:
            print("Voce errou, o seu chute foi menor que o numero secreto")

    rodada = rodada + 1


print("Fim do jogo")
