# Verificar senha
def main():
    senha_fornecida = input('Digite sua senha: ')

    senha_gerada = '1234'

    if senha_fornecida  == senha_gerada:
        print('Acesso Permitido')

    else:
        print('Acesso Negado')

main()
