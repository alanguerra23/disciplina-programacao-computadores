import datetime

# verificar idade
def main():
    ano_nascimento = int(input('Digite o Ano que você nasceu: '))

    get_date = datetime.date.today()

    current_year = get_date.year

    current_age = current_year - ano_nascimento

    if current_age == 16 or current_age == 17:
        print('Você pode Votar, mas não é obrigatório')

    elif current_age >= 18:
        print('A Votação é obrigatória')

    else:
        print('Você não tem idade para votar')

main()
