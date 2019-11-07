import menuCoord
import menuUsuario
import menuG

logincoordenador = "coord"
senhacoordenador = "123"
logingestor = "gestor"
senhagestor = "456"

def login():

    print("=-"*10)

    loginprincipal = input("1 - Usuário Comum:\n"
    "2 - Coordenador:\n"
    "3 - Gestor de Recursos:\n")

    if loginprincipal == "1":
        verificacao()
        menuUsuario()

    elif loginprincipal == "2":
        verificacao()
        menuCoord.menuCoordenador()


    elif loginprincipal == "3":
       verificacao()
       menuGestor()

def verificacao():

    podeparar = False

    while podeparar == False:

        loginDigitado = input("Digite seu Login: ")
        senhaDigitada = input("Digite sua senha: ")

        if loginDigitado == logincoordenador and senhaDigitada == senhacoordenador:
            podeparar = True
            print("Logado com Sucesso!")

        else:
            print("Login ou senha incorreta. Digite novamente!")
            loginDigitado = input("Digite seu Login: ")
            senhaDigitada = input("Digite sua senha: ")