"""

Maquina Geradora de Jogos na Mega Sena

Version 0.1 Aqua
Version 0.2 Darknes
Version 0.3 LaLatina

Criado por Peterson Mendonça de Oliveira

"""

import random

while True:
    print("\n|                GERADOR DE JOGOS DA MEGA OU QUINA                 |")
    print("| 1 - Jogo da Mega Sena| 2 - Jogos da Quina | 3 - Sair do Programa |")
    escolha = int(input("Escolha: "))

    if escolha == 1:
        qtd = int(input("Quantidade de Jogos: "))
        for i in range(qtd):
            result = []  # Lista ou vetor
            while len(result) != 6:  # Retorna o tamanho da string.
                casa = random.randint(1, 60)
                if casa not in result:
                    result.append(casa)  # Insere um item no final da lista.
                    result.sort()  # Ordena na Ordem Numerica
            print("*****************************************")
            print(result[0]," - ", result[1], " - ", result[2], " - ", result[3]," - ", result[4]," - ", result[5])
            print("*****************************************")

    elif escolha == 2:
        qtd = int(input("Quantidade de Jogos: "))
        for i in range(qtd):
            result1 = [] # Lista ou vetor
            while len(result1) != 5: # retorna o tamanho da string.
                casa1 = random.randint(1, 60)
                if casa1 not in result1:
                    result1.append(casa1) # Insere um item no final da lista.
                    result1.sort()  # Ordena na Ordem Numerica
            print("********************************")
            print(result1[0], " - ", result1[1], " - ", result1[2], " - ", result1[3], " - ", result1[4])
            print("********************************")

    elif escolha == 3:
        print("Obrigado por Utilizar o Projeto!!!")
        break

    else:
        print("Faça uma Escolha Valida")