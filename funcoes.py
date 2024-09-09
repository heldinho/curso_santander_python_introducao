def saudacao():
  print("Olá, mundo!")

saudacao()

def saudacao2(nome):
  print(f"Olá, {nome}!")

saudacao2("Helder")
saudacao2("mundo")

# Valores de retorno
def soma(a, b):
  return a + b

resultado = soma(3, 4)
print(resultado)

# Funções anônimas (lambda)
quadrado = lambda x: x ** 2
print(quadrado(5))

# Escopo das variáveis (local vs. global)
def funcao():
  variavel_local = 10
  print(variavel_local)

variavel_global = 20

def funcao2():
  print(variavel_global)

funcao()
funcao2()
print(variavel_global)
print(variavel_local)

def calcular_media(*numeros):
  soma = sum(numeros)
  cantidad = len(numeros)
  media = soma / cantidad
  return media

print("Media:", calcular_media(10,20,30,40))

def somar_3(x):
  return x + 3

somar = lambda x: x + 3

print(f"Surmale 3 a un numero: {somar(5)}")

def area_retangulo(base, altura):
  """
  Calcula a área de um retângulo.
  Args:
    base (float): A base do retângulo.
    altura (float): A altura do retângulo.
  
  Returns:
    float: A área do retângulo.
  """
  return base * altura

def soma_variavel(*numeros):
  total = 0
  for numero in numeros:
    total += numero
  return total

print(soma_variavel(1,2,3))
print(soma_variavel(4,5,6,7))
