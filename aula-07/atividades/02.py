# Escreva um programa que leia um número inteiro positivo n do usuário e imprima os n primeiros números naturais (de 1 a n) usando um laço for.
def implimir_numeros_naturais():
  n = int(input("Digite um número inteiro positivo: "))

  for i in range(1, n+1):
    print(i)

implimir_numeros_naturais()
