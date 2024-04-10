def sao_anagramas(texto1, texto2):
    texto1 = texto1.lower().replace(" ", "")
    texto2 = texto2.lower().replace(" ", "")

    if len(texto1) != len(texto2):
        return False
    
    lista_texto1 = sorted(list(texto1))
    lista_texto2 = sorted(list(texto2))

    if lista_texto1 == lista_texto2:
        return True
    else:
        return False
    
texto1 = input("Digite o primeiro texto: ")

texto2 = input("Digite o segundo texto: ")

if sao_anagramas(texto1, texto2):
    print("São anagramas!")

else:
    print("Não são anagramas!")
