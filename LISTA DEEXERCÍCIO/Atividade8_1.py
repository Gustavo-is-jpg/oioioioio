distansia = float(input('Qualtos km você quer viargar: '))

if distansia >= 200:
    valo = (distansia // 0.45)
    print('O valor que você tem que pagar é:', valo)

elif distansia<= 199:
    valo = (distansia // 0.50)
    print('O valor que você tem que pagar é:', valo)