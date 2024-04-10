# Script para verificar o genero informado
def main():
    genero = input('Informa uma letra entre m,M,F ou f: ')

    if genero == 'm' or genero == 'M':
        print('Gênero informado é Masculino!')

    elif genero == 'f' or genero == 'F':
        print('Gênero informado é Feminino!')

    else:
        print(f'Você informou {genero} e não é uma opção válida!')

main()
