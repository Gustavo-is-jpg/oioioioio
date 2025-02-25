#LIVRO
livcodigo = []
livnome = []
livautor = []
livgenero = []
livlancamento = []
livmidia = []
livlocal = []
livdataentrada = []

#ALUNO
alra = []
alnome = []
alsobrenemo = []
alchsse = []
alescola = []
alperiodo = []
alemail = []
alnivel = []

#RESERVAS
resdataentrada = []
resdatasida = []
resnome = []
resgenero = []
resra = []
resemail = []
rescodego_do_pedido = []

vconf = 'S'
while (vconf == 'S') or (vconf == 's'):

    print('Boitergar')
    print('(1)Cadastrar o livro.')
    print('(2)Cadastrar-se o aluno.')
    print('(3)Faz uma resarva de um livro.')
    print('(4)Excluir Cadastro.')

    vop = int(input('Escolha uma opção: '))

    if (vop == 1):

              livcodigo.append(int(input('Código do Livro: ')))
              livnome.append(input('Nome do Livro: '))
              livautor.append(input('Autor do Livro: '))
              livgenero.append(input('Gênero dod Livro: '))
              livlancamento.append(input('Lançamento do Livro: '))
              livmidia.append(input('O Livro é físio ou dígital?'))
              livlocal.append(input('Endereço da Biblioteca: '))
              livdataentrada.append(input('Data de inscrição:'))

    elif (vop == 2):
            alra.append(int(input('Ra do aluno: ')))
            alnome.append(input('Nome do aluno: '))
            alsobrenemo.append(input('Sobrenemo do aluno: '))
            alchsse.append(input('Chasse do aluno: '))
            alescola.append(input('Escola da mautricula: '))
            alperiodo.append(input('O perido de amanhã, tarde ou noite: '))
            alemail.append(input('Email do aluno: '))
            alnivel.append(input('o aluno está em qual nivel de escolaridade: '))

    elif (vop == 3):
            print('Cadastro ')
            print('Código do Livro: ')
            print('Nome do Livro: ')
            print('Autor do Livro: ')
            print('Gênero do Livro: ')
            print('Lançamento do Livro: ')
            print('O Livro é físico ou dígital? ')
            print('Endereço da Biblioteca: ')
            print('Data de inscrição: ')

    elif (vop == 4):
        vdel = int(input('Qual elemento apagar? '))
        del livcodigo[vdel]
        del livnome[vdel]
        del livautor[vdel]
        del livgenero[vdel]
        del livlancamento[vdel]
        del livmidia [vdel]
        del livlocal[vdel]
        del livdataentrada[vdel]