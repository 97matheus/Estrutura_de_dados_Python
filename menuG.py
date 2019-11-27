import login_user
import csv

def menuGestor():
    #menu principal do gestor
    op3 = (input("1 - Confirmar local de reuniões\n"
                 "2 - Cadastrar novos espaços de reunião\n"
                 "3 - Voltar ao menu principal\n"))
    if op3 == "1":
        with open('usuarioreuniao.csv') as csvfile: #consulta o arquivo e lista as informações das reunioes
            reader = csv.DictReader(csvfile, delimiter=';')

            for row in reader:
                    print('{} : {}\n {} : {}\n {} : {}\n {} : {}\n {} : {}\n {} : {}\n {} : {}'.format(
                        'Assunto', row['Assunto'], 'Data', row['Data'], 'Hora', row['Hora'], 'Local', row['Local'],
                        'Participantes', row['Participantes'], 'Ata', row['Ata'], 'Presença Coordenador',
                        row['confirmacaocoord']))

        confirmacao = input("Digite sim/nao para confirmar o local:")
        with open('usuarioreuniao.csv', 'a', newline='') as csvfile:  # abre o arquivo usuarioreuniaocsv e insere a informação de confirmação do local da reunião
            fieldnames = ['Assunto', 'Data', 'Hora', 'Local', 'Participantes', 'Coordenador', 'Ata', 'confirmacaocoord',
                          'confirmacaogestor', 'novoespaco']  # parametros das colunas do arquivo
            writer = csv.DictWriter(csvfile,fieldnames=fieldnames, delimiter=';')
            writer.writerow({'confirmacaogestor': confirmacao}) #insere a informação na coluna especifica desejada
        menuGestor() #chama o menu do gestor

    elif op3 == "2":
        novoespaco = input('Digite o nome do novo local:')
        with open('usuarioreuniao.csv', 'a', newline='') as csvfile:  # abre o arquivo usuarioreuniaocsv e insere a informação do novo espaço para reunioes
            fieldnames = ['Assunto', 'Data', 'Hora', 'Local', 'Participantes', 'Coordenador', 'Ata', 'confirmacaocoord',
                          'confirmacaogestor', 'novoespaco']  # parametros das colunas do arquivo
            writer = csv.DictWriter(csvfile,fieldnames=fieldnames, delimiter=';')
            writer.writerow({'novoespaco': novoespaco}) #insere a informação na coluna especifica desejada
        menuGestor()  #chama o menu do gestor

    elif op3 == "3":
        login_user.login() #chama o menu de login