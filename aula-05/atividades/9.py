# Script mostrar mumeros crescente
def main():
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite main um valor: '))

    if num1 <= 0 or num2 <= 0:
        print('Os Números Devem ser positivos')

    elif num1 > num2:
        print(num2)
        print(num1)

    else:
        print(num1)
        print(num2)

main()
