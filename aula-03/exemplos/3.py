salarioAtual = float(input("Digite o salário atual: "))
reajuste = float(input("Digite o reajuste: "))

salarioNovo = salarioAtual + (salarioAtual * (reajuste / 100))

print("O salário novo é {}".format(salarioNovo))