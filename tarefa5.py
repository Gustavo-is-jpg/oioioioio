
nota1 = float(input('Digite a nota 1:\t'))
nota2 = float(input('Digite a nota 2:\t'))
nota3 = float(input('Digite a nota 3:\t'))
nota4 = float(input('Digite a nota 4:\t'))

media = (nota1+nota2+nota3+nota4) / 4


print('\nA media é:', media)
if (media >= 0 and media <= 25):
    input('Reprovado')

elif (media >= 25.1 and media <=45):
    input('Recuperação')

elif (media >= 45.1 and media <=65):
    input('Conselho')
    
elif (media >= 65.1 and media <=80):
    input('Eexame')
    
else:
    input('Aprovado')
