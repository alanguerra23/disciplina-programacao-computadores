# Script para receber a e b, calcular da seguinte forma e exibir o resultado:
def main():
    # Receber valores de a e b
	a = float(input("Digite o valor de a: "))
	b = float(input("Digite o valor de b: "))

	# Calcular x
	x = (a + b) ** 2

	# Calcular y
	y = (a ** 2) * (2 * a * b + b ** 2)

	# Exibir valores
	print("x = %.2f" % x)
	print("y = %.2f" % y)

main()
