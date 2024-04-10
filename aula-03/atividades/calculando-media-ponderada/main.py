# Script Python para calcular média ponderada
def main():
    # receber 3 notas com input
	nota1 = float(input("Digite a primeira nota: "))
	nota2 = float(input("Digite a segunda nota: "))
	nota3 = float(input("Digite a terceira nota: "))

	# calcular a média com essa formular nota1 * 2 + nota2 * 3 + nota3 * 5 / 10
	media = (nota1 * 2) + (nota2 * 3) + (nota3 * 5) / 10

	# imprimir a média com print
	print(f'A média ponderada é {media}')

main()
