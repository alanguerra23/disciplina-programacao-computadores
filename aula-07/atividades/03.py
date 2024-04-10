# Escreva um programa que leia uma lista de números do usuário e imprima a soma de todos os números da lista usando um laço for.
def implimir_soma_numeros():
  # Solicitando a entrada do usuário para obter os números
  numeros = input("Digite uma lista de números separados por espaço: ")

  # Separando a entrada em uma lista de números individuais
  numeros = numeros.split()

  # Inicializando a soma com zero
  soma = 0

  # Looping for para somar cada número da lista
  for numero in numeros:
    soma += int(numero)

  # Imprimindo a soma
  print("A soma dos números é:", soma)

implimir_soma_numeros()
