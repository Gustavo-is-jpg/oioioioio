velosidadecarro = float(input('Informe a volocidade do carra: '))

if velosidadecarro >= 80:
    mutavalo = velosidadecarro // 80
    muta = mutavalo * 5
    print(F'Você foi mutado em ${muta}')

else:
    Print('Você não foi mutado')