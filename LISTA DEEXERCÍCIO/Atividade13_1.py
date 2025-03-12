#funções
def par(a):
    numero = a % 2
    if numero == 0:
        p = 'sim'

    elif numero != 0:
        p  ='não'
    return p


#código principal    
valor = float(input('Digite um valor:\t'))
result = par(valor)

print(result)