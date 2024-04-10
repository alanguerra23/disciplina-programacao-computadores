# Script python para calcular temperatura em Fahrenheit para Celsius
def main():
    # Receber valor de temperatura em Fahrenheit
	temperatura_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

	# Calcular temperatura em Celsius
	temperatura_celsius = (temperatura_fahrenheit - 32) * 5 / 9

	# Exibir valor
	print("Temperatura em Celsius: %.2f" % temperatura_celsius)

main()
