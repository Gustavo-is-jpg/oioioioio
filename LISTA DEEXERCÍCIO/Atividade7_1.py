distansia = float(input('Informe os km percorido com o carro: '))
dias = float(input('por qualtos dias você esta com  carro: '))

valorkm = (distansia // 0.15)
valordias = (dias // 1)

custo = valordias + valorkm

print(f'Custo por km: {valorkm}')
print(f'Custo por dias: {valordias}')
print(f'Total: {custo}')