from random import randint


def numero_aleatorio():
    aleatorio = randint(1, 50)
    chute = 0

    while aleatorio != chute:
        chute = int(input("digite um valor (1 a 50):"))
        if aleatorio == chute:
            print("Parabens!")
        else:
            print('Podre')
    numero_aleatorio()
