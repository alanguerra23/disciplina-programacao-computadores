# Escreva um programa que leia uma string do usuário e imprima a string ao contrário usando um laço while.
def implimir_string_invertido():
  # Lê a string do usuário
  string = input("Digite uma string: ")

  # Inicializa a variável que armazenará a string invertida
  string_invertida = ""

  # Obtém o comprimento da string
  comprimento = len(string)

  # Inicializa o contador
  contador = comprimento - 1

  # Percorre a string do final ao começo usando um laço while
  while contador >= 0:
    # Adiciona o caractere atual da string à string invertida
    string_invertida += string[contador]

    # Decrementa o contador
    contador -= 1

  # Imprime a string invertida
  print("A string invertida é:", string_invertida)

implimir_string_invertido()
