import time

print('Calculando ingressos bloco A')
for i in range(2001):
    if (i >= 500) and (i <= 800):
        noa = i * 20
    else:
        total_ingressos_blocoA = i * 20

total = total_ingressos_blocoA - noa
print(total)