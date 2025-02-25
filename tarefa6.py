
vnf = float(input('Valor da nota fiscal:\t'))

uf_destino = input('Qual estado:\t')

if (uf_destino =='SP') or (uf_destino == 'sp'):
    vicms = vnf * 0.18
    print('Valor ICMS', vicms, 'para o estado de',uf_destino)

elif (uf_destino =='PR') or (uf_destino == 'pr') or (uf_destino =='MG') or (uf_destino == 'mg'):
    vicms = vnf * 0.07
    print('Valor ICMS', vicms, 'para o estado de',uf_destino)

elif (uf_destino =='GO') or (uf_destino == 'go'):
    vicms = vnf * 0.12
    print('Valor ICMS', vicms, 'para o estado de',uf_destino)

elif (uf_destino =='TO') or (uf_destino == 'to'):
    vicms = vnf * 0.5
    print('Valor ICMS', vicms, 'para o estado de',uf_destino)

elif (uf_destino =='RJ') or (uf_destino == 'rj') or (uf_destino =='BA') or (uf_destino == 'ba'):
    vicms = vnf * 0.9
    print('Valor ICMS', vicms, 'para o estado de',uf_destino)

else:
    print('O estado que vocé colocou não foi escortrado ')
