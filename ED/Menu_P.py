import Cad_user
import login_user
import classeReuniao

def main():

    print("Morais corporation")

    print(" --------------- MENU ----------------")

    op = (input(" 1 - Cadastrar Usuário: \n"" 2 - Efetuar Login: \n"))
    if op == "1":
        Cad_user.Cadastro()
    elif op == "2":
        login_user.login()

    n = input("1 - Efetuar login:\n"
              "2 - Voltar para o Menu principal:\n")
    while n != '1' and n != '2':
        n = input("1 - Efetuar login:\n"
                  "2 - Voltar para o Menu principal:\n")
    if n == "1":
        login_user.login()
    elif n == "2":
        main()

main()

