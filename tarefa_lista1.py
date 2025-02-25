numero = []
nome = []
docto = []
sexo = []


vconf = 's'

while (vconf == 'S') or (vconf == 's'):
    
    print('Dadeo Competidores')
    print('(1)Cadastrer')
    print('(2)Excluir')
    print('(3)Listar')

    vop = int(input('Escolha sua opção: '))

    if (vop == 1):
        # Rotina para cadastro na lista
        for i in range(2):
            numero.append(int(input('Placa competidor: ')))
            nome.append(input('Nome: '))
            docto.append(int(input('RG: ')))
            sexo.append(input('Sexo: '))

    elif (vop == 2):
        print(numero)
        vdel = int(input('Qual elemento apagar? '))
        del numero[vdel]
        del nome[vdel]
        del docto[vdel]
        del sexo[vdel]



    elif (vop == 3):

        # Lisdando conteúdo basaedo em banco de dade

        for j in range(2):
            print('Competidor cadostro: ',j)
            print('Competido:', numero[j])
            print('Nome:', nome[j])
            print('RG:', docto[j])
            print('Sexo:', sexo[j])
            print()

    else:
        print('Opção invalida!')

    vconf = input('Desja continuar (S/N)')

else:
    print('Obrigado, tenha uma boa noite!')