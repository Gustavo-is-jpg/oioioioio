cpf = []
nome = []
convenio =[]
medico = []
valor = []

vconf = 's'

while (vconf == 's') or (vconf == 'S'):

    print('')
    print('(1)Cadastrer')
    print('(2)Excluir')

    vop = int(input('Escolha sua opção: '))

    if (vop == 1):
        
            cpf.append(int(input('CPF: ')))
            nome.append((input('Nome do pasiente: ')))
            convenio.append((input('onvenio: ')))
            medico.append((input('Medico: ')))
            valor.append(float(input('Valor: ')))

    elif (vop == 2):
        
        for j in range(2):
            print(cpf)
            vdel = int(input('Qual elemento apagar? '))
            del cpf [vdel]
            del nome [vdel]
            del convenio [vdel]
            del medico [vdel]
            del valor [vdel]

    else:
        print('Opção invalida!')

    vconf = input('Desja continuar (S/N)')

else:
    print('Obridado por nós escolhe!')