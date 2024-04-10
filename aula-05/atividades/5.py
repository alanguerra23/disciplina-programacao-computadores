# Script Verificar o Salário
def main():
    salario_recebido = float(input('Informe o seu salário: '))

    salario_gastado = float(input('Informe o total que você gastou: '))

    if salario_recebido > salario_gastado:
        print(f'Você recebeu R$ {salario_recebido} e gastou R$ {salario_gastado}, está dentro do orçamento')

    else:
        print(f'Você recebeu R$ {salario_recebido} e gastou R$ {salario_gastado}, e ultrapassou o orçamento')

main()
