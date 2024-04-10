# Escreva um programa que leia uma lista de números do usuário e
# imprima o maior e o menor número da lista usando um laço while
def implimir_maior_menor_numero():
  lista = [] # cria uma lista vazia
  n = int(input("Digite a quantidade de números que deseja inserir na lista: "))
  i = 0

  # laço para inserir os números na lista
  while i < n:
    num = float(input("Digite um número: "))
    lista.append(num)
    i += 1

  # encontra o maior e o menor número da lista
  maior = lista[0]
  menor = lista[0]
  i = 1
  while i < n:
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]
    i += 1

  # imprime o maior e o menor número da lista
  print("O maior número da lista é:", maior)
  print("O menor número da lista é:", menor)

implimir_maior_menor_numero()
