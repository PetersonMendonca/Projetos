# -*- coding: utf-8 -*-
"""Calculadora V3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lm_J5qT70H6wckBOjP787QrhgdeUU1ap
"""

'''
  Versão 1.0.0 da Calculadora 
  Criador Peterson Mendonça de Oliveira

  * Versão 1.0 - Kazuma - Inicio do Codigo
  * Versão 1.5 - Aqua - Erro na Configuração das Funções
  * Versão 2.0 - Megumin - Funções Operando Corretamente
  * Versão 2.5 - Darknes - Aprimoramento das Funções
  * Versão 3.0 - Albed0 - Adicionando mais Funções



import math

def func():
  print("\n")
  print("Valor Atual: ", resu)
  print("****************** Calculadora ******************")
  print("*            + - Somar                          *")
  print("*            - - Subtrair                       *")
  print("*            x - Multiplicar                    *")
  print("*            / - Dividir                        *")
  print("*            % - Porcentagem                    *")
  print("*            P - Potencia ( ^ )                 *")
  print("*            R - Raiz Quadrada                  *")
  print("*            F - Fatorial ( ! )                 *")
  print("*            AC - Limpar Resultado              *")
  print("*            0 - Sair da Calculadora            *")
  print("*************************************************")

def setValor1():
  return float(input("Valor 1: "))
def setValor2():
  return float(input("Valor 2: "))

resu = 0

while True:
  resu =+ resu
  h = []
  func()
  op = input("Função: ")

  if resu == 0:
    if op == "+": ## Somar
      print("\n")
      resu = setValor1() + setValor2()
      print(resu)
    elif op == "-": ## Subtrair
      print("\n")
      resu = setValor1() - setValor2()
      print(resu)
    elif op == "x": ## Multiplicar
      print("\n")
      resu = setValor1() * setValor2()
      print(resu)
    elif op == "/": ## Dividir
      print("\n")
      resu = setValor1() / setValor2()
      print(resu)
    elif op == "%": ## Porcentagem
      print("\n")
      print("Entre Valor depois com Porcentagem")
      resu = (setValor1() * setValor2()) / 100
      print(resu)
    elif op == "P" or op == "p": ## Potencia
      print("\n")
      resu = setValor1() ** setValor2()
      print(resu)
    elif op == "R" or op == "r": ## Raiz Quadrada
      print("\n")
      resu = math.sqrt(setValor1())
      print(resu)
    elif op == "F" or op == "f": ## Fatorial
      rs = 1
      fat = setValor1()
      while (fat > 0):
        rs = rs * fat
        fat -= 1
      resu = rs
      print(resu)
    elif op == "0": ## Sair do Programa
      print("\n")
      print("Obrigado por utilizar a calculadora !!!")
      break
    elif op == "ac" or op == "AC" or op == "Ac" or op == "aC": ## Limpar Variavel Resultado do Programa
      resu = 0
      print(resu)
    else: ## Erro valor errado
      print("\n")
      print("Erro 69 valor não aceito !!!")

  elif resu != 0:
    if  op == "+": ## Somar
      print("\n")
      resu = resu + setValor1()
      print("Total ",resu)
    elif op == "-": ## Subtrair
      print("\n")
      resu = resu - setValor1()
      print("Total ",resu)
    elif op == "x": ## Multiplicar
      print("\n")
      resu = resu * setValor1()
      print("Total ",resu)
    elif op == "/": ## Dividir
      print("\n")
      resu = resu / setValor1()
      print("Total ",resu)
    elif op == "%": ## Porcentagem
      print("\n")
      print("Entre com Porcentagem")
      resu = (resu * setValor1()) / 100
      print("Total ",resu)
    elif op == "P" or op == "p": ## Potencia
      print("\n")
      print("Entre com Potencia")
      resu = resu ** setValor2()
      print("Total ",resu)
    elif op == "R" or op == "r": ## Raiz Quadrada
      print("\n")
      resu = math.sqrt(resu)
      print("Total ",resu)
    elif op == "F" or op == "f": ## Fatorial
      rs = 1
      fat = resu
      while (fat > 0):
        rs = rs * fat
        fat -= 1
      resu = rs
      print(resu)
    elif op == "0": ## Sair do Programa
      print("\n")
      print("Obrigado por utilizar a calculadora !!!")
      break
    elif op == "ac" or op == "AC" or op == "Ac" or op == "aC": ## Limpar Variavel Resultado do Programa
      resu = 0
      print("Total ",resu)
    else: ## Erro valor errado
        print("\n")
        print("Erro 69 valor não aceito !!!")
  else: ## Erro valor errado
        print("\n")
        print("Erro 69 valor não aceito !!!")
'''

import math

# Classe de Funções Matematicas
class Calculadora:
  def __init__(self,vl1,vl2,resu):
    self.vl1 = vl1
    self.vl2 = vl2
    self.resu = resu
# Seta valor vl1
  def valorVl1(self, entrada):
    self.vl1 = entrada
    return True
# Seta valor vl2
  def valorVl2(self, entrada):
    self.vl2 = entrada
    return True
# Seta valor de resu
  def RetornoResu(self):
    self.resu = resu
    return self.resu
# Função Somar
  def soma(self): 
    if(self.resu == 0):
      return float(self.vl1) + float(self.vl2)
    elif(self.resu != 0):
      return self.resu + float(self.vl1)
# Função Subtrair
  def sub(self): 
    if(resu == 0):
      return float(self.vl1) - float(self.vl2)
    elif(resu != 0):
      return self.resu - float(self.vl1)
# Função Multiplicar
  def mult(self): 
    if(resu == 0):
      return float(self.vl1) * float(self.vl2)
    elif(resu != 0):
      return self.resu * float(self.vl1)
# Função Dividir
  def div(self): 
    if(resu == 0):
      return float(self.vl1) / float(self.vl2)
    elif(resu != 0):
      return self.resu / float(self.vl1)
# Função Porcentagem
  def Porcentagem(self): 
    if(resu == 0):
      return (float(self.vl1) * float(self.vl2))/100
    elif(resu != 0):
      return (float(self.vl1) * self.resu) / 100
# Função Potencia ^
  def Potencia(self): 
    if(resu == 0):
      return float(self.vl1) ** float(self.vl2)
    elif(resu != 0):
      return self.resu ** float(self.vl1)
# Função Raiz Quadrada
  def raiz(self): 
    if(resu == 0):
      return math.sqrt(float(self.vl1))
    elif(resu != 0):
      return math.sqrt(self.resu)
# Função Fatorial
  def Fatorial(self): 
    if(self.resu == 0):
      count = 1
      fat = float(self.vl1)
      while fat > 0 :
        count = count * fat
        fat -= 1
        self.resu = count
      return self.resu
    elif(self.resu != 0):
      count = 1
      fat = self.resu
      while (fat > 0):
        count = count * fat
        fat -= 1
        self.resu = count
      return self.resu

# Laço de Repetição Infinito
vl1 = None
vl2 = None
resu = 0

# Chama a Classe
new = Calculadora(vl1,vl2,resu)

while True:
  print("\n")
  print("Valor Atual: ", new.RetornoResu())
  print("****************** Calculadora ******************")
  print("*     + Somar          |     - Subtrair         *")
  print("*     x Multiplicar    |     / Dividir          *")
  print("*     % Porcentagem    |     P Potencia  ( ^ )  *")
  print("*     R Raiz Quadrada  |     F Fatorial  ( ! )  *")
  print("*            AC - Limpar Resultado              *")
  print("*            0 - Sair da Calculadora            *")
  print("*************************************************")
  func = input("Função: ")

# Chama Função Somar
  if (func == "+"):
    if(resu == 0):
      try:
        new.valorVl1(float(input("Valor1: ")))
        new.valorVl2(float(input("Valor2: ")))
        resu = new.soma() # Ativa função
        print(resu)
      except:
        print("Erro valor não aceito, Entre com função novamente !!!")
    elif(resu != 0):
      try:
        print("\n")
        new.valorVl1(float(input("Valor1: ")))
        resu = new.soma() # Ativa função
        print(resu)
      except:
        print("Erro valor não aceito, Entre com função novamente !!!")
# Chama Função Subtrair
  elif (func == "-"):
    if(resu == 0):
      try:
        new.valorVl1(float(input("Valor1: ")))
        new.valorVl2(float(input("Valor2: ")))
        resu = new.sub()
        print(resu)
      except:
        print("Erro valor não aceito, Entre com função novamente !!!")
    elif(resu != 0):
      try:
        print("\n")
        new.valorVl1(float(input("Valor1: ")))
        resu = new.sub()
        print(resu)
      except:
        print("Erro valor não aceito, Entre com função novamente !!!")
# Chama Função Multiplicar
  elif (func == "x" or func == "X"):
    if(resu == 0):
      try:
        new.valorVl1(float(input("Valor1: ")))
        new.valorVl2(float(input("Valor2: ")))
        resu = new.mult()
        print(resu)
      except:
        print("Erro valor não aceito, Entre com função novamente !!!")
    elif(resu != 0):
      try:
        print("\n")
        new.valorVl1(float(input("Valor1: ")))
        resu = new.mult()
        print(resu)
      except:
        print("Erro valor não aceito, Entre com função novamente !!!")
# Chama Função Dividir
  elif (func == "/"):
    if(resu == 0):
      try:
        new.valorVl1(float(input("Valor1: ")))
        new.valorVl2(float(input("Valor2: ")))
        resu = new.div()
        print(resu)
      except:
        print("Erro valor não aceito, Entre com função novamente !!!")
    elif(resu != 0):
      try:
        print("\n")
        new.valorVl1(float(input("Valor1: ")))
        resu = new.div()
        print(resu)
      except:
        print("Erro valor não aceito, Entre com função novamente !!!")
# Chama Função Porcentagem
  elif (func == "%"):
    if(resu == 0):
      try:
        new.valorVl1(float(input("Valor Porcen: ")))
        new.valorVl2(float(input("Valor Aplicar: ")))
        resu = new.Porcentagem()
        print(resu)
      except:
        print("Erro valor não aceito, Entre com função novamente !!!")
    elif(resu != 0):
      try:
        print("\n")
        new.valorVl1(float(input("Valor Porcen: ")))
        resu = new.Porcentagem()
        print(resu)
      except:
        print("Erro valor não aceito, Entre com função novamente !!!")
# Chama Função Potencia
  elif (func == "P" or func == "p"):
    if(resu == 0):
      try:
        new.valorVl1(float(input("Valor1: ")))
        new.valorVl2(float(input("Valor2: ")))
        resu = new.Potencia()
        print(resu)
      except:
        print("Erro valor não aceito, Entre com função novamente !!!")
    elif(resu != 0):
      try:
        print("\n")
        new.valorVl1(float(input("Valor: ")))
        resu = new.Potencia()
        print(resu)
      except:
        print("Erro valor não aceito, Entre com função novamente !!!")
# Chama Função Raiz Quadrada
  elif (func == "R" or func == "r"):
    if(resu == 0):
      try:
        new.valorVl1(float(input("Valor1: ")))
        resu = new.raiz()
        print(resu)
      except:
        print("Erro valor não aceito, Entre com função novamente !!!")
    elif(resu != 0):
      try:
        print("\n")
        resu = new.raiz()
        print(resu)
      except:
        print("Erro valor não aceito, Entre com função novamente !!!")
# Chama Função Fatorial
  elif (func == "F" or func == "f"):
    if(resu == 0):
      try:
        new.valorVl1(float(input("Valor1: ")))
        resu = new.Fatorial()
        print(resu)
      except:
        print("Erro valor não aceito, Entre com função novamente !!!")
    elif(resu != 0):
      try:
        print("\n")
        resu = new.Fatorial()
        print(resu)
      except:
        print("Erro valor não aceito, Entre com função novamente !!!")
# Chama Função Limpar
  elif (func == "ac" or func == "AC" or func == "Ac" or func == "aC"):
    resu = 0
# Chama Função Sair do Programa
  elif (func == "0"):
    print("Volte Sempre !!!")
    break
# Chama Função Erro Entrada
  else:
    print("Erro Valor de Função não aceito !!!")