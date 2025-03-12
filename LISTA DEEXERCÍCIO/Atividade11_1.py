j = 0

while j == 0:
    print(f'''
    Infome o tipo de local de consumo

    Tipo R para residências
    Tipo C para comersial
    Tipo I para industrial
    ''')
    tipo = input('Coloque o tipo(R, C e I) de consumo:\t')

    if tipo == 'R' or tipo == 'r':
        localu = 'residências'
        kwh = float(input(f'Informe o KWH da {localu}:'))
        if kwh <= 500:
            valor = kwh * 0.40
            print(f'O preça da conta e de {valor}')

        elif kwh >= 500:
            valor = kwh * 0.65
            print(f'O preça da conta e de {valor}')
        j = 1


    elif tipo == 'C' or tipo == 'c':
        localu = 'comercio'
        kwh = float(input(f'Informe o KWH da {localu}:'))

        if kwh <= 1000:
            valor = kwh * 0.55
            print(f'O preça da conta e de {valor}')

        elif kwh >= 1000:
            valor = kwh * 0.60
            print(f'O preça da conta e de {valor}')
        j = 1


    elif tipo == 'I' or tipo == 'i':
        localu = 'Industrial'
        kwh = float(input(f'Informe o KWH da {localu}:'))

        if kwh <= 5000:
            valor = kwh * 0.55
            print(f'O preça da conta e de {valor}')

        elif kwh >= 5000:
            valor = kwh * 0.60
            print(f'O preça da conta e de {valor}')
        j = 1

    else:
        print('Tipo não emcontrado')