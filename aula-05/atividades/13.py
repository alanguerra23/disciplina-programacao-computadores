def main():
    macas_compradas = int(input('Digite o numero de maças compradas: '))

    valor_por_maca = 0.30

    valor_por_maca_desconto = 0.25

    if macas_compradas < 12:
        calc = valor_por_maca * macas_compradas

        print(f'O Valor total pago é R${calc:.2f}')

    else:
        calc = valor_por_maca_desconto * macas_compradas

        print(f'O Valor total pago é R${calc:.2f}')

main()
