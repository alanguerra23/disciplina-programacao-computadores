# Script para estrutura de decisão
def main():
    num1 = int(input('Digite o Primeiro Número: '))
    num2 = int(input('Digite o Segundo Número: '))

    if num1 > num2:
        print(f'O Primeiro número {num1} é maior que {num2}')

    elif num1 == num2:
        print(f'Os número {num1} e {num2} são iguais')
    
    else:
        print(f'O segundo número {num2} é maior que {num1}')


main()
