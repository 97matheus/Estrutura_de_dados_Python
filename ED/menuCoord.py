import classeReuniao

def menuCoordenador():

    reuniao = classeReuniao.Reuniao()
    opCoord = input("1 - Visualizar as reuniões em que foi confirmado a sua presença \n"
    "2 - Criar reunião\n"
    "3 - Editar atas\n"
    "4 - Realocar reuniões de sala\n"
    "5 - Adicionar participantes na lista de reuniões\n"
    "6 - Voltar ao Menu principal\n")

    if opCoord == "1":
        print("teste")
        # op1 = mostrar as reunioes que o coordenador foi convidado com json
        #armazenar a resposta do coordenador em confcoordenador que será armazenada no json

    elif opCoord == "2":
        reuniao.criarReuniaoCoord()
        reuniao.mostrarInf()
        # armazenar no json
        print("Reunião criada com sucesso!")

    elif opCoord == "3":
        print("Editar atas")