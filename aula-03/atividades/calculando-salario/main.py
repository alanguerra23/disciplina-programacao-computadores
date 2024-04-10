# Script python para calcular salário
def main():
    # Receber valores de horas trabalhadas, valor da hora e percentual de desconto
	horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))

	valor_hora = float(input("Digite o valor da hora: "))

	percentual_desconto = float(input("Digite o percentual de desconto: "))

	# Calcular salário bruto, desconto e salário líquido
	salario_bruto = horas_trabalhadas * valor_hora
    
	# Calcular desconto
	desconto = salario_bruto * (percentual_desconto / 100)

	# Calcular salário líquido
	salario_liquido = salario_bruto - desconto

	# Exibir valores
	print("Salário bruto: R$ %.2f" % salario_bruto)
	print("Desconto: R$ %.2f" % desconto)
	print("Salário líquido: R$ %.2f" % salario_liquido)

main()