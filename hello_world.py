if True:
  print("True")
else:
  print("False")

# Este é um comentário de uma única linha

"""
Este é um comentário
de várias linhas
"""

Diferente de outras linguagens, o Python não requer o uso de ponto e vírgula (;) ao final de cada instrução. No entanto, se você desejar escrever várias instruções em uma única linha, pode separá-las com um ponto e vírgula. Por exemplo:
instrucao1; instrucao2; instrucao3

Uso de parênteses
Os parênteses são utilizados para agrupar expressões, definir funções e realizar chamadas a funções. Por exemplo:
resultado = (a + b) * c

Tipos de dados básicos
Em python, os tipos de dados básicos são as categorias nas quais podemos classificar os valores que utlizamos em nossos programas.
Compreender os diferentes tipos de dados é fundamental para trabalhar com variáveis e realizar operações em python. os tipos de dados básicos incluem:

inteiros (int)
idade = 34
quantidade = 100

flutuantes (float)
preco = 9.99
altura = 1.85

cadeias de texto (strings)
nome = "Helder"
mensagem = 'Olá, Mundo!'

booleanos
é maior de idade = True
tem desconto = False


Declaração e atribuição de variáveis

nome = "Helder"
idade = 34
altura = 1.85
é estudante = True

Também pode atribuir o mesmo valor a várias variáveis em uma única linha usando o operador de atribuição múltipla:
a = b = c = 10

neste caso, as variáveis a, b e c terão o valor 10.

Regras para nomear variáveis

ao nomear variáveis em python, é importante seguir algumas regras para manter um código legível e evitar erros:

os nomes das variáveis só podem letras (a-z, A-Z), números (0-9) e sublinhados (_). Não podem começar com um número.
Não se pode usar palavras-chave reservadas do python como nomes de variáveis (por exemplo, if, else, for, while, etc.)
o pyhton diferente maiúsculas de minúsculas, então nome e Nome são variáveis diferentes.
recomenda-se usar nomes descritivos para as variáveis, que indiquem claramente seu propósito: nome, idade, total_vendas, etc.
seguindo essas regras, alguns exemplos de nomes  de variáveis válidos são:
idade
nome_completo
total_vendas
_contador

e alguns exemplos de nomes de variáveis inválidos são:
1idade # Começa com um número
nome-completo # usar um hífen em vez de um sublinhado
if # palavras-chave reservada do python

Aritméticos

soma (+): soma dois valores.
subtração (-): subtrai o segundo valor do primeiro.
multiplicação (*): multiplica dois valores.
divisão (/): divide o primeiro valor pelo segundo e devolve um resultado de tipo flutuante.
divisão inteira (//): divide o primeiro valor pelo segundo e devolve um resultado de tipo inteiro (a parte decimal é descartada).
módulo (%): devolve o resto da divisão entre o primeiro valor e o segundo.
exponenciação (**): eleva o primeiro valor à potência do segundo.

exemplos:
a = 10
b = 3

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
modulo = a % b
exponenciacao = a ** b

De comparação

igual a (==): devolve True se ambos os valores são iguais.
diferente de (!=): devolve True se os valores são diferentes.
maior que (>): devolve True se o primeiro valor é maior que o segundo.
menor que (<): devolve True se o primeiro valor é menor que o segundo.
maior ou igual que (>=): devolve True se o primeiro valor é maior ou igual que o segundo.
menor ou igual que (<=): devolve True se o primeiro valor é menor ou igual que o segundo.

exemplos:
a = 10
b = 3

igual = a == b
diferente = a != b
maior que = a > b
menor que = a < b
maior ou igual = a >= b
menor ou igual = a <= b


Lógicos

AND (and): devolve True se ambas as condições são verdadeiras.
OR (or): devolve True se ao menos uma das condições é verdadeira.
NOT (not): inverte o valor de uma condição, devolve True se a condição é falsa e False se a condição é verdadeira.

exemplo:

a = 10
b = 3

resultado_and = (a > 5) and (b < 5)
resultado_or = (a > 15) or (b < 5)
resultado_not = not (a > 5)

Estruturas condicionais

if condicao
  instrucao

idade = 18

if idade >= 18:
  print("você é maior de idade.")

if-else

idade = 15

if idade >= 18:
  print("você é maior de idade.")
else:
  print("você é menor de idade.")

if-elif-else
  
nota = 85

if note >= 90:
  print("excelente")
elif nota >= 80:
  print("muito bom")
elif nota >= 70:
  print("bom")
else:
  print("precisa melhorar")



Listas de compreensão
As listas de compreensão são uma forma concisa de criar novas listas baseadas em uma sequência existente. Permitem filtrar e transformar os elementos de uma lista em uma única linha de código.

nova_lista = [expressão for elemento in sequência if condição]
Exemplo:

números = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in números if x % 2 == 0]
print(quadrados)  # Imprime [4, 16]
Neste exemplo, é criada uma nova lista chamada quadrados, que contém os quadrados dos números pares da lista números. A expressão x ** 2 eleva cada elemento ao quadrado, e a condição if x % 2 == 0 filtra apenas os números pares.

