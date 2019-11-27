import login_user
import csv

def menuCoordenador():

    #menu coordenador
    opCoord = input("1 - Visualizar as reuniões em que voce foi convidado \n"
    "2 - Criar reunião\n"
    "3 - Adicionar Participantes\n"
    "4 - Realocar reuniões de sala\n"
    "5 - Voltar ao menu principal\n")


    if opCoord == "1":
        with open('usuarioreuniao.csv') as csvfile: #abre o arquivo usuarioreuniao.csv
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                if row['Coordenador'] == 'sim': #consulta se o coordenador foi convidado, caso 'sim' mostra as informações da reunião
                    print('{} : {}\n {} : {}\n {} : {}\n {} : {}\n {} : {}\n {} : {}\n {} : {}'.format(
                    'Assunto', row['Assunto'], 'Data', row['Data'], 'Hora', row['Hora'], 'Local', row['Local'],
                    'Participantes', row['Participantes'], 'Ata', row['Ata'], 'Coordenador convidado',
                    row['Coordenador']))
            presenca = input("Marcar presença?(sim/nao)") #após verificar os dados da reunião,opção para confirmar presença
            if presenca == 'sim':
                with open('usuarioreuniao.csv', 'a', newline='') as csvfile:  # abre o arquivo csv
                    fieldnames = ['Assunto', 'Data', 'Hora', 'Local', 'Participantes', 'Ata', 'confirmacaocoord']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

                    writer.writerow({'confirmacaocoord': presenca}) #insere a informação no arquivo csv, confirmando ou nao sua presença
                print('Presença confirmada')
        menuCoordenador() #chama o menu coordenador.

    elif opCoord == "2": #criar reuniao
        Assunto = input("Digite o assunto da reunião")
        Data = input("Digite a data da reunião")
        Hora = input("Digite a Hora da reunião")
        Local = input("Digite a número sala da reunião")
        Participantes = input("Informe o nome dos participantes")
        Ata = input("Ata da reunião:")
        confcoord = input("Confirmar presença:")

        with open('usuarioreuniao.csv', 'a', newline='') as csvfile:   #abre o arquivo csv
            fieldnames = ['Assunto', 'Data', 'Hora', 'Local', 'Participantes', 'Ata', 'confirmacaocoord'] #parametros das colunas
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')


            writer.writerow({'Assunto': Assunto, 'Data': Data , 'Hora': Hora, 'Local': Local , 'Participantes': Participantes,
                            'Ata': Ata, 'confimacaocoord' : confcoord})  #inserir as informações nas colunas espeficicas do arquivo

        print("Reunião criada com sucesso!")
        menuCoordenador() #chama o menu corrdenador

    elif opCoord == "3": #adicionar participantes a reunião
        with open('usuarioreuniao.csv') as csvfile:#abre arquivo csv
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader: #verifica as linhas do arquivo
                if row['Coordenador'] == 'sim': #verifica se a presença do coordenador esta confirmada e mostra as informações da reuniao
                    print('{} : {}\n {} : {}\n {} : {}\n {} : {}\n {} : {}\n {} : {}\n {} : {}'.format(
                    'Assunto', row['Assunto'], 'Data', row['Data'], 'Hora', row['Hora'], 'Local', row['Local'],
                    'Participantes', row['Participantes'], 'Ata', row['Ata'], 'Coordenador convidado',
                    row['Coordenador']))

        Participantes = input("Informe o nome dos participante que deseja adicionar:") #armazena o nome do participante

        with open('usuarioreuniao.csv', 'a', newline='') as csvfile: #abre o arquivo csv usuarioreuniao.csv
            fieldnames = ['Participantes'] #coluna que deseja inserir
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writerow({'Participantes': Participantes})   #inserir a informação da variavel na coluna especifica mencionada
        menuCoordenador() #chama o menu coordenador

    elif opCoord == "4":
        with open('usuarioreuniao.csv') as csvfile: #abre o arquivo csv
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                if row['Coordenador'] == 'sim':  #verifica se a presença do coordenador esta confirmada e mostra as informações da reuniao
                    print('{} : {}\n {} : {}\n {} : {}\n {} : {}\n {} : {}\n {} : {}\n {} : {}'.format(
                    'Assunto', row['Assunto'], 'Data', row['Data'], 'Hora', row['Hora'], 'Local', row['Local'],
                    'Participantes', row['Participantes'], 'Ata', row['Ata'], 'Coordenador convidado',
                    row['Coordenador']))

        realocar = input('Digite a nova sala:') # insere informação na variavel

        with open('usuarioreuniao.csv', 'a', newline='') as csvfile: #abre arquivo csv
            fieldnames = ['Participantes']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writerow({'mudancasala': realocar}) #insere a informação na coluna especifica
        menuCoordenador() #chama o menu coordenador

    elif opCoord == "5":
        login_user.login() # chama o menu de login
