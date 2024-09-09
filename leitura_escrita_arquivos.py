def read_file():
  file = open("dados.txt", "r"); content = file.read(); print(content); file.close()

def write_file():
  file = open("dados.txt", "w"); file.write("Olá, mundo!"); file.close()

def read_2_file():
  with open("dados.txt", "r") as file: # abri e fecha automaticamente um arquivo
    content = file.read(); print(content)

read_file(); write_file(); read_2_file()