frutas = ["maçã", "banana", "laranja"]

print(frutas[0]); print(frutas[1]); print(frutas[2])

print(frutas[-1]); print(frutas[-2]); print(frutas[-3])

frutas.append("pera") # adiciona um elemento ao final da lista.
print(frutas)

frutas.insert(1, "uva") # insere um elemento em uma posição especifica da lista.
print(frutas)

frutas.remove("banana") # remove a primeira ocorrência de um elemento na lista.
print(frutas)

fruta_removida = frutas.pop(2) # remove e retorna o elemento em uma posição especifica da lista.
print(frutas)
print(fruta_removida)

frutas.sort() # ordena os elementos da lista em ordem ascendente.
print(frutas)

frutas.reverse() # inverte a ordem dos elementos na lista.
print(frutas)


# Listas de compreensão

numeros = [1, 2, 3, 4, 5]
quadrado = [x ** 2 for x in numeros if x % 2 == 0]
print(quadrado)