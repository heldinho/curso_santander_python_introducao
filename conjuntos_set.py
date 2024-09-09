frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 4, 5])

conjunto1 = {1,2,3}
conjunto2 = {3,4,5}

uniao = conjunto1 | conjunto2
print(uniao)

intersecao = conjunto1 & conjunto2
print(intersecao)

diferenca = conjunto1 - conjunto2
print(diferenca)

diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)

frutas.add("pera")
print(frutas)

frutas.remove("banana")
print(frutas)

frutas.discard("uva")
print(frutas)

frutas.clear()
print(frutas)
