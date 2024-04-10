# verificar o resultado do jogo
def main():
    gools_time1 = int(input('Digite o Total de gools do time 1: '))
    gools_time2 = int(input('Digite o Total de gools do time 2: '))

    if gools_time1 == gools_time2:
        print('O Placar foi empate')

    elif gools_time1 > gools_time2:
        print(f'O Time 1 venceu de {gools_time1} x {gools_time2} do Time 2')

    else:
        print(f'O Time 2 venceu de {gools_time2} x {gools_time1} do Time 1')

main()
