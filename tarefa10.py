
import time

for cont in range(1,1001, 10):
    if (cont >=300) and (cont <=600):
        print('Desclassificado')
    else:
        print('Ciclista, posição,', cont)
    time.sleep(0.5)
