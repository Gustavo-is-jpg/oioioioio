import math

vconf = 's'

while vconf == 's' or vconf == 'S':
    print()
    print('CALCOLO DE METRO CÚBICOS')
    print()
    print('DIGITE 1-cAIXA / 2-CILINDRO / 3-TRIANGULO')

    verp = input('Qual opção(1/2)?\t')

    if (verp == '1'): #Calculo da caixa
        base = float(input('Valor da basa: '))
        fror = float(input('Valor da profundidade: '))
        altura = float(input('Valor da altura: '))

        calc = ((base*fror*altura) * 1000)

        print(f'''A caixa com dimensões acima tem 
         o volume de {calc:.3f} litros''')

    elif (verp == '2'): #calculo do cilindo

        raio = float(input('Valor do raio: '))
        altura = float(input('Valor da altura: '))

        calc = ((math.pi * (raio**2) * altura) * 1000)
        print(f'A cilindro com dimensões acima tem\no volume de {calc:.2f} litros')

    elif (verp == '3'): 
        basa = float(input('Valor da basa: '))
        altura = float(input('Valor da altura: '))

        calc = ((basa * altura) / 2)
        print(f'A ária do triangolo com dimensões acima tem\no volume de {calc:.2f} litros')

    else: #escolha errada
        print('Opção inválida')


    vconf = input('Deseja continuar (S/N)? ')