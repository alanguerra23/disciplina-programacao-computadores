# Escreva um programa que leia um número inteiro positivo n do usuário e imprima a tabuada de n (de 1 a 10) usando um laço for.
def implimir_tabuada():
  n = int(input("Digite um número inteiro positivo: "))

  print("Tabuada de", n)

  for i in range(1, 11):
      print(n, "x", i, "=", n*i)

implimir_tabuada()
