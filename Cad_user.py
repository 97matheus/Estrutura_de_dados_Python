import csv
import login_user
def Cadastro():
    #salva as informações nas variaveis
    nome = input("Digite seu nome")
    cpf = input('Digite seu cpf')
    senha = input("Digite sua senha")


    with open('usuario.csv', 'a', newline='') as csvfile: #abre o arquivo csv para inserir as informações do usuario
        fieldnames = ['cpf', 'senha', 'nome']  #parametro com o nome das colunas
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter= ';')
        writer.writerow({'cpf': cpf, 'senha': senha, 'nome': nome}) #insere as informações das variaveis nas colunas espeficicas

    n = input("1 - Efetuar login:\n"  # verificação se o valor digitado corresponde as opções apresentadas
              "2 - Voltar para o Menu principal:\n")
    while n != "1" and n != "2":
        n = input("1 - Efetuar login:\n"
                  "2 - Voltar para o Menu principal:\n")
    if n == "1":
        login_user.login() #chama o menu de login

