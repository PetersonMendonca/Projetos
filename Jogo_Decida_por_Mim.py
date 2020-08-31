"""
from random import *
random.seed() #inicia a semente dos número pseudo randômicos
random.randrange(0, 9, 2) # pares entre 0 e 9
random.choice('abcdefghij') # seleciona um dos elementos aleatoriamente
items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items) # embaralha os itens aleatoriamente

"""

# Import da ferramentas random
from random import randint, choice

# Laço de repetição Infinito
while True:
    print("\n")
    ent1 = int(input("Quer Jogar | SIM = 1 | NÃO = 2 | ?: "))

    if (ent1 == 1):
        # Entrada do usuario
        ent = input("Entre com sua Pergunta: ")

        # Lista de elementos usados para resposta
        lista1 = ("Talvez","Pode ser","Acho que Sim","Acho que não","Não", "Sim", "Jamais", "Concerteza")

        # Seleciona valor aleatorio dentro da lista
        resposta = choice(lista1) 

        # Retorno da pergunta e da resposta gerada
        print(ent,resposta)
    elif (ent1 == 2):
        print("\n")
        print("Obrigado por Utilizar o Decida por Mim !!!!")
        break
    else:
        print("\n")
        print("Erro valor não aceito")