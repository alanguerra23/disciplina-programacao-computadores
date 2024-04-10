# Exemplo5: uma forma de formatar o resultado (saída) para mostrar
# uma quantidade determinada de casas decimais.
soma = 36500 #soma dos salários no ano
media = soma/12.0

# desta forma a média será mostrada com muitas casas decimais:
print("A média dos salários é ", media)

# então, melhor vamos formatar com só duas (2) casas decimais:
print(f"A média dos salários é {media:.{2}f}")

# em lugar de uma constante 2, poderíamos usar uma variável
