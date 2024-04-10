# Script para verificar valores que seja maior que o outro
def main():
    num1 = float(input('Digite um valor: '))
    num2 = float(input('Digite mais um valor: '))

    if num1 == num2:
        print(f'Os Valores não podem ser iguais')

    elif num1 > num2:
        print(f'O Número {num1} é maior que o Número {num2}')

    elif num2 > num1:
        print(f'O Número {num2} é maior que o Número {num1}')

    else:
        print('Não foi informado valores válidos')

main()
