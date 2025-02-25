import time
for j in range(30):
    for k in range(10):
        print('Contador interno', k)
        time.sleep(0.2)
    print('Contador externo', j)
    time.sleep(0.5)
