nome = 'Gustavo'
salario_atual = 1200.00

print('Fusionario:', nome)
print('salario dele é:', salario_atual)

sal = float(input(f'Digite o salario do(a) {nome}:\t' ))
por = float(input(f'Digite a porsemtajen do almento dele:\t'))

almerto = (salario_atual + (por*5.12))

print(f'O novo salario do(a) {nome} é {almerto}')

salario_atual = almerto

#Esta estranho esse calculo da linha 10