# Script para verificar se o numero é negativo ou positivo
def main():
    numero = int(input('Digite um Número: '))

    if numero > 0:
        print(f'O Número {numero} é Positivo')

    elif numero == 0:
        print(f'O Número {numero} é neutro')

    else:
        print(f'O Número é negativo')

main()
