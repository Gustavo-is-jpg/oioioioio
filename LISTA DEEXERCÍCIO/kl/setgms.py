# Programa para entrar com valores uma lista e colocar em ordem crescente


#Código principal
element = int(input("Quantos elementos na lista?: "))
lista_numeros=[]

for i in range(element):
    lista_numeros.append(int(input("Digite um valor: ")))

print(lista_numeros)


for j in range(element):
    for k in range(element):
        if lista_numeros[j] < lista_numeros[k]:
            troca = lista_numeros[j]
            lista_numeros[j] = lista_numeros[k]
            lista_numeros[k] = troca
            exit

print(f"Sua lista ordenada é: {lista_numeros}")