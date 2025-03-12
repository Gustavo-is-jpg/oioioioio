salario = float(input('Digite o seu salario: '))
casa = float(input('Digite o valo da casa: '))
anos = int(input('Quantos anos você dezega paga essa casa: '))

prestacao = anos * 12
valo = prestacao // casa

if valo <= (salario*(30*100)):
    print('A cronpra da casa fiz aceita')

else:
    print('Recusada, salario baixo')
    