frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
  print(fruta)

contador = 0
while contador < 5:
  print(contador)
  contador += 1

contador_two = 0
while True:
  print(contador_two)
  contador_two += 1

  if contador_two == 5:
    break

for i in range(10):
  if i % 2 == 0:
    continue
  print(i)