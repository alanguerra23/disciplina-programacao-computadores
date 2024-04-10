# Escreva um programa que leia um número inteiro positivo n do usuário e
# imprima se n é primo ou não usando um laço while.
def implimir_numero_primo():
  n = int(input("Digite um número inteiro positivo: "))

  # Verifica se o número é menor que 2, pois nesse caso não é primo
  if n < 2:
      print(n, "não é primo.")
  else:
    # Inicializa a variável que contará a quantidade de divisores
    div = 0
    # Inicializa o contador para testar cada possível divisor
    i = 1
    while i <= n:
      # Verifica se i é um divisor de n
      if n % i == 0:
          div += 1
      # Se já encontrou mais de 2 divisores, interrompe o laço
      if div > 2:
          break
      i += 1
    # Se encontrou exatamente 2 divisores, o número é primo
    if div == 2:
        print(n, "é primo.")
    else:
        print(n, "não é primo.")

implimir_numero_primo()
