# Escreva um programa que leia uma string do usuário e imprima o número de vogais (a, e, i, o, u) que aparecem na string usando um laço for
def implimir_vogais():
  # solicita que o usuário insira uma string
  string = input("Digite uma string: ")

  # inicializa o contador de vogais em 0
  num_vogais = 0

  # percorre cada caractere na string usando um laço for
  for caractere in string:
    # verifica se o caractere atual é uma vogal
    if caractere.lower() in "aeiou":
      # se for, incrementa o contador de vogais
      num_vogais += 1

  # imprime o número total de vogais encontradas na string
  print("Número de vogais na string: ", num_vogais)

implimir_vogais()
