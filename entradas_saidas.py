
def pessoa():
  nome = input("Insira seu nome: ")
  idade = input("Insira sua idade: ")

  print(f"Olá, {nome}!")
  print(f"Você tem {idade} anos.")

pessoa()

def pessoa_2():
  idade = int(input("Insira sua idade: "))

  if idade >= 18:
    print("Você é maior de idade.")

  else:
    print("Você é menor de idade.")

pessoa_2()

def saida_de_dados():
  nome = "Juan"; idade = 25
  print(f"Olá, meu nome é {nome} e tenho {idade} anos.")

