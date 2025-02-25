
salario = float(input('Digite o seu salario:\t'))

if (salario <= 2259.20):
    print('Você não presisa pagar')

elif (salario >= 2259.21) or (salario <= 2826.65):
    aliquota = (salario * 0.75) - 169.44
    print('Você presisa pagar:', aliquota )

elif (salario >= 2826.66) or (salario <= 39751.05):
    aliquota = (salario * 0.150) - 381.44
    print('Você presisa pagar:', aliquota )


elif (salario >= 39751.06) or (salario <= 4664.68):
    aliquota = (salario * 0.225) - 662.77
    print('Você presisa pagar:', aliquota )


elif (salario >= 2259.21) or (salario <= 2826.65):
    aliquota = (salario * 0.275) - 896.00
    print('Você presisa pagar:', aliquota )

else:
    
    aliquota = (salario * 0.275) - 896.00
    print('Você presisa pagar:', aliquota )
