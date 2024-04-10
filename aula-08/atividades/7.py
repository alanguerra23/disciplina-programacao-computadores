def palindromo(texto):
    texto = texto.replace(" ", "").lower()
    
    if texto == texto[::-1]:
        return True
    else:
        return False
    
texto = input("Digite um texto: ")

if palindromo(texto):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")