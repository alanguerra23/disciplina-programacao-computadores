# Escreva um programa que leia uma lista de palavras do usuário e imprima a palavra mais longa da lista usando um laço for.
def implimir_palavra_longa():
  palavras = input("Digite uma lista de palavras separadas por espaço: ")

  lista_palavras = palavras.split()

  palavra_mais_longa = ""

  for palavra in lista_palavras:
    if len(palavra) > len(palavra_mais_longa):
      palavra_mais_longa = palavra

  print("A palavra mais longa é:", palavra_mais_longa)

implimir_palavra_longa()
