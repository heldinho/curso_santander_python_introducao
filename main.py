import operacoes
import utilidades

resultado = operacoes.somar(5, 3)
utilidades.imprimir_mensagem(f"O resultado da soma  é: {resultado}")

nome = utilidades.obter_nome_usuario()
utilidades.imprimir_mensagem(f"Olá, {nome}!")

from meu_pacote import modulo1, modulo2

modulo1.funcao_1()
modulo2.funcao_2()