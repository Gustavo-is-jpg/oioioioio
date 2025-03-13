# listas

cpf = [12345]
Nome =['guatvo']
sexo = ['m']
bairro = ['xery']
Responsaveis = ['jdj']

loop = 's'


while loop == 's':
    print("Menu:")
    print("1. Cadastrar registro")
    print("2. Alterar registro")
    print("3. Excluir registro")
    print("4. Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
         qualtos = int(input('Qualtos alunos e para cadastrar:'))

         for i in range(qualtos):
            Nome.append(input('Digite o nome do aluno: '))
            cpf.append(int(input('Digite o CPF do aluno: ')))
            sexo.append(input('Digite o sexo do aluno: '))
            bairro.append(input('Digite o bairro do aluno: '))
            Responsaveis.append(input('Digite o nome do responsaveris: '))
            print('')

    elif opcao == 2:

        print('Digite o CPF do aluno')
        alterar = int(input("Digite qual deseja alterar: "))
        if alterar in (cpf):
            Nome[alterar] = input("Digite o novo nome: ")
            sexo[alterar] = input("Digite o novo sexo: ")
            bairro[alterar] = input("Digite o novo bairro: ")
            Responsaveis[alterar] = input("Digite o novo responsável: ")
        else:
         print("alteraçâo inválido.")

    elif opcao == 3:
        #Função Deletar

        vdel = int(input('Qual elemento apagar?'))
        del cpf[vdel]
        del nome [vdel]
        del sexo[vdel]
        del bairro[vdel]
        del responsaveis[vdel]
        print(cpf)

    elif opcao == 4:
        print("Saindo do programa...")
        loop = 'n'


    else:
        print("Opção inválida!")