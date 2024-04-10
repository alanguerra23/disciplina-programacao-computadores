def calcula_valor_total(produtos):
    valor_total = 0
    for preco in produtos.values():
        valor_total += preco
    return valor_total


produtos = {'banana': 2.5, 'maçã': 3.0, 'abacaxi': 5.5}

valor_total = calcula_valor_total(produtos)

print(valor_total)