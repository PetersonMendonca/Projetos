from random import randint

sn = True

while sn:

    vl = randint(0,10)

    while True:
        print("\n")
        print("Jogo de adivinhação")
        print("Adivinhe qual o numero o computador escolheu de 0 a 10")
        ent = int(input("Escolha o Numero: "))

        if (ent == vl):
            print("\n")
            print("Parabens o numero que você escolheu esta correto!!!")
            break
        elif (ent != vl):
            print("\n")
            print("Desculpe Tente Novamente!!!")
    
    ent2 = input("Quer Jogar de Novo (S/N)?: ").lower()

    if (ent2 == "s"):
        print("\n")
        print("OK Vamos La!!!")
        sn = True
    elif (ent2 == "n"):
        print("\n")
        print("Obrigado por Jogar!!!")
        sn = False
    else:
        print("\n")
        print("Erro valor não aceito!!!")
        sn = False