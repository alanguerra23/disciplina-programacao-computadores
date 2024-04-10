def contar_palavras(texto):
    palavras = texto.split()

    num_palavras = len(palavras)
    
    return num_palavras

texto = input('Digite um texto: ')

print(contar_palavras(texto))
