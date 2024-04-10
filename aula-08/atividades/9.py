def texto_mais_longo(*textos):
    return max(textos, key=len)


texto1 = input("Digite um texto: ")

texto2 = input("Digite outro texto: ")

texto3 = input("Digite mais um texto: ")

print("O texto mais longo é: {}".format(texto_mais_longo(texto1, texto2, texto3)))