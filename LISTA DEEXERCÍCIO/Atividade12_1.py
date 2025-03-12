elemento = int(input("Quantos elementos na lista?: "))
lista_numeros=[]

for i in range(elemento):
    lista_numeros.append(int(input("Digite o numéro da lista: ")))

print(lista_numeros)

for j in range(elemento):
    for k in range(elemento):
        if lista_numeros[j] < lista_numeros[k]:

            troca = lista_numeros[j]

            lista_numeros[j] = lista_numeros[k]
            lista_numeros[k] = troca
            
            exit

elemento -=1
print(f"O maior numéro é {lista_numeros[elemento]}")