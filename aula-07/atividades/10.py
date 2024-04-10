# Escreva um programa que leia duas listas de números do usuário e
# imprima a lista resultante da concatenação das duas listas usando um
# laço for.
def implimir_concatenacao():
  # Leitura das duas listas
  lista1 = list(map(int, input("Digite os números da primeira lista, separados por espaço: ").split()))
  lista2 = list(map(int, input("Digite os números da segunda lista, separados por espaço: ").split()))

  # Concatenação das listas usando um loop for
  concatenada = []
  for numero in lista1:
      concatenada.append(numero)
  for numero in lista2:
      concatenada.append(numero)

  # Imprime a lista concatenada resultante
  print("Lista concatenada: ", concatenada)

implimir_concatenacao()
