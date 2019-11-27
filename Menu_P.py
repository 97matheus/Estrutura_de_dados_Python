import Cad_user
import login_user

def main():

    podeparar = False

    print(" " * 5 + "Morais corporation")   #menu principal
    print(" " * 9 + "E-meeting\n")

    while podeparar == False:

        op = (input(" 1 - Cadastrar Usuário: \n"" 2 - Efetuar Login: \n"))
        if op == "1":
            Cad_user.Cadastro() #chama o arquivo onde contem a função para cadastrar o usuário
            podeparar = True
        elif op == "2":
            login_user.login() # faz a verificação do login, de acordo com o login digitado, chama o menu especifico
            podeparar = True

        else:
            print("Você digitou uma opção inválida")


main()
