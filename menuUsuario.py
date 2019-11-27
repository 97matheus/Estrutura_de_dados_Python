import login_user
import csv


def menuUser():
    #menu principal usuário comum
    opUsuario = (input("1 - Criar Reunião\n"       
                       "2 - Visualizar Atas das reuniões\n"
                       "3 - Visualizar reuniões\n"
                       "4 - Voltar ao menu principal\n"))


    if opUsuario == "1":   #cria a reuniao e armazena as informações no arquivo csv
        Assunto = input("Digite o assunto da reunião")
        Data = input("Digite a data da reunião")
        Hora = input("Digite a Hora da reunião")
        Local = input("Digite a sala da reunião")
        Participantes = input("Informe o nome dos participantes")
        ConvidarCoordenador = input("Convidar coordenador?(sim/nao)")
        Ata = input("Ata da reunião:")

        with open('usuarioreuniao.csv', 'a', newline='') as csvfile:   #abre o arquivo csv e salva as informações
            fieldnames = ['Assunto', 'Data', 'Hora', 'Local', 'Participantes' , 'Coordenador', 'Ata'] #parametros das colunas do arquivo
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

            writer.writerow({'Assunto': Assunto, 'Data': Data , 'Hora': Hora, 'Local': Local , 'Participantes': Participantes,
                             'Coordenador': ConvidarCoordenador, 'Ata': Ata})  #insere as informações nas colunas espeficicas

        print("Reunião criada com sucesso!\n"
              "Por favor, aguarde a confirmação do local") #o gestor vai inserir a informação no arquivo da reuniao,
                                                            #confirmando o local da reuniao que foi inserido
        menuUser() # chama o menu do usuário

    elif opUsuario == "2":  #abre o arquivo csv 'usuarioreuniao.csv' e mostra a coluna com o nome Ata.
        with open('usuarioreuniao.csv','r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                print(row['Ata']) #coluna Ata com as informações que foram inseridas
        menuUser() # chama o menu do usuário

    elif opUsuario == "3":
        with open('usuarioreuniao.csv') as csvfile: #abre o arquivo reuniao
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:  # lista as reunioes que foram criadas
                    print('{} : {}\n {} : {}\n {} : {}\n {} : {}\n {} : {}\n {} : {}\n {} : {}'.format(
                        'Assunto', row['Assunto'], 'Data', row['Data'], 'Hora', row['Hora'], 'Local', row['Local'],
                        'Participantes', row['Participantes'], 'Ata', row['Ata'], 'Presença Coordenador', row['confirmacaocoord']))
        menuUser()

    elif opUsuario == "4":
        login_user.login() #chama o menu de login
