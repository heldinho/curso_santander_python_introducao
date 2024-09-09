try:
  arquivo = open("arquivo.txt", "r")

except FileNotFoundError:
  print("Erro: Arquivo não encontrado")

finally:
  arquivo.close()

# Exceções personalizadas

def funcao():
  # Código que pode gerar uma exceção personalizada
  if condicao:
    raise Exception("Descrição do erro")

try:
  funcao()

except Exception as e:
  print(f"Erro: {str(e)}")