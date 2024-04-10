def inverte_texto(texto):
    texto_invertido = texto[::-1]
    return texto_invertido

texto = input("Digite um texto: ")

print(inverte_texto(texto))
